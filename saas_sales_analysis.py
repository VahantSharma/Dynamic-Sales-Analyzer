"""
Professional SaaS Sales Data Analysis Project
============================================

This script performs a comprehensive analysis of SaaS sales data for January 2025.
It includes data cleaning, pivot table analysis, visualizations, and business insights.

Author: Senior Data Analyst
Date: July 2025
"""

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np

# Set professional styling for visualizations
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

print("=" * 60)
print("SaaS Sales Data Analysis - January 2025")
print("=" * 60)
print()

# ============================================================================
# STEP 1: DATA SIMULATION AND SETUP
# ============================================================================

print("Step 1: Creating representative SaaS sales dataset...")
print()

# Create the dataset based on the provided sample with known data points
# This simulates the raw data that would typically be loaded from a CSV file
raw_data = {
    'Unnamed: 0': list(range(32)),  # Extraneous index column to be removed
    'Date': [
        '2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05',
        '2025-01-06', '2025-01-07', '2025-01-08', '2025-01-09', '2025-01-10',
        '2025-01-11', '2025-01-12', '2025-01-13', '2025-01-14', '2025-01-15',
        '2025-01-16', '2025-01-17', '2025-01-18', '2025-01-19', '2025-01-20',
        '2025-01-21', '2025-01-22', '2025-01-23', '2025-01-24', '2025-01-25',
        '2025-01-26', '2025-01-27', '2025-01-28', '2025-01-29', '2025-01-30',
        '2025-01-03', '2025-01-31'  # Row 30 (index 30) is duplicate of row 2
    ],
    'Sales Rep': [
        'Sarah', 'Mike', 'Anil', 'Lisa', 'Raj',
        'Priya', 'Sarah', 'Mike', 'Anil', 'Lisa',
        'Raj', 'Priya', 'Sarah', 'Mike', 'Anil',
        'Lisa', 'Raj', 'Priya', 'Sarah', 'Mike',
        'Anil', 'Lisa', 'Raj', 'Priya', 'Sarah',
        'Mike', 'Anil', 'Lisa', 'Raj', 'Priya',
        'Anil', 'Sarah'  # Row 30 is duplicate
    ],
    'Region': [
        'North', 'West', 'South', 'East', 'North',
        'South', 'West', 'East', 'South', 'North',
        'West', 'East', 'North', 'West', 'South',
        'East', 'North', 'South', 'West', 'East',
        'South', 'North', 'West', 'East', 'North',
        'West', 'South', 'East', 'North', 'South',
        'South', 'West'  # Row 30 is duplicate
    ],
    'Deals Closed': [
        5, 7, 8, 6, 9,
        4, 3, 8, 7, 5,
        6, 4, 8, 9, 6,
        7, 5, 3, 8, 6,
        9, 4, 7, 5, 6,
        8, 7, 4, 9, 3,
        8, 5  # Row 30 is duplicate
    ],
    'Revenue': [
        2150, 3200, 3027, 2800, 4100,
        -100, 1500, 3600, 2900, 2250,  # Row 5 has negative revenue (data error)
        2700, 1800, 3500, 4200, 2600,
        3100, 2400, 1350, 3800, 2750,
        4300, 1900, 3000, 2100, 2650,
        3400, 3027, 2000, 4500, 1450,  # Row 26 duplicates row 2's revenue
        3027, 2300  # Row 30 is exact duplicate
    ],
    'Customer Type': [
        'New', 'Returning', 'Returning', 'New', 'Returning',
        'New', 'New', 'Returning', 'New', 'Returning',
        'New', 'Returning', 'New', 'Returning', 'New',
        'Returning', 'New', 'New', 'Returning', 'New',
        'Returning', 'New', 'Returning', 'New', 'Returning',
        'New', 'Returning', 'New', 'Returning', 'New',
        'Returning', 'New'  # Row 30 is duplicate
    ],
    'Product': [
        'Premium', 'Enterprise', 'Basic', 'Premium', 'Enterprise',
        'Basic', 'Basic', 'Enterprise', 'Premium', 'Basic',
        'Premium', 'Basic', 'Enterprise', 'Enterprise', 'Premium',
        'Enterprise', 'Basic', 'Basic', 'Enterprise', 'Premium',
        'Enterprise', 'Basic', 'Premium', 'Basic', 'Premium',
        'Enterprise', 'Basic', 'Basic', 'Enterprise', 'Basic',
        'Basic', 'Premium'  # Row 30 is duplicate
    ]
}

