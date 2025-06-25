import os
import requests
from dotenv import load_dotenv

load_dotenv()

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
ETHERSCAN_API = "https://api.etherscan.io/api"

def is_valid_eth_address(address):
    return address.startswith("0x") and len(address) == 42

def fetch_contract_source(address, output_path="contracts/fetched_contract.sol"):
    if not ETHERSCAN_API_KEY:
        print("❌ Missing ETHERSCAN_API_KEY in .env")
        return

    if not is_valid_eth_address(address):
        print("❌ Invalid Ethereum address format.")
        return

    print(f"📡 Fetching source code for: {address}")

    params = {
        "module": "contract",
        "action": "getsourcecode",
        "address": address,
        "apikey": ETHERSCAN_API_KEY
    }

    try:
        response = requests.get(ETHERSCAN_API, params=params)
        data = response.json()

        if data["status"] == "1":
            source_code = data["result"][0]["SourceCode"]
            if not source_code:
                print("❌ No source code available.")
                return

            with open(output_path, "w") as f:
                f.write(source_code)
            print(f"✅ Contract saved to {output_path}")
            return output_path
        else:
            print("❌ Failed to fetch contract:", data["message"])
    except Exception as e:
        print("🚨 Error while fetching source code:", e)

if __name__ == "__main__":
    addr = input("🏦 Enter contract address from Etherscan: ").strip()
    fetch_contract_source(addr)
