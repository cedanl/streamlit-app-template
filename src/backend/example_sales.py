import json
import os
from datetime import datetime, timedelta
import random

SALES_FILE = "data/sales.json"

def generate_sample_sales():
    """Generate sample sales data if file doesn't exist"""
    categories = ["Electronics", "Clothing", "Books", "Home", "Sports"]
    sales = []
    
    # Generate 6 months of sample data
    start_date = datetime.now() - timedelta(days=180)
    
    for i in range(100):
        date = start_date + timedelta(days=random.randint(0, 180))
        sale = {
            'id': i + 1,
            'date': date.strftime('%Y-%m-%d'),
            'amount': round(random.uniform(50, 1000), 2),
            'category': random.choice(categories),
            'customer': f"Customer_{random.randint(1, 50)}"
        }
        sales.append(sale)
    
    return sales

def get_sales_data():
    """Load or generate sales data"""
    if not os.path.exists(SALES_FILE):
        os.makedirs(os.path.dirname(SALES_FILE), exist_ok=True)
        sales = generate_sample_sales()
        with open(SALES_FILE, 'w') as f:
            json.dump(sales, f, indent=2)
        return sales
    
    with open(SALES_FILE, 'r') as f:
        return json.load(f)

def calculate_sales_metrics(sales_data):
    """Calculate key sales metrics"""
    if not sales_data:
        return {'total': 0, 'average': 0, 'best_month': 'N/A', 'growth': 0}
    
    total = sum(sale['amount'] for sale in sales_data)
    average = total / len(sales_data)
    
    # Find best month
    monthly_totals = {}
    for sale in sales_data:
        month = sale['date'][:7]  # YYYY-MM
        if month not in monthly_totals:
            monthly_totals[month] = 0
        monthly_totals[month] += sale['amount']
    
    best_month = max(monthly_totals, key=monthly_totals.get) if monthly_totals else 'N/A'
    
    # Calculate simple growth (last month vs first month)
    months = sorted(monthly_totals.keys())
    if len(months) >= 2:
        growth = ((monthly_totals[months[-1]] - monthly_totals[months[0]]) / monthly_totals[months[0]]) * 100
    else:
        growth = 0
    
    return {
        'total': total,
        'average': average,
        'best_month': best_month,
        'growth': growth
    }

def get_monthly_sales(sales_data):
    """Get monthly sales data for charting"""
    monthly_data = {}
    for sale in sales_data:
        month = sale['date'][:7]  # YYYY-MM
        if month not in monthly_data:
            monthly_data[month] = 0
        monthly_data[month] += sale['amount']
    
    return monthly_data