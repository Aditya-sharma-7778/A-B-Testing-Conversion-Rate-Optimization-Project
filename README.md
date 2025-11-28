# 📊 A/B Testing – Conversion Rate Optimization Project

This project evaluates whether a redesigned product page (Variant B) performs better than the existing version (Variant A) on an e-commerce platform.  
The experiment measures user behaviour across the funnel — Click-Through Rate, Add-to-Cart actions, and final Purchase Conversions — followed by statistical validation using p-value (T-Test).

---

## 🎯 Objective
To determine if **Variant B improves conversions significantly** compared to **Variant A**, and whether it should be rolled out to all users based on data evidence.

---

## 🛠 Tools & Technologies

| Category | Tools |
|---------|-------|
| Programming | Python (Pandas, NumPy, Matplotlib, SciPy) |
| Data Source | CSV-based A/B experiment dataset |
| Statistical Testing | T-Test, p-value significance testing |
| Visualization | Matplotlib Charts & Comparative Plots |

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `ab_test_dataset.csv` | Raw dataset containing 2,000 user interactions |
| `ab_test_analysis_main.py` | Complete analysis script + statistical testing + visualizations |
| `AB_Test_Project_Report_main.pdf` | Detailed business-ready summary report |
| `README.md` | Project documentation (this file) |

---

## 🔍 Approach & Workflow

### 1. **Data Loading & Cleaning**
- Imported CSV dataset using Pandas
- Checked null values, distribution shape & data consistency

### 2. **User Variant Segmentation**
- Split dataset into **Variant A** vs **Variant B**
- Computed base metrics for both groups

### 3. **Funnel Metric Computation**
- Click-Through Rate (CTR)
- Add-to-Cart Percentage
- Final Purchase Conversion Rate

### 4. **Statistical Hypothesis Testing**
- Null Hypothesis (H₀): No difference between A & B
- Applied **two-sample t-test**
- Evaluated p-value for significance (< 0.05 = improvement is real)

### 5. **Visualization & Insights**
- CTR comparison bar graph
- Add-to-Cart rate visualization
- Conversion performance chart
- Purchase distribution plot

---

## 📈 Key Experiment Results (Sample Output)

| Metric | Variant A | Variant B | Result |
|--------|-----------|-----------|--------|
| CTR | 8.4% | 11.2% | ↑ Better |
| Add-to-Cart Rate | 6.3% | 9.1% | ↑ Better |
| Purchase Conversion | 2.9% | 4.5% | ↑ +55% lift |
| **p-value** | 0.021 | **< 0.05** | 📌 Statistically Significant |

---

## 🔥 Conclusion

Variant B delivered **higher conversions, better engagement & a 55% lift in purchases**, validated through statistical confidence.  
📌 **Recommendation:** Roll out **Variant B** platform-wide to maximize revenue impact.

---

## 🧠 Skills Demonstrated

✔ A/B Experiment Design & Hypothesis Testing  
✔ Funnel + Cohort Metric Analysis  
✔ Python-based Analytics (Pandas, SciPy)  
✔ Data Visualization & Storytelling  
✔ Business Insight Derivation & Recommendation  

---
