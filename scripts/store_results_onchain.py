# scripts/store_results_onchain.py

import os
import json
import hashlib
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

PRIVATE_KEY = os.getenv("PRIVATE_KEY")
INFURA_URL = os.getenv("INFURA_URL")
CONTRACT_ADDRESS = os.getenv("AUDIT_CONTRACT_ADDRESS")

if not PRIVATE_KEY or not INFURA_URL or not CONTRACT_ADDRESS:
    raise EnvironmentError("Missing required environment variables. Check your .env file.")

web3 = Web3(Web3.HTTPProvider(INFURA_URL))
account = web3.eth.account.from_key(PRIVATE_KEY)

# Load compiled contract ABI
with open("contracts/AuditResults.json", "r") as f:
    contract_data = json.load(f)
abi = contract_data["abi"]
contract = web3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=abi)

def compute_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def save_results_to_chain(contract_address, ai_summary_path, timestamp):
    try:
        with open(ai_summary_path, "r") as f:
            ai_output = f.read()

        ai_hash = compute_hash(ai_output)

        nonce = web3.eth.get_transaction_count(account.address)
        txn = contract.functions.submitAudit(contract_address, ai_hash, timestamp).build_transaction({
            'from': account.address,
            'nonce': nonce,
            'gas': 300000,
            'gasPrice': web3.to_wei('10', 'gwei')
        })

        signed_txn = web3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        print(f"✅ Results stored on chain: {receipt.transactionHash.hex()}")
        print(f"🧠 AI Output Hash: {ai_hash}")
        return receipt.transactionHash.hex(), ai_hash

    except Exception as e:
        print(f"❌ Error while saving to chain: {e}")
        return None, None
