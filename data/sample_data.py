import pandas as pd
import numpy as np

def generate_sample_data():
    """Generate sample sales data for demonstration."""
    np.random.seed(42)
    
    # Generate 36 months of data (3 years)
    dates = pd.date_range(start='2020-01-01', periods=36, freq='M')
    
    # Create a base trend (upward trend)
    base = np.linspace(100, 300, 36)
    
    # Add seasonality (higher in Q4, lower in Q1)
    seasonal_pattern = np.array([0.1, 0.0, 0.1, 0.2, 0.3, 0.2, 0.1, 0.0, 0.1, 0.2, 0.3, 0.4] * 3)
    
    # Add some noise
    noise = np.random.normal(0, 15, 36)
    
    # Combine components
    sales = base + (seasonal_pattern * 50) + noise
    sales = np.maximum(sales, 50)  # Ensure no negative sales
    
    # Create DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Sales': sales.round(2)
    })
    
    # Save to CSV
    df.to_csv('e:/FUTURE_ML_01/data/sales_data.csv', index=False)
    print("Sample data generated and saved to 'data/sales_data.csv'")
    return df

if __name__ == "__main__":
    df = generate_sample_data()
    print("\nFirst 5 rows of generated data:")
    print(df.head())
