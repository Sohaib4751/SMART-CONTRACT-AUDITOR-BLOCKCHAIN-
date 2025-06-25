# SMART-CONTRACT-AUDITOR-BLOCKCHAIN-
# 🛡️ BLOCK AUDIT  
**Automated AI-Powered Smart Contract Security Analysis with On-Chain Audit Logging**

---

## 📘 Introduction  
Smart contracts are central to decentralized applications, but their immutability means vulnerabilities can be catastrophic. This project introduces **Block Audit**, an automated audit pipeline that combines:
- Static analysis,
- AI-based interpretation,
- And blockchain-based audit logging.

This allows developers to identify vulnerabilities and **immutably store audit results on-chain** for future verification.

---

## 🎯 Project Objectives  
- ✅ Automate detection of smart contract vulnerabilities  
- ✅ Generate human-readable audit summaries using Groq’s LLaMA-4  
- ✅ Hash audit results and store metadata on-chain via Ganache  
- ✅ Support both `.sol` uploads and Etherscan contract fetch  

---

## 🏗️ System Architecture

### **1. Input Layer**
- Upload `.sol` file **or**
- Fetch verified source code from **Etherscan**

### **2. Processing Layer**
- 🔍 Static Analysis via **Slither**
- 🤖 AI Summary Generation using **Groq’s LLaMA-4**
- 🧩 Metadata: SHA-256 hash, timestamp, address

### **3. Storage Layer**
- Save audit hash & metadata on-chain using **Solidity smart contract (AuditResults.sol)**

### **4. Interaction Layer**
- CLI guides users through:
  - File input or Etherscan fetch
  - Audit execution
  - AI interpretation
  - On-chain save

---

## 🔩 Core Components

| File                     | Description                                        |
|--------------------------|----------------------------------------------------|
| `final_pipeline.py`      | Main pipeline that runs the entire CLI flow        |
| `fetch_from_etherscan.py`| Retrieves contract source using Etherscan API      |
| `analyze_with_slither.py`| Runs Slither for static vulnerability analysis     |
| `ai_analyze.py`          | Interacts with Groq LLaMA-4 to summarize findings  |
| `store_results_onchain.py`| Stores audit results on local blockchain          |
| `AuditResults.sol`       | Solidity smart contract for audit metadata storage |

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
