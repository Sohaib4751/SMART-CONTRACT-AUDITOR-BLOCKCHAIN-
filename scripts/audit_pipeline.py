import os
from analyze_with_slither import run_slither
from ai_model.ai_analyze import interpret_with_local_model
from store_results_onchain import store_ai_result_onchain
from datetime import datetime

def full_audit(contract_path):
    print(f"\n🔍 Analyzing file: {contract_path}")
    run_slither(contract_path)

    # Use AI to interpret vulnerabilities
    interpret_with_local_model("analysis/slither_output.json", "analysis/final_ai_output.txt")

    # Ask user to store on blockchain
    store = input("📝 Do you want to store the results on blockchain? (y/n): ").lower()
    if store == 'y':
        contract_addr = input("📦 Enter the smart contract address (or path description): ").strip()
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        store_ai_result_onchain("analysis/final_ai_output.txt", contract_addr, timestamp)

    print("\n✅ Full audit complete. Check the 'analysis/' folder for results!")

if __name__ == "__main__":
    user_path = input("📂 Enter path to Solidity contract (e.g., contracts/sample_contract.sol): ").strip()

    if os.path.isfile(user_path) and user_path.endswith(".sol"):
        full_audit(user_path)
    else:
        print("❌ Invalid Solidity file. Please provide a valid .sol file path.")
