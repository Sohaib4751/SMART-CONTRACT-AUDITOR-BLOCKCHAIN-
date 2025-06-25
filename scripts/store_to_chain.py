import hashlib
import os
from web3 import Web3
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

PRIVATE_KEY = os.getenv("PRIVATE_KEY")
INFURA_URL = os.getenv("INFURA_URL")
CONTRACT_ADDRESS = os.getenv("AUDIT_CONTRACT_ADDRESS")
ABI_PATH = "contracts/AuditResults_abi.json"

def get_summary_hash(file_path):
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def push_result_to_chain(contract_address, ai_output_file, contract_str_addr):
    web3 = Web3(Web3.HTTPProvider(INFURA_URL))
    acct = web3.eth.account.from_key(PRIVATE_KEY)

    with open(ABI_PATH, "r") as abi_file:
        abi = abi_file.read()

    contract = web3.eth.contract(address=contract_address, abi=abi)

    summary_hash = get_summary_hash(ai_output_file)
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    txn = contract.functions.submitAudit(contract_str_addr, summary_hash, timestamp).build_transaction({
        "from": acct.address,
        "nonce": web3.eth.get_transaction_count(acct.address),
        "gas": 300000,
        "gasPrice": web3.to_wei("20", "gwei"),
    })

    signed_txn = acct.sign_transaction(txn)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    print(f"✅ Audit hash submitted. Tx: {receipt.transactionHash.hex()}")

if __name__ == "__main__":
    path = input("📂 Enter AI output file path: ")
    contract_ref = input("🔗 Enter contract address (or hash reference): ")
    push_result_to_chain(CONTRACT_ADDRESS, path, contract_ref)
