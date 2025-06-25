import subprocess
import os

def run_slither(contract_path):
    output_path = os.path.join("analysis", "slither_output.json")
    try:
        result = subprocess.run(['slither', contract_path, '--json', output_path],
                                capture_output=True, text=True)

        if result.returncode == 0 and os.path.exists(output_path):
            print(f"✅ Slither analysis completed. Results saved to {output_path}")
        else:
            print("❌ Slither failed or no output generated.")
            print("🔍 Details:", result.stderr)
    except Exception as e:
        print("🚨 Unexpected error while running Slither:", e)
