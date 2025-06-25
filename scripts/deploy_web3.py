# scripts/deploy_web3.py

import json
import os
from web3 import Web3
from solcx import compile_standard, install_solc
from dotenv import load_dotenv

load_dotenv()

PRIVATE_KEY = os.getenv("PRIVATE_KEY")
INFURA_URL = os.getenv("INFURA_URL")

web3 = Web3(Web3.HTTPProvider(INFURA_URL))
account = web3.eth.account.from_key(PRIVATE_KEY)

def compile_contract(file_path):
    with open(file_path, "r") as f:
        source_code = f.read()

    install_solc("0.8.0")

    compiled = compile_standard({
        "language": "Solidity",
        "sources": {
            "Contract.sol": {"content": source_code}
        },
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "evm.bytecode"]}
            }
        }
    }, solc_version="0.8.0")

    return compiled

def deploy_to_testnet(compiled):
    abi = compiled["contracts"]["Contract.sol"]["Vulnerable"]["abi"]
    bytecode = compiled["contracts"]["Contract.sol"]["Vulnerable"]["evm"]["bytecode"]["object"]

    contract = web3.eth.contract(abi=abi, bytecode=bytecode)

    nonce = web3.eth.get_transaction_count(account.address)
    txn = contract.constructor().build_transaction({
        "from": account.address,
        "nonce": nonce,
        "gas": 3000000,
        "gasPrice": web3.to_wei("10", "gwei")
    })

    signed_txn = web3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    print(f"✅ Contract deployed at: {receipt.contractAddress}")

if __name__ == "__main__":
    path = input("🌐 Enter Solidity file path to deploy (testnet): ")
    if os.path.isfile(path):
        compiled = compile_contract(path)
        deploy_to_testnet(compiled)
    else:
        print("❌ Invalid file.")
