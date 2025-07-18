# 🚀 Dynamic Sales Data Analyzer

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)](https://github.com)

A robust, production-ready platform that can analyze sales data from **any format** with **intelligent automation**. Transform raw data from various sources into actionable business insights with zero manual configuration.

![Sales Dashboard](saas_sales_dashboard.png)

## ✨ Features

### 🔧 **Multi-Format Data Ingestion**

- **CSV**: Auto-detects delimiters, encodings, and quote characters
- **Excel**: Handles multiple sheets, merged cells, various Excel versions (.xlsx, .xls)
- **PDF**: Extracts tables from PDF documents automatically
- **JSON**: Processes structured JSON data seamlessly
- **Future Support**: Database connections, API integrations, cloud storage

### 🧠 **Intelligent Column Detection**

- **Fuzzy Matching**: Recognizes column variations ("Revenue" = "Sales Amount" = "Total Income")
- **Content Analysis**: Automatically detects data types (dates, currency, categories)
- **Smart Mapping**: Maps any column structure to standard analysis schema
- **Configurable**: Custom column mappings via YAML configuration

### 🧹 **Automatic Data Cleaning**

- **Quality Issues**: Removes duplicates, handles missing values, fixes data types
- **Outlier Detection**: Multiple algorithms (IQR, Z-score, Isolation Forest)
- **Error Handling**: Graceful handling of negative values, malformed dates
- **Validation**: Comprehensive data quality reporting and logging

### 📊 **Dynamic Analysis Engine**

- **Adaptive**: Analysis adjusts to available columns automatically
- **Comprehensive**: Revenue trends, regional performance, sales rep rankings
- **Business Intelligence**: Executive summaries with actionable insights
- **Scalable**: Handles datasets from small samples to enterprise-scale

## 🚦 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/dynamic-sales-analyzer.git
cd dynamic-sales-analyzer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```python
from dynamic_sales_analyzer import analyze_sales_data

# One-line analysis of ANY format
results = analyze_sales_data('sales_data.csv')

if results['success']:
    print(f"Total Revenue: ${results['analysis_results']['basic_stats']['total_revenue']:,.2f}")
    print(f"Top Region: {results['analysis_results']['regional_analysis']['top_region']}")
    print("\nExecutive Report:")
    print(results['report'])
else:
    print(f"Analysis failed: {results['error']}")
```

### Advanced Usage

```python
from dynamic_sales_analyzer import DynamicSalesAnalyzer

# Create analyzer with custom configuration
analyzer = DynamicSalesAnalyzer('analysis_config.yaml')

# Analyze with specific parameters
results = analyzer.analyze_file(
    'quarterly_report.xlsx',
    sheet_name='Q1_Sales',
    header=2  # Data starts at row 3
)

# Access detailed results
if results['success']:
    # Get column mappings
    mappings = results['column_mappings']

    # Get analysis results
    analysis = results['analysis_results']

    # Get cleaned data
    cleaned_data = analyzer.cleaned_data

    # Export results
    cleaned_data.to_csv('cleaned_sales_data.csv', index=False)
```

## 📊 Analysis Capabilities

### Automatic Analysis Types

The analyzer automatically performs different types of analysis based on detected columns:

| Analysis Type            | Required Columns    | Output                                              |
| ------------------------ | ------------------- | --------------------------------------------------- |
| **Basic Statistics**     | Revenue             | Total revenue, average deal size, transaction count |
| **Trend Analysis**       | Date + Revenue      | Daily/weekly trends, peak performance periods       |
| **Regional Performance** | Region + Revenue    | Top performing regions, geographic insights         |
| **Sales Rep Analysis**   | Sales Rep + Revenue | Individual performance rankings, quotas             |
| **Product Analysis**     | Product + Revenue   | Product line performance, category insights         |

### Sample Output

```
DYNAMIC SALES ANALYSIS REPORT
========================================

DATA SUMMARY:
• Original dataset: 1,247 rows, 8 columns
• Cleaned dataset: 1,201 rows, 6 columns
• Detected columns: date_column, revenue_column, region_column, sales_rep_column

KEY PERFORMANCE METRICS:
• Total Revenue: $2,847,392.50
• Total Transactions: 1,201
• Average Deal Size: $2,371.18

TOP PERFORMING REGION: West ($847,293.20)
TOP PERFORMING REP: Sarah Johnson ($156,847.30)
```

## 🗂️ Project Structure

```
dynamic-sales-analyzer/
├── README.md                    # This comprehensive guide
├── LICENSE                      # MIT License
├── requirements.txt             # Python dependencies
├── analysis_config.yaml         # Configuration templates
├── dynamic_sales_analyzer.py    # Main analysis engine
├── saas_sales_analysis.py       # Original static implementation
├── test_analyzer.py             # Test suite
├── examples/                    # Usage examples
│   ├── basic_usage.py
│   ├── advanced_configuration.py
│   └── sample_data/
└── docs/                        # Additional documentation
    ├── API_REFERENCE.md
    ├── CONFIGURATION_GUIDE.md
    └── CHANGELOG.md
```

## ⚙️ Configuration

The analyzer uses YAML configuration files for maximum flexibility:

```yaml
# analysis_config.yaml
analysis_templates:
  sales_analysis:
    required_columns:
      date_column:
        possible_names: ["date", "transaction_date", "sale_date"]
        data_type: "datetime"
        required: true
      revenue_column:
        possible_names: ["revenue", "sales", "amount", "total"]
        data_type: "numeric"
        required: true

    cleaning_rules:
      remove_negative_revenue: true
      remove_duplicates: true
      outlier_detection: "iqr"
      handle_missing_values: "interpolate"
```

## 🧪 Testing

```bash
# Run comprehensive tests
python test_analyzer.py

# Test with sample data
python -m dynamic_sales_analyzer
```

## 📈 Use Cases

### 🏢 **Enterprise Sales Analytics**

- Quarterly performance reviews
- Regional sales comparison
- Sales rep performance tracking
- Product line analysis

### 📊 **Data Migration & Cleanup**

- Legacy system data migration
- Data quality assessment
- Format standardization
- Automated data preprocessing

### 🔄 **Automated Reporting**

- Daily sales dashboards
- Executive summary generation
- Performance alert systems
- Multi-source data consolidation

## 🛠️ Technical Details

### Architecture

The system follows a modular, class-based architecture:

- **DataIngestionEngine**: Multi-format data loading with intelligent parameter detection
- **SchemaMapper**: Fuzzy column matching and automatic schema detection
- **DataCleaningPipeline**: Configurable cleaning rules and quality validation
- **DynamicSalesAnalyzer**: Main orchestration class with comprehensive analysis

### Dependencies

**Core Requirements:**

- `pandas>=1.5.0` - Data manipulation and analysis
- `numpy>=1.20.0` - Numerical computing
- `PyYAML>=6.0` - Configuration file parsing

**Optional Features:**

- `openpyxl>=3.0.0` - Excel file support
- `tabula-py>=2.5.0` - PDF table extraction
- `fuzzywuzzy>=0.18.0` - Intelligent column matching
- `matplotlib>=3.5.0` - Visualization generation
- `seaborn>=0.11.0` - Statistical visualizations

### Performance

- **Memory Efficient**: Streams large files, configurable memory limits
- **Fast Processing**: Optimized pandas operations, optional parallel computing
- **Scalable**: Tested with datasets up to 10M+ rows
- **Robust**: Comprehensive error handling and graceful degradation

### Development Setup

```bash
# Clone and setup development environment
git clone https://github.com/yourusername/dynamic-sales-analyzer.git
cd dynamic-sales-analyzer

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Format code
black dynamic_sales_analyzer.py
flake8 dynamic_sales_analyzer.py
```

## 🎯 Roadmap

### Current Version (v1.0)

- ✅ Multi-format data ingestion
- ✅ Intelligent column detection
- ✅ Configurable data cleaning
- ✅ Dynamic analysis adaptation
- ✅ Executive reporting

### Planned Features (v2.0)

- 🔄 Real-time data streaming
- 🔄 Machine learning predictions
- 🔄 Interactive web dashboard
- 🔄 API service deployment
- 🔄 Cloud platform integration

---

**⭐ Star this repository if you find it useful!**

**🍴 Fork it to customize for your specific needs!**

**📢 Share it with your team and colleagues!**
