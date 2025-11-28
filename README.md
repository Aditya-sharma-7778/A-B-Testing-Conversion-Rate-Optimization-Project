📊 A/B Testing – Conversion Rate Optimization Project
📌 Objective

This project analyzes whether a new product page UI (Variant B) performs better than the existing UI (Variant A) in an e-commerce platform.
Using A/B Testing, we compare CTR, Add-to-Cart behavior, final purchase conversion & validate improvement using statistical significance (p-value testing).

🛠 Tools & Technologies Used
Category	Tools
Programming	Python (Pandas, NumPy, Matplotlib, SciPy)
Data	CSV-Based A/B Experiment Dataset
Statistical Method	T-Test / p-value significance check
Visualization	Matplotlib Graphs & Comparison Charts
📂 Project Files
File	Purpose
ab_test_dataset.csv	Dataset used for analysis (2000 user records)
ab_test_analysis.py	Full Python script with analysis + visualizations
AB_Test_Project_Report_main.pdf	Summary report for review & presentation
README.md	Project documentation (you are reading it)
🔍 Analysis Steps Followed

Dataset Import & Cleaning
Loaded A/B experiment data & checked column distributions.

Segmentation into Variant A & B
Split user groups to compare behavior metrics.

Funnel Metric Calculation

Click Through Rate (CTR)

Add-to-Cart %

Purchase Conversion %

Statistical Significance Testing
Performed T-Test to check if Variant B improvement is real or random.

Visualization & Insight Extraction

Conversion Bar Chart

CTR Comparison

Add-to-Cart Comparison

Purchase Distribution Plot

Final Recommendation
Suggested whether Variant B should be rolled out or not.

📈 Key Results (Sample Outcome)
Metric	Variant A	Variant B	Performance
Click Through Rate (CTR)	8.4%	11.2%	↑ Better
Add-to-Cart Rate	6.3%	9.1%	↑ Better
Purchase Conversion	2.9%	4.5%	↑ +55% lift
p-value	0.021	< 0.05	📌 Statistically Significant
🔥 Conclusion

Variant B resulted in higher conversions & lower bounce → Recommend rollout.
This indicates better UX, improved product visibility & higher revenue potential.

🧪 Skills Demonstrated

✔ Data Insight Generation
✔ A/B Testing & Hypothesis Validation
✔ Conversion Funnel Analytics
✔ Python Data Analysis
✔ Visualization & Reporting
✔ Business Recommendation using Data
