# SMART CONTRACT AUDITOR
# 🛡️ BLOCK AUDIT  
**Automated AI-Powered Smart Contract Security Analysis with On-Chain Audit Logging**

---

## 📘 Introduction  
Smart contracts are central to decentralized applications, but their immutability means vulnerabilities can be catastrophic. This project introduces **Block Audit**, an automated audit pipeline that combines static analysis, AI-based vulnerability summaries, and blockchain-based audit logging. It allows developers to identify vulnerabilities and immutably store results on-chain for verifiability and trust.

---

## 🎯 Project Objectives  
- Automate the detection of smart contract vulnerabilities  
- Generate human-readable audit summaries using Groq’s LLaMA-4  
- Store audit hashes and metadata on a local Ethereum blockchain (Ganache)  
- Support both Solidity file uploads and Etherscan-based contract fetching  

---

## 🏗️ System Architecture

### Input Layer
- Upload `.sol` file manually
- OR fetch verified contract source directly from Etherscan

### Processing Layer
- Slither performs static vulnerability analysis
- Groq’s LLaMA-4 generates AI-based summary
- SHA-256 used for hashing metadata (summary, timestamp)

### Storage Layer
- Results stored on-chain via a smart contract deployed to Ganache

### Interaction Layer
- CLI interface guides user through upload, scan, AI summary, and logging

---

## 🔩 Core Components

| Component File            | Description                                          |
|---------------------------|------------------------------------------------------|
| `final_pipeline.py`       | Coordinates full CLI-based pipeline workflow         |
| `fetch_from_etherscan.py` | Pulls contract source from Etherscan API             |
| `analyze_with_slither.py` | Runs Slither static analysis                         |
| `ai_analyze.py`           | Uses Groq API to summarize issues                    |
| `store_results_onchain.py`| Stores metadata hash and summary to local blockchain |
| `AuditResults.sol`        | Solidity smart contract to log and store audit data  |

---

## 🔁 Workflow Summary

```mermaid
graph TD
A[Upload .sol file or Fetch from Etherscan]
B[Run Slither Analysis]
C[Generate AI Summary (Groq)]
D[Store on Ganache Blockchain]
E[Display Results]
A --> B --> C --> D --> E
```

---

## 🧾 Smart Contract: `AuditResults.sol`

### Structure

```solidity
struct Audit {
  address submitter;
  string contractAddress;
  string aiSummaryHash;
  string timestamp;
}
```

### Functionality

- Records the contract address
- Saves SHA-256 hash of AI-generated summary
- Captures UTC timestamp
- Enables on-chain verifiability of audit data

---

## ⚙️ Technologies Used

| Tool/Library     | Purpose                                      |
|------------------|----------------------------------------------|
| Python 3.12      | Automation and backend scripting              |
| Solidity         | Smart contract development                   |
| Slither          | Static vulnerability detection               |
| Groq API (LLaMA-4)| AI-based vulnerability summarization         |
| Ganache          | Local Ethereum blockchain for audit logging  |
| Web3.py          | Smart contract interaction in Python         |
| `solcx`          | Compile specific Solidity versions dynamically|
| dotenv           | Secure environment configuration             |

---

## 🐞 Challenges & Fixes

| Issue                   | Fix                                                                 |
|-------------------------|----------------------------------------------------------------------|
| `solc` version mismatch | Automatically installed correct version using `solcx`               |
| ABI mismatch            | Ensured ABI JSON matches deployed contract                          |
| `.rawTransaction` error | Replaced with `.raw_transaction` to match Web3 version              |
| Gas errors              | Used Ganache faucet to refill dev accounts                          |
| Timestamp format issue  | Converted timestamp to string to match ABI input                    |

---

## 📋 Sample Audit Report Snippet

```
===============================
 SMART CONTRACT AUDIT REPORT
===============================
Contract: uploaded_contract.sol
Audited Using: Slither + Groq LLaMA-4

Issue 1: Reentrancy in withdraw()
----------------------------------
Impact: High
Confidence: Medium

AI Summary:
The withdraw() function lacks reentrancy protection...
```

---

## ⛓️ Blockchain Output Example

- Results stored on-chain: `0xABC123...`  
- AI Summary SHA-256 Hash: `6f2c9b8a0...`  

---

## 🚀 Future Enhancements

- Deploy to testnets/mainnets (e.g., Sepolia, Polygon)
- Store full audit reports on IPFS
- Multi-auditor authentication and access control
- Web dashboard with visual analytics of audit results

---

## 📌 Note  
This project was developed for educational purposes as part of coursework at **FAST-NUCES**.
