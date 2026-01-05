# Sales & Demand Forecasting using Machine Learning

This project demonstrates how to build a simple yet effective sales forecasting model using machine learning. It's designed to help businesses predict future sales based on historical data.

## Project Structure
```
.
├── data/                    # Directory for storing datasets
├── notebooks/               # Jupyter notebooks
│   └── sales_forecasting.ipynb  # Main notebook
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```

## Setup
1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

## Usage
1. Place your sales data in the `data/` directory
2. Open and run `notebooks/sales_forecasting.ipynb`
3. Follow the notebook to train the model and generate forecasts

## Model Details
- **Algorithm**: Linear Regression
- **Features**: Time-based features derived from date
- **Evaluation**: Mean Absolute Error (MAE), R² Score

## Results
The model provides:
- Historical sales trend visualization
- Future sales predictions
- Model performance metrics
