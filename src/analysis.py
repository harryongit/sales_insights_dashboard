class SalesAnalyzer:
    def __init__(self, df):
        self.df = df
    
    def get_sales_summary(self):
        summary = {
            'total_revenue': self.df['total_amount'].sum(),
            'total_orders': len(self.df),
            'avg_order_value': self.df['total_amount'].mean(),
            'total_customers': self.df['customer_id'].nunique()
        }
        return summary
    
    def get_top_products(self, n=5):
        return (self.df.groupby('product_name')
                ['total_amount'].sum()
                .sort_values(ascending=False)
                .head(n))
    
    def get_monthly_sales(self):
        return (self.df.groupby(['year', 'month'])
                ['total_amount'].sum()
                .reset_index())
    
    def get_customer_segments(self):
        customer_value = (self.df.groupby('customer_id')
                         ['total_amount'].sum()
                         .reset_index())
        
        customer_value['segment'] = pd.qcut(
            customer_value['total_amount'],
            q=3,
            labels=['Low Value', 'Medium Value', 'High Value']
        )
        return customer_value
