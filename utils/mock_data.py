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
    import json
    import boto3
    from botocore.exceptions import NoCredentialsError, PartialCredentialsError

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
            # Initialize the Bedrock client
            bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

            # We'll use Anthropic Claude v2, a common and powerful option in Bedrock
            model_id = 'anthropic.claude-v2'
            
            # Format the prompt specifically for Claude
            claude_prompt = f"\\n\\nHuman: {prompt}\\n\\nAssistant:"
            
            payload = {
                "prompt": claude_prompt,
                "max_tokens_to_sample": 100,
                "temperature": 0.5,
                "top_p": 0.9,
            }

            response = bedrock.invoke_model(
                modelId=model_id,
                body=json.dumps(payload),
                contentType='application/json',
                accept='application/json'
            )

            response_body = json.loads(response.get('body').read())
            return response_body.get('completion', '').strip()

        except (NoCredentialsError, PartialCredentialsError):
            return "AWS Configuration Error: Amazon Bedrock requires valid AWS Credentials. Please set your AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to use the Generative AI features."
        except Exception as e:
             return f"Amazon Bedrock API Error: {str(e)}"

    except Exception as e:
        return f"Sorry, I encountered an error connecting to the AI: {str(e)}"