# Create the DataFrame (simulating loaded CSV data)
df = pd.DataFrame(raw_data)

print(f"Original dataset created with {len(df)} rows and {len(df.columns)} columns")
print("Dataset includes known issues: extraneous index column, duplicates, and negative revenue")
print()

# ============================================================================
# STEP 2: DATA CLEANING AND PREPARATION
# ============================================================================

print("Step 2: Data Cleaning and Preparation")
print("-" * 40)

# 2.1 Remove the extraneous 'Unnamed: 0' column
print("2.1 Removing extraneous 'Unnamed: 0' column...")
df_cleaned = df.drop('Unnamed: 0', axis=1)
print(f"    ✓ Removed extraneous index column")

# 2.2 Correct data types
print("2.2 Correcting data types...")
df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'])
df_cleaned['Revenue'] = pd.to_numeric(df_cleaned['Revenue'])
df_cleaned['Deals Closed'] = pd.to_numeric(df_cleaned['Deals Closed'])
print(f"    ✓ Converted Date to datetime format")
print(f"    ✓ Ensured Revenue and Deals Closed are numeric")

# 2.3 Handle negative revenue (treat as data entry errors)
print("2.3 Removing rows with negative revenue...")
rows_before = len(df_cleaned)
df_cleaned = df_cleaned[df_cleaned['Revenue'] >= 0]
negative_revenue_removed = rows_before - len(df_cleaned)
print(f"    ✓ Removed {negative_revenue_removed} row(s) with negative revenue")
print(f"    → Rationale: Negative revenue values are treated as data entry errors")

# 2.4 Remove complete duplicate rows
print("2.4 Removing duplicate rows...")
rows_before_dedup = len(df_cleaned)
df_cleaned = df_cleaned.drop_duplicates()
duplicates_removed = rows_before_dedup - len(df_cleaned)
print(f"    ✓ Removed {duplicates_removed} complete duplicate row(s)")
print(f"    → Rationale: Duplicate records skew analysis and indicate data quality issues")

print()
print("Data Cleaning Summary:")
print(f"  • Original rows: {len(df)}")
print(f"  • Rows with negative revenue removed: {negative_revenue_removed}")
print(f"  • Duplicate rows removed: {duplicates_removed}")
print(f"  • Final clean dataset: {len(df_cleaned)} rows")
print()

# 2.5 Final validation - show cleaned dataset info
print("2.5 Final Dataset Validation:")
print("=" * 30)
df_cleaned.info()
print()

# ============================================================================
# STEP 3: SUMMARY PIVOT TABLE
# ============================================================================

print("Step 3: Sales Performance Summary (Pivot Table)")
print("-" * 50)

# Create pivot table with Region and Sales Rep as multi-level index
sales_summary = df_cleaned.pivot_table(
    index=['Region', 'Sales Rep'], 
    values=['Revenue', 'Deals Closed'], 
    aggfunc='sum'
).round(0)

# Reorder columns for better readability
sales_summary = sales_summary[['Deals Closed', 'Revenue']]

print("SALES PERFORMANCE SUMMARY BY REGION AND SALES REP")
print("=" * 55)
print(sales_summary)
print()

# ============================================================================
# STEP 4: EXECUTIVE DASHBOARD WITH VISUALIZATIONS
# ============================================================================

print("Step 4: Creating Executive Dashboard...")
print()

# Set up the dashboard with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('SaaS Sales Executive Dashboard - January 2025', fontsize=16, fontweight='bold')

# Chart 1: Daily Sales Revenue Trend (Left subplot)
daily_revenue = df_cleaned.groupby('Date')['Revenue'].sum()
ax1.plot(daily_revenue.index, daily_revenue.values, linewidth=2.5, marker='o', markersize=4)
ax1.set_title('Daily Sales Revenue Trend - Jan 2025', fontsize=14, fontweight='bold')
ax1.set_ylabel('Total Revenue ($)', fontsize=12)
ax1.set_xlabel('Date', fontsize=12)
ax1.grid(True, alpha=0.3)

# Format y-axis to show currency
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))

# Rotate x-axis labels for better readability
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')

