# scripts/deploy_local.py

from web3 import Web3
from solcx import compile_standard, install_solc
import json
import os

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

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

def deploy_contract(compiled):
    abi = compiled["contracts"]["Contract.sol"]["Vulnerable"]["abi"]
    bytecode = compiled["contracts"]["Contract.sol"]["Vulnerable"]["evm"]["bytecode"]["object"]

    account = web3.eth.accounts[0]
    web3.eth.default_account = account

    Contract = web3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = Contract.constructor().transact()
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    print(f"✅ Deployed at address: {tx_receipt.contractAddress}")

if __name__ == "__main__":
    path = input("📝 Enter path to .sol file to deploy (e.g., contracts/sample_contract.sol): ")
    if os.path.isfile(path):
        compiled = compile_contract(path)
        deploy_contract(compiled)
    else:
        print("❌ Invalid path.")
