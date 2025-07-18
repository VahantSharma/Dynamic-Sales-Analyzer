"""
Basic Usage Examples for Dynamic Sales Analyzer
==============================================

Simple examples demonstrating the most common use cases.
"""

from dynamic_sales_analyzer import analyze_sales_data, DynamicSalesAnalyzer
import pandas as pd

def example_1_quick_analysis():
    """Example 1: One-line analysis of any file"""
    print("=" * 60)
    print("EXAMPLE 1: Quick Analysis")
    print("=" * 60)
    
    # Create sample data
    sample_data = {
        'Date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05'],
        'Sales_Rep': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve'],
        'Region': ['North', 'South', 'East', 'West', 'North'],
        'Revenue': [1500, 2300, 1800, 2700, 1900],
        'Deals': [3, 5, 4, 6, 4]
    }
    
    # Save to CSV
    df = pd.DataFrame(sample_data)
    df.to_csv('example_sales.csv', index=False)
    
    # One-line analysis
    results = analyze_sales_data('example_sales.csv')
    
    if results['success']:
        print("✅ Analysis completed successfully!")
        
        stats = results['analysis_results']['basic_stats']
        print(f"\n💰 Total Revenue: ${stats['total_revenue']:,.2f}")
        print(f"📈 Total Deals: {stats['total_deals']}")
        print(f"📊 Average Deal Size: ${stats['total_revenue']/stats['total_deals']:,.2f}")
        
        # Show top performers
        if 'regional_analysis' in results['analysis_results']:
            regional = results['analysis_results']['regional_analysis']
            print(f"🌍 Top Region: {regional['top_region']} (${regional['top_region_revenue']:,.2f})")
        
        if 'sales_rep_analysis' in results['analysis_results']:
            rep = results['analysis_results']['sales_rep_analysis']
            print(f"👤 Top Sales Rep: {rep['top_rep']} (${rep['top_rep_revenue']:,.2f})")
    
    else:
        print(f"❌ Analysis failed: {results['error']}")
    
    # Cleanup
    import os
    if os.path.exists('example_sales.csv'):
        os.remove('example_sales.csv')


def example_2_alternative_columns():
    """Example 2: Handling different column names"""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Alternative Column Names")
    print("=" * 60)
    
    # Data with different column naming conventions
    alt_data = {
        'Transaction_Date': ['2025-01-06', '2025-01-07', '2025-01-08'],
        'Salesperson': ['Frank', 'Grace', 'Henry'],
        'Territory': ['North', 'South', 'East'],
        'Total_Sales': [2100, 1800, 2400],
        'Orders': [5, 4, 6]
    }
    
    df = pd.DataFrame(alt_data)
    df.to_csv('alternative_columns.csv', index=False)
    
    print("📊 Original column names:", list(df.columns))
    
    results = analyze_sales_data('alternative_columns.csv')
    
    if results['success']:
        print("✅ Intelligent column mapping successful!")
        
        mappings = results['column_mappings']
        print("\n🗺️  Column Mappings:")
        for schema_name, actual_name in mappings.items():
            print(f"  {schema_name} → '{actual_name}'")
        
        stats = results['analysis_results']['basic_stats']
        print(f"\n💰 Total Revenue: ${stats['total_revenue']:,.2f}")
    
    # Cleanup
    import os
    if os.path.exists('alternative_columns.csv'):
        os.remove('alternative_columns.csv')


def example_3_messy_data():
    """Example 3: Automatic data cleaning"""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Automatic Data Cleaning")
    print("=" * 60)
    
    # Messy data with issues
    messy_data = {
        'Date': ['2025-01-01', '2025-01-02', '2025-01-01', '2025-01-03', '2025-01-04'],  
        'Sales_Rep': ['Kate', 'Liam', 'Kate', 'Mia', 'Nick'],                   
        'Region': ['South', 'East', 'South', 'West', 'North'],                     
        'Revenue': [2300, 1700, 2300, -150, 2100],  # Negative value + duplicate
        'Deals': [6, 4, 6, 3, 5]                   
    }
    
    df = pd.DataFrame(messy_data)
    df.to_csv('messy_data.csv', index=False)
    
    print(f"📊 Original data: {len(df)} rows")
    print("⚠️  Issues: Duplicates, negative revenue")
    
    results = analyze_sales_data('messy_data.csv')
    
    if results['success']:
        print("✅ Data cleaning completed!")
        
        original_rows = results['raw_data_shape'][0]
        cleaned_rows = results['cleaned_data_shape'][0]
        
        print(f"\n🧹 Cleaning Results:")
        print(f"  Original: {original_rows} rows")
        print(f"  Cleaned: {cleaned_rows} rows")
        print(f"  Removed: {original_rows - cleaned_rows} rows")
        
        stats = results['analysis_results']['basic_stats']
        print(f"\n💰 Final Revenue: ${stats['total_revenue']:,.2f}")
    
    # Cleanup
    import os
    if os.path.exists('messy_data.csv'):
        os.remove('messy_data.csv')


