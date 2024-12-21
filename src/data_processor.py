import pandas as pd
import numpy as np
from datetime import datetime

class DataProcessor:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
    
    def clean_data(self):
        # Remove duplicates
        self.df = self.df.drop_duplicates()
        
        # Convert date columns
        self.df['order_date'] = pd.to_datetime(self.df['order_date'])
        
        # Handle missing values
        self.df['quantity'].fillna(self.df['quantity'].mean(), inplace=True)
        self.df['unit_price'].fillna(self.df['unit_price'].median(), inplace=True)
        
        # Calculate total amount
        self.df['total_amount'] = self.df['quantity'] * self.df['unit_price']
        
        # Add time-based features
        self.df['month'] = self.df['order_date'].dt.month
        self.df['year'] = self.df['order_date'].dt.year
        self.df['quarter'] = self.df['order_date'].dt.quarter
        
        return self.df
