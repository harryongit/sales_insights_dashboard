import matplotlib.pyplot as plt
import seaborn as sns

class SalesVisualizer:
    def __init__(self, df):
        self.df = df
        plt.style.use('seaborn')
    
    def plot_monthly_sales(self):
        monthly_sales = (self.df.groupby(['year', 'month'])
                        ['total_amount'].sum()
                        .reset_index())
        
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=monthly_sales, 
                    x='month', 
                    y='total_amount', 
                    hue='year')
        plt.title('Monthly Sales Trend')
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        return plt
    
    def plot_product_performance(self, top_n=10):
        product_sales = (self.df.groupby('product_name')
                        ['total_amount'].sum()
                        .sort_values(ascending=True)
                        .tail(top_n))
        
        plt.figure(figsize=(10, 6))
        product_sales.plot(kind='barh')
        plt.title(f'Top {top_n} Products by Sales')
        plt.xlabel('Total Sales')
        return plt
    
    def plot_customer_segments(self):
        customer_segments = (self.df.groupby('customer_id')
                           ['total_amount'].sum()
                           .reset_index())
        
        plt.figure(figsize=(8, 6))
        sns.histplot(data=customer_segments, 
                    x='total_amount', 
                    bins=30)
        plt.title('Customer Value Distribution')
        plt.xlabel('Total Purchase Amount')
        return plt
