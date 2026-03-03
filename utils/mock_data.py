import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def get_inventory_data():
    items = ['Smart T-Shirt', 'Eco-friendly Jeans', 'Wireless Earbuds', 'Yoga Mat', 'Running Shoes', 'Water Bottle', 'Bluetooth Speaker', 'Fitness Tracker', 'Backpack']
    categories = ['Apparel', 'Apparel', 'Electronics', 'Fitness', 'Footwear', 'Fitness', 'Electronics', 'Electronics', 'Accessories']
    
    np.random.seed(42)
    current_stock = np.random.randint(5, 500, size=len(items))
    reorder_level = np.random.randint(20, 100, size=len(items))
    demand_forecast = np.random.randint(10, 200, size=len(items))
    
    df = pd.DataFrame({
        'Product': items,
        'Category': categories,
        'Current Stock': current_stock,
        'Reorder Level': reorder_level,
        'Demand Forecast (Next 30 Days)': demand_forecast
    })
    
    df['Status'] = np.where(df['Current Stock'] <= df['Reorder Level'], 'Low Stock', 'Healthy')
    return df

def get_sales_data():
    np.random.seed(42)
    dates = pd.date_range(end=datetime.today(), periods=30)
    sales = np.random.randint(1000, 5000, size=len(dates))
    revenue = sales * np.random.uniform(5.5, 15.0, size=len(dates))
    
    df = pd.DataFrame({
        'Date': dates,
        'Daily Units Sold': sales,
        'Revenue ($)': revenue
    })
    return df

def get_customer_inquiries():
    inquiries = [
        {"id": "CS-101", "customer": "Alice Smith", "issue": "Where is my order? It was supposed to arrive yesterday.", "category": "Shipping", "status": "Open", "urgency": "High"},
        {"id": "CS-102", "customer": "Bob Johnson", "issue": "The fitness tracker isn't syncing with my phone.", "category": "Product Support", "status": "Pending", "urgency": "Medium"},
        {"id": "CS-103", "customer": "Carol Williams", "issue": "I need to return these shoes, they are a size too small.", "category": "Returns", "status": "Open", "urgency": "Low"}
    ]
    return pd.DataFrame(inquiries)

def get_ai_response(query):
    import os
    from openai import OpenAI

    try:
        # Fetch current mock data to give context to the LLM
        inventory_df = get_inventory_data()
        sales_df = get_sales_data()
        
        # Send only extremely brief summaries to stay well under token limits
        low_stock = inventory_df[inventory_df['Status'] == 'Low Stock']['Product'].tolist()
        total_sales = sales_df['Daily Units Sold'].sum()
        total_revenue = sales_df['Revenue ($)'].sum()

        prompt = (
            f"You are an AI Retail Copilot.\n"
            f"Business Summary:\n"
            f"- Items critically low on stock: {', '.join(low_stock) if low_stock else 'None'}\n"
            f"- Total 30-day Sales: {total_sales} units\n"
            f"- Total 30-day Revenue: ${total_revenue:,.2f}\n\n"
            f"User Query: {query}\n\n"
            f"Answer briefly (under 50 words) based only on this summary. Do not formulate markdown tables."
        )

        try:
            from dotenv import load_dotenv
            load_dotenv(override=True)
            api_key = os.environ.get("OPENAI_API_KEY")
            base_url = os.environ.get("OPENAI_BASE_URL", "https://bedrock-mantle.eu-north-1.api.aws/v1")
            
            if not api_key:
                return "Configuration Error: OPENAI_API_KEY is missing. Please check your .env file."
                
            client = OpenAI(api_key=api_key, base_url=base_url)

            try:
                # The hackathon environment uses responses API
                response = client.responses.create(
                    model="openai.gpt-oss-120b",
                    input=[
                        {"role": "user", "content": prompt}
                    ]
                )
                return response.output_text.strip()
            except Exception:
                # Fallback to standard chat completions
                response = client.chat.completions.create(
                    model="openai.gpt-oss-120b",
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=100,
                    temperature=0.5
                )
                return response.choices[0].message.content.strip()
        except Exception as e:
            return f"AI Proxy API Error: {str(e)}"
    except Exception as e:
        return f"Sorry, I encountered an error connecting to the AI: {str(e)}"
