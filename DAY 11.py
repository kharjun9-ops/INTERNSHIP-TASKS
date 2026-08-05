insights = [
    "1. Headcount Distribution: Sales (50) and IT (45) represent the largest teams, indicating heavy organizational focus on technical execution and revenue generation.",
    "2. Budget Allocation vs. Staffing: The Sales department holds the highest budget ($200,000) alongside high headcount, whereas HR operates with the leanest resources ($50,000 across 15 employees).",
    "3. Revenue Growth Trend: Across all departments, Q2 revenue outperformed Q1, demonstrating positive operational growth momentum quarter-over-quarter.",
    "4. Salary Disparities: Compensation spans from a minimum of $45,000 in Marketing to a maximum of $85,000 in IT, reflecting technical skill premiums in tech-driven roles.",
    "5. Data Quality Risk: Initial dataset audits revealed null values in Age and Salary alongside duplicate records, highlighting the necessity of systematic data validation pipelines before executive reporting."
]
print("      DAY 11: KEY BUSINESS INSIGHTS SUMMARY       ")

for insight in insights:
    print(f"\n{insight}")