# Chart 2: Regional Performance (Right subplot)
regional_revenue = df_cleaned.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
bars = ax2.bar(regional_revenue.index, regional_revenue.values, 
               color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
ax2.set_title('Total Revenue by Region', fontsize=14, fontweight='bold')
ax2.set_ylabel('Total Revenue ($)', fontsize=12)
ax2.set_xlabel('Region', fontsize=12)

# Format y-axis to show currency
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + height*0.01, 
             f'${height:,.0f}', ha='center', va='bottom', fontweight='bold')

# Adjust layout and save/display
plt.tight_layout()

# Save the dashboard as an image file
plt.savefig('saas_sales_dashboard.png', dpi=300, bbox_inches='tight')
print("Dashboard saved as 'saas_sales_dashboard.png'")

# Display the dashboard (comment out if running in non-interactive environment)
try:
    plt.show()
    print("Dashboard displayed successfully!")
except:
    print("Dashboard saved to file (display not available in current environment)")
    
print()

# ============================================================================
# STEP 5: BUSINESS INSIGHTS AND FINAL SUMMARY
# ============================================================================

print("Step 5: Business Insights and Recommendations")
print("=" * 50)

# Calculate key metrics for insights
total_revenue = df_cleaned['Revenue'].sum()
total_deals = df_cleaned['Deals Closed'].sum()
avg_deal_size = total_revenue / total_deals

# Top performers
top_region = regional_revenue.index[0]
top_region_revenue = regional_revenue.iloc[0]

rep_performance = df_cleaned.groupby('Sales Rep')['Revenue'].sum().sort_values(ascending=False)
top_rep = rep_performance.index[0]
top_rep_revenue = rep_performance.iloc[0]

# Sales trend analysis
daily_revenue_sorted = daily_revenue.sort_values(ascending=False)
best_day = daily_revenue_sorted.index[0]
best_day_revenue = daily_revenue_sorted.iloc[0]

# Print comprehensive business summary
summary = f"""
EXECUTIVE SUMMARY - JANUARY 2025 SAAS SALES PERFORMANCE
======================================================

DATA QUALITY & CLEANING ACTIONS:
• Successfully cleaned dataset by removing {negative_revenue_removed} record(s) with erroneous negative revenue
• Eliminated {duplicates_removed} duplicate entries to ensure data integrity
• Final analysis based on {len(df_cleaned)} validated sales records

KEY PERFORMANCE INDICATORS:
• Total Revenue: ${total_revenue:,.0f}
• Total Deals Closed: {total_deals:,.0f}
• Average Deal Size: ${avg_deal_size:,.0f}

TOP PERFORMERS:
• Leading Region: {top_region} (${top_region_revenue:,.0f} revenue)
• Top Sales Representative: {top_rep} (${top_rep_revenue:,.0f} revenue)

REGIONAL PERFORMANCE RANKING:
"""

for i, (region, revenue) in enumerate(regional_revenue.items(), 1):
    summary += f"  {i}. {region}: ${revenue:,.0f}\n"

summary += f"""
SALES TREND INSIGHTS:
• Peak Sales Day: {best_day.strftime('%B %d, %Y')} (${best_day_revenue:,.0f})
• Sales Pattern: {"Consistent performance" if daily_revenue.std() < daily_revenue.mean() * 0.3 else "Variable daily performance"}
• Revenue Distribution: {len(regional_revenue)} regions contributing to total sales

RECOMMENDATIONS FOR MANAGEMENT:
1. REPLICATE SUCCESS: Analyze {top_region} region's strategies for implementation in other regions
2. SALES COACHING: Provide additional support to underperforming regions and reps
3. DATA QUALITY: Implement validation rules to prevent negative revenue entries and duplicate records
4. TREND MONITORING: Investigate factors contributing to daily sales variations for better forecasting

AREAS FOR FURTHER INVESTIGATION:
• Customer type analysis to understand new vs. returning customer revenue patterns
• Product line performance analysis to identify most profitable offerings
• Sales rep efficiency metrics (revenue per deal) to optimize resource allocation
• Regional market penetration opportunities in lower-performing areas

This analysis provides a solid foundation for strategic sales decisions and performance optimization.
"""

print(summary)

print("=" * 60)
print("Analysis Complete - Ready for Management Review")
print("=" * 60)
