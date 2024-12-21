# sales_insights_dashboard

## Overview
This project analyzes sales data to derive actionable business insights using Python. It demonstrates skills in data cleaning, exploratory data analysis, visualization, and business intelligence.

## Key Features
- Automated data cleaning and preprocessing
- Sales trend analysis and forecasting
- Customer segmentation
- Product performance analysis
- Interactive visualizations
- Reusable analysis pipeline

## Technical Skills Demonstrated
- Python programming (Pandas, NumPy)
- Data visualization (Matplotlib, Seaborn)
- Data cleaning and preprocessing
- Statistical analysis
- Object-oriented programming
- Version control (Git)

## Project Structure
```
sales_insights/
├── data/               # Data files
├── notebooks/          # Jupyter notebooks for analysis
├── src/               # Source code
├── reports/           # Generated reports and visualizations
└── requirements.txt   # Project dependencies
```

## Installation
```bash
git clone https://github.com/harryongit/sales_insights_dashboard.git
cd sales-insights
pip install -r requirements.txt
```

## Usage
1. Place your sales data in `data/raw/sales_data.csv`
2. Run the analysis:
```bash
python main.py
```
3. View generated reports in the `reports/` directory

## Data Requirements
The input CSV should contain these columns:
- order_date: Date of sale
- customer_id: Unique customer identifier
- product_name: Name of product
- quantity: Number of units sold
- unit_price: Price per unit

## Key Insights Generated
1. Sales Trends
   - Monthly/quarterly sales analysis
   - Year-over-year growth
   
2. Customer Analysis
   - Customer segmentation
   - Customer lifetime value
   
3. Product Performance
   - Top/bottom performing products
   - Product category analysis

## Future Improvements
- Add predictive analytics
- Implement interactive dashboard
- Add more advanced visualizations
- Include seasonal analysis

## Contributing
Pull requests are welcome. For major changes, please open an issue first.

## License
MIT
