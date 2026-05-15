import matplotlib.pyplot as plt
import pandas as pd
import random

# =====================================================
# CONFIGURATION
# =====================================================

RISK_THRESHOLD = 0.6
MAX_QUANTUM_CHANNELS = 3   # Limited quantum resources

alpha = 0.7   # Risk weight
beta = 0.3    # Energy penalty weight

print("\n========= HQORA FULL IMPLEMENTATION =========\n")

# =====================================================
# LOAD DATA
# =====================================================

fitbit = pd.read_csv("data/fitbit_data.csv")
diabetes = pd.read_csv("data/diabetes.csv")

# =====================================================
# 1️⃣ DYNAMIC PRIVACY RISK PREDICTION
# =====================================================

def fitbit_risk(row):
    steps_norm = row['TotalSteps'] / 20000
    calories_norm = row['Calories'] / 5000
    risk = 0.4*steps_norm + 0.4*calories_norm + 0.2*0.5
    return min(risk, 1)

def diabetes_risk(row):
    glucose_norm = row['Glucose'] / 200
    bmi_norm = row['BMI'] / 50
    age_norm = row['Age'] / 100
    risk = 0.5*glucose_norm + 0.3*bmi_norm + 0.2*age_norm
    return min(risk, 1)

# =====================================================
# 2️⃣ EDGE-ASSISTED RESOURCE COLLECTION
# =====================================================

devices = []

# Fitbit devices
for i, row in fitbit.head(10).iterrows():
    risk = fitbit_risk(row)

    # 3️⃣ ENERGY-AWARE QKD ACTIVATION
    energy = random.uniform(0.2, 1.0)  # lower energy cost

    devices.append({
        "type": "Fitbit",
        "id": f"F{i+1}",
        "risk": risk,
        "energy": energy,
    })

# Medical devices
for i, row in diabetes.head(10).iterrows():
    risk = diabetes_risk(row)

    # Medical devices consume more energy
    energy = random.uniform(0.5, 1.2)

    devices.append({
        "type": "Medical",
        "id": f"M{i+1}",
        "risk": risk,
        "energy": energy,
    })

# =====================================================
# 4️⃣ MULTI-OBJECTIVE OPTIMIZATION (UTILITY FUNCTION)
# =====================================================

for device in devices:
    device["utility"] = alpha * device["risk"] - beta * device["energy"]

# Sort devices by utility (highest priority first)
devices_sorted = sorted(devices, key=lambda x: x["utility"], reverse=True)

# =====================================================
# 5️⃣ ADAPTIVE HYBRID SECURITY SWITCHING
# =====================================================

for idx, device in enumerate(devices_sorted):
    if idx < MAX_QUANTUM_CHANNELS:
        device["mode"] = "Quantum Mode"
    else:
        device["mode"] = "Classical Mode"

# =====================================================
# OUTPUT RESULTS
# =====================================================

for device in devices_sorted:
    print(f"Device ID: {device['id']} ({device['type']})")
    print(f"  Risk Score : {device['risk']:.3f}")
    print(f"  Energy Cost: {device['energy']:.3f}")
    print(f"  Utility    : {device['utility']:.3f}")
    print(f"  Mode       : {device['mode']}")
    print("--------------------------------------")

print("\nHQORA Full Resource Allocation Completed.")
# =====================================================
# PROFESSIONAL VISUALIZATION SECTION
# =====================================================

import os

if not os.path.exists("Output"):
    os.makedirs("Output")

risks = [d["risk"] for d in devices_sorted]
energies = [d["energy"] for d in devices_sorted]
utilities = [d["utility"] for d in devices_sorted]
modes = [d["mode"] for d in devices_sorted]

# 1️⃣ Quantum vs Classical Allocation
plt.figure(figsize=(6,4))
quantum_count = modes.count("Quantum Mode")
classical_count = modes.count("Classical Mode")

plt.bar(["Quantum", "Classical"], [quantum_count, classical_count])
plt.title("Quantum vs Classical Allocation")
plt.ylabel("Number of Devices")
plt.tight_layout()
plt.savefig("Output/quantum_vs_classical.png", dpi=300)
plt.show()

# 2️⃣ Risk vs Utility Scatter
plt.figure(figsize=(6,4))
plt.scatter(risks, utilities)
plt.xlabel("Risk Score")
plt.ylabel("Utility Value")
plt.title("Risk vs Utility Trade-off")
plt.tight_layout()
plt.savefig("Output/risk_vs_utility.png", dpi=300)
plt.show()

# 3️⃣ Energy vs Allocation
allocation_numeric = [1 if m == "Quantum Mode" else 0 for m in modes]

plt.figure(figsize=(6,4))
plt.scatter(energies, allocation_numeric)
plt.xlabel("Energy Cost")
plt.ylabel("Allocation (1 = Quantum, 0 = Classical)")
plt.title("Energy-Aware Quantum Allocation")
plt.tight_layout()
plt.savefig("Output/energy_vs_allocation.png", dpi=300)
plt.show()

# 4️⃣ Utility Ranking
plt.figure(figsize=(6,4))
plt.plot(utilities)
plt.xlabel("Device Priority Rank")
plt.ylabel("Utility Score")
plt.title("Sorted Utility Ranking")
plt.tight_layout()
plt.savefig("Output/utility_ranking.png", dpi=300)
plt.show()

print("\nGraphs saved inside 'Output' folder.")

# =====================================================
# SYSTEM PERFORMANCE EVALUATION
# =====================================================

print("\n========= SYSTEM PERFORMANCE EVALUATION =========")

# Baseline: All Classical Mode
baseline_total_risk = 0
for d in devices:
    baseline_risk = d["risk"] * 0.9   # classical reduces only 10%
    baseline_total_risk += baseline_risk

# HQORA Optimized System
hqora_total_risk = 0
for d in devices_sorted:
    if d["mode"] == "Quantum Mode":
        optimized_risk = d["risk"] * 0.6   # quantum reduces 40%
    else:
        optimized_risk = d["risk"] * 0.9
    hqora_total_risk += optimized_risk

improvement = ((baseline_total_risk - hqora_total_risk) / baseline_total_risk) * 100

print(f"Baseline System Risk : {baseline_total_risk:.3f}")
print(f"HQORA Optimized Risk : {hqora_total_risk:.3f}")
print(f"Security Improvement : {improvement:.2f}%")

# ---------------- Comparison Graph ----------------
plt.figure(figsize=(6,4))
plt.bar(["Baseline", "HQORA"], [baseline_total_risk, hqora_total_risk])
plt.ylabel("Total System Risk")
plt.title("System Risk Reduction Using HQORA")
plt.tight_layout()
plt.savefig("Output/system_risk_comparison.png", dpi=300)
plt.show()