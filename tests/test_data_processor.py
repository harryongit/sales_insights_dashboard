import pytest
import pandas as pd
from src.data_processor import DataProcessor

def test_data_cleaning():
    # Create sample test data
    test_data = {
        'order_date': ['2023-01-01', '2023-01-02', '2023-01-01'],
        'customer_id': [1, 2, 1],
        'product_name': ['Product A', 'Product B', 'Product A'],
        'quantity': [2, None, 2],
        'unit_price': [10.0, 20.0, 10.0]
    }
    df = pd.DataFrame(test_data)
    
    # Initialize processor with test data
    processor = DataProcessor(df)
    cleaned_df = processor.clean_data()
    
    # Assert tests
    assert cleaned_df['quantity'].isnull().sum() == 0  # No missing values
    assert len(cleaned_df) == 2  # Duplicates removed
    assert 'total_amount' in cleaned_df.columns  # New column created
    assert isinstance(cleaned_df['order_date'].iloc[0], pd.Timestamp)  # Date converted