def example_4_minimal_data():
    """Example 4: Minimal required data"""
    print("\n" + "=" * 60)
    print("EXAMPLE 4: Minimal Required Data")
    print("=" * 60)
    
    # Only required columns
    minimal_data = {
        'Date': ['2025-01-01', '2025-01-02', '2025-01-03'],
        'Revenue': [1000, 1500, 1200]
    }
    
    df = pd.DataFrame(minimal_data)
    df.to_csv('minimal_data.csv', index=False)
    
    print("📊 Data contains only: Date, Revenue")
    
    results = analyze_sales_data('minimal_data.csv')
    
    if results['success']:
        print("✅ Analysis adapted to available data!")
        
        available_analyses = list(results['analysis_results'].keys())
        print(f"\n📈 Available analyses: {', '.join(available_analyses)}")
        
        stats = results['analysis_results']['basic_stats']
        print(f"💰 Total Revenue: ${stats['total_revenue']:,.2f}")
        
        if 'trend_analysis' in results['analysis_results']:
            trend = results['analysis_results']['trend_analysis']
            print(f"📅 Peak Day: {trend['peak_day']} (${trend['peak_revenue']:,.2f})")
    
    # Cleanup
    import os
    if os.path.exists('minimal_data.csv'):
        os.remove('minimal_data.csv')


def example_5_comprehensive_analysis():
    """Example 5: Full feature demonstration"""
    print("\n" + "=" * 60)
    print("EXAMPLE 5: Comprehensive Analysis")
    print("=" * 60)
    
    # Rich dataset with all possible columns
    comprehensive_data = {
        'Date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05',
                 '2025-01-06', '2025-01-07', '2025-01-08', '2025-01-09', '2025-01-10'],
        'Sales_Rep': ['Alice', 'Bob', 'Carol', 'Alice', 'Bob', 
                      'Carol', 'Dave', 'Eve', 'Alice', 'Bob'],
        'Region': ['North', 'South', 'East', 'West', 'North',
                   'South', 'East', 'West', 'North', 'South'],
        'Revenue': [1500, 2300, 1800, 2700, 1900,
                    2100, 1600, 2400, 1700, 2200],
        'Deals': [3, 5, 4, 6, 4, 5, 3, 6, 4, 5],
        'Customer_Type': ['New', 'Returning', 'New', 'Returning', 'New',
                          'Returning', 'New', 'Returning', 'New', 'Returning'],
        'Product': ['Basic', 'Premium', 'Enterprise', 'Premium', 'Basic',
                    'Enterprise', 'Basic', 'Premium', 'Enterprise', 'Premium']
    }
    
    df = pd.DataFrame(comprehensive_data)
    df.to_csv('comprehensive_data.csv', index=False)
    
    print("📊 Rich dataset with all analysis dimensions")
    
    results = analyze_sales_data('comprehensive_data.csv')
    
    if results['success']:
        print("✅ Comprehensive analysis completed!")
        
        # Show all analysis results
        analysis = results['analysis_results']
        
        # Basic stats
        if 'basic_stats' in analysis:
            stats = analysis['basic_stats']
            print(f"\n💰 Revenue: ${stats['total_revenue']:,.2f}")
            print(f"📈 Deals: {stats['total_deals']}")
            print(f"📊 Avg Deal: ${stats['total_revenue']/stats['total_deals']:,.2f}")
        
        # Top performers
        if 'regional_analysis' in analysis:
            regional = analysis['regional_analysis']
            print(f"🌍 Top Region: {regional['top_region']} (${regional['top_region_revenue']:,.2f})")
        
        if 'sales_rep_analysis' in analysis:
            rep = analysis['sales_rep_analysis']
            print(f"👤 Top Rep: {rep['top_rep']} (${rep['top_rep_revenue']:,.2f})")
        
        if 'trend_analysis' in analysis:
            trend = analysis['trend_analysis']
            print(f"📅 Peak Day: {trend['peak_day']} (${trend['peak_revenue']:,.2f})")
        
        # Show executive report
        print(f"\n📋 Executive Report:")
        print("-" * 40)
        print(results['report'])
    
    # Cleanup
    import os
    if os.path.exists('comprehensive_data.csv'):
        os.remove('comprehensive_data.csv')


def main():
    """Run all basic examples"""
    print("🚀 Dynamic Sales Analyzer - Basic Usage Examples")
    print("=" * 80)
    
    example_1_quick_analysis()
    example_2_alternative_columns()
    example_3_messy_data()
    example_4_minimal_data()
    example_5_comprehensive_analysis()
    
    print("\n" + "=" * 80)
    print("🎉 All examples completed successfully!")
    print("✨ The Dynamic Sales Analyzer handles any data format with intelligence!")


if __name__ == "__main__":
    main()
