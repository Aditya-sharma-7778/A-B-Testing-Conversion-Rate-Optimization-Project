# A/B TESTING ANALYSIS PROJECT
# ------------------------------------
# Objective: Check whether Variant B performs better than Variant A
# in terms of engagement & conversion.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# -------------------------------
# 1️⃣ Load Dataset
# -------------------------------
df = pd.read_csv("ab_test_dataset.csv")   # <-- make sure this file is in same folder
print("\n---- DATA SAMPLE ----")
print(df.head())

print("\nTotal Rows:", len(df))
print(df.variant.value_counts())

# -------------------------------
# 2️⃣ Calculate Funnel Metrics
# -------------------------------

variantA = df[df.variant=="A"]
variantB = df[df.variant=="B"]

# CTR = Clicks / Views
ctr_A = variantA["click_through_rate"].mean()
ctr_B = variantB["click_through_rate"].mean()

add_to_cart_A = variantA["add_to_cart"].mean()
add_to_cart_B = variantB["add_to_cart"].mean()

conversion_A = variantA["purchase"].mean()
conversion_B = variantB["purchase"].mean()

print("\n----- Funnel Metrics -----")
print(f"CTR  A: {ctr_A:.3f} | CTR  B: {ctr_B:.3f}")
print(f"Add-to-Cart A: {add_to_cart_A:.3f} | Add-to-Cart B: {add_to_cart_B:.3f}")
print(f"Conversion A: {conversion_A:.3f} | Conversion B: {conversion_B:.3f}")

# Revenue Uplift / Improvement %
improvement = ((conversion_B - conversion_A) / conversion_A) * 100
print(f"\n📈 Conversion Uplift from Variant B → {improvement:.2f}%\n")

# -------------------------------
# 3️⃣ Statistical Significance Test
# -------------------------------
# We check if difference is real or by chance
z_stat, p_value = stats.ttest_ind(variantA.purchase, variantB.purchase)

print("----- Statistical Result -----")
print("P-Value:", p_value)

if p_value < 0.05:
    print("✔ Variant B performs significantly better (reject Null Hypothesis)")
else:
    print("❌ No significant difference found (fail to reject Null Hypothesis)")

# -------------------------------
# 4️⃣ Visualize Results
# -------------------------------

# Conversion Comparison Bar Chart
plt.bar(["Variant A","Variant B"], [conversion_A, conversion_B])
plt.title("Conversion Rate Comparison - A/B Test")
plt.ylabel("Conversion Rate")
plt.show()

# CTR Comparison
plt.bar(["Variant A","Variant B"], [ctr_A, ctr_B])
plt.title("Click Through Rate Comparison")
plt.ylabel("CTR")
plt.show()

# Add to Cart visualization
plt.bar(["Variant A","Variant B"], [add_to_cart_A, add_to_cart_B])
plt.title("Add to Cart Comparison")
plt.ylabel("Add to Cart %")
plt.show()

# Distribution visualization
variantA.purchase.hist(alpha=0.6)
variantB.purchase.hist(alpha=0.6)
plt.title("Purchase Distribution: Variant A vs B")
plt.show()

print("\n🔍 Final Interpretation:")
print("If Variant B has higher values & p-value < 0.05 → rollout Variant B across platform.")
