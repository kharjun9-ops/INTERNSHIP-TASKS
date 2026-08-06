import pandas as pd
import matplotlib.pyplot as plt

def load_and_prep_data() -> pd.DataFrame:
    """Creates and returns the primary departmental dataset."""
    raw_data = {
        'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales'],
        'Employees': [15, 45, 30, 22, 50],
        'Budget_USD': [50000, 150000, 120000, 80000, 200000],
        'Q1_Revenue': [12000, 25000, 18000, 15000, 30000],
        'Q2_Revenue': [15000, 28000, 20000, 18000, 35000]
    }
    return pd.DataFrame(raw_data)

def display_summary(df: pd.DataFrame) -> None:
    """Prints formatted high-level KPI summaries to the console."""
    total_employees = df['Employees'].sum()
    total_budget = df['Budget_USD'].sum()
    avg_budget = df['Budget_USD'].mean()

    print("=" * 55)
    print(f"{'EXECUTIVE KPI SUMMARY':^55}")
    print("=" * 55)
    print(f" • Total Headcount       : {total_employees:,} employees")
    print(f" • Total Budget          : ${total_budget:,.2f}")
    print(f" • Mean Department Budget: ${avg_budget:,.2f}")
    print("=" * 55 + "\n")

def generate_dashboard(df: pd.DataFrame) -> None:
    """Generates a 2x2 polished grid dashboard of department metrics."""
    # Custom color palette for consistent visual branding
    primary_color = '#2b5c8f'
    secondary_color = '#27ae60'
    accent_colors = ['#4c72b0', '#55a868', '#c44e52', '#8172b0', '#ccb974']

    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Executive Departmental Performance Dashboard', fontsize=16, fontweight='bold', y=0.98)

    axes[0, 0].bar(df['Department'], df['Employees'], color=primary_color, width=0.55, edgecolor='black', alpha=0.85)
    axes[0, 0].set_title('Headcount Distribution by Department', fontweight='bold', fontsize=11)
    axes[0, 0].set_ylabel('Number of Staff')

    axes[0, 1].pie(
        df['Budget_USD'], 
        labels=df['Department'], 
        autopct='%1.1f%%', 
        colors=accent_colors, 
        startangle=140, 
        wedgeprops={'edgecolor': 'white', 'linewidth': 1.5}
    )
    axes[0, 1].set_title('Budget Allocation Breakdown (%)', fontweight='bold', fontsize=11)

    axes[1, 0].plot(df['Department'], df['Q1_Revenue'], marker='o', linewidth=2, label='Q1 Revenue', color=primary_color)
    axes[1, 0].plot(df['Department'], df['Q2_Revenue'], marker='s', linewidth=2, label='Q2 Revenue', color=secondary_color)
    axes[1, 0].set_title('Quarterly Revenue Growth (Q1 vs Q2)', fontweight='bold', fontsize=11)
    axes[1, 0].set_ylabel('Revenue ($)')
    axes[1, 0].legend(frameon=True)
    axes[1, 0].grid(True, linestyle='--', alpha=0.5)

    axes[1, 1].barh(df['Department'], df['Budget_USD'], color='#e74c3c', height=0.55, alpha=0.85)
    axes[1, 1].set_title('Total Budget Distribution ($)', fontweight='bold', fontsize=11)
    axes[1, 1].set_xlabel('Budget ($)')
    axes[1, 1].grid(axis='x', linestyle='--', alpha=0.5)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

if __name__ == "__main__":
    df = load_and_prep_data()
    display_summary(df)
    generate_dashboard(df)