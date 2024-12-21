import pytest
from src.analysis import SalesAnalyzer
import pandas as pd

def test_sales_summary():
    # Create test data
    test_data = {
        'customer_id': [1, 2, 3],
        'total_amount': [100, 200, 300]
    }
    df = pd.DataFrame(test_data)
    
    analyzer = SalesAnalyzer(df)
    summary = analyzer.get_sales_summary()
    
    assert summary['total_revenue'] == 600
    assert summary['total_orders'] == 3
    assert summary['avg_order_value'] == 200
    assert summary['total_customers'] == 3
