import json
import os
from transformers import AutoTokenizer, AutoModelForCausalLM
from dotenv import load_dotenv

load_dotenv()

VULN_CATEGORIES = {
    "reentrancy": ["reentrancy"],
    "visibility": ["visibility", "public", "external"],
    "gas": ["gas", "loop"],
    "access_control": ["owner", "admin", "access", "authorization"],
    "math": ["overflow", "underflow", "arithmetic"],
    "dos": ["denial of service", "DoS"],
    "tx_origin": ["tx.origin"],
    "unchecked_call": ["call.value", "low-level call"],
}

def load_model():
    model_name = "Salesforce/codegen-2B-multi"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return model, tokenizer

def classify_vulnerability(description):
    description_lower = description.lower()
    for category, keywords in VULN_CATEGORIES.items():
        if any(keyword in description_lower for keyword in keywords):
            return category
    return "other"

def analyze_contract_code(model, tokenizer, contract_code):
    tokens = tokenizer(contract_code, return_tensors="pt", truncation=True, padding=True)
    output = model.generate(tokens['input_ids'], max_length=500)
    analysis_result = tokenizer.decode(output[0], skip_special_tokens=True)
    return analysis_result

def interpret_with_local_model(slither_output_path, output_path="analysis/final_ai_output.txt"):
    model, tokenizer = load_model()

    with open(slither_output_path, "r") as f:
        slither_json = json.load(f)

    issues = slither_json.get("results", {}).get("detectors", [])
    interpretations = []

    for issue in issues:
        description = issue.get("description", "")
        impact = issue.get("impact", "Unknown")
        confidence = issue.get("confidence", "Unknown")
        category = classify_vulnerability(description)

        prompt = f"""
# Vulnerability Description
{description}

# Impact
{impact}

# Confidence
{confidence}

# Task
Explain this vulnerability in simple terms, and provide a way to fix or mitigate it.
"""

        ai_summary = analyze_contract_code(model, tokenizer, prompt)

        interpretations.append({
            "description": description,
            "impact": impact,
            "confidence": confidence,
            "category": category,
            "ai_summary": ai_summary.strip()
        })

    with open(output_path, "w") as f:
        for i, item in enumerate(interpretations):
            f.write(f"🔐 Issue {i+1}:\n")
            f.write(f"Description: {item['description']}\n")
            f.write(f"Category: {item['category']}\n")
            f.write(f"Impact: {item['impact']}, Confidence: {item['confidence']}\n")
            f.write("AI Summary:\n")
            f.write(item['ai_summary'] + "\n\n")

    print(f"✅ AI-based interpretation saved to: {output_path}")
