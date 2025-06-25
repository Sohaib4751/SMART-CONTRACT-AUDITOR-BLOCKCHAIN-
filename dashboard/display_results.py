from prettytable import PrettyTable
import json

def display_findings():
    with open("analysis/slither_output.json") as f:
        data = json.load(f)

    table = PrettyTable(["Check", "Impact", "Description"])
    for i in data.get("results", {}).get("detectors", []):
        table.add_row([i["check"], i["impact"], i["description"][:40] + "..."])

    print("\n📋 Vulnerability Report")
    print(table)

if __name__ == "__main__":
    display_findings()
