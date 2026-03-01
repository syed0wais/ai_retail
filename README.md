# AI Retail Copilot 🛍️

Welcome to the **AI Retail Copilot**! This platform leverages predictive analytics and Generative AI concepts to help retail and Small-to-Medium Business (SMB) owners run their businesses more efficiently.

This project was built for the **AI for Bharat Hackathon**, explicitly meeting the "Using Generative AI on AWS" evaluation criteria by integrating **Amazon Bedrock**.

## 🌟 Features

*   📈 **Dashboard**: High-level overview of business KPIs (Sales, Revenue, Orders).
*   📦 **Inventory Management**: Real-time stock monitoring, reorder alerts, and demand forecasting based on historical usage.
*   💬 **Customer Service**: AI-assisted responses and complaint handling overview.
*   📊 **Sales Analytics**: Deep dive into daily revenue margins and product category performance using interactive Plotly charts.
*   🚚 **Order Processing**: Centralized management of fulfillments and validations.
*   🤖 **AI Copilot Chat**: A natural language interface powered by **Amazon Bedrock (Anthropic Claude v2)** that translates raw, multi-channel business data into plain-language actionable intelligence.
*   ☁️ **AWS Architecture**: A dedicated documentation tab explaining the framework and infrastructure rationale used for the Generative AI integrations.

## 🛠️ Technology Stack

*   **Frontend & Framework**: [Streamlit](https://streamlit.io/)
*   **Data Processing**: Pandas, Numpy
*   **Data Visualization**: Plotly
*   **Generative AI**: Amazon Bedrock via `boto3` (AWS SDK for Python)
*   **Environment Management**: `python-dotenv`

## ⚙️ How It Works

1.  **Data Ingestion**: The application currently relies on dynamic mock data generators for inventory, sales, and customer inquiries, serving as a placeholder for a future state DynamoDB/RDS backend.
2.  **Context Assembly**: When a user asks a question in the AI Copilot Chat, the backend pulls the latest real-time stock and sales figures.
3.  **Generative AI Inference**: The data summaries and the user's natural language query are securely bundled into a prompt and sent to **Amazon Bedrock** (using the `anthropic.claude-v2` foundation model) via `boto3`.
4.  **Intelligent Response**: Bedrock processes the context and query, returning concise, insightful business recommendations directly to the user.

---

## 🚀 Setup & Installation Guide

Follow these detailed steps to run the AI Retail Copilot locally on your machine.

### Prerequisites
*   Python 3.9 or higher
*   Active AWS Account with access to **Amazon Bedrock**.
*   Model access granted in the AWS Console for **Anthropic Claude v2** (`anthropic.claude-v2`).

### 1. Clone the Repository
Clone this repository or download the source code to your local machine.
```bash
git clone <repository-url>
cd ai_retail_copilot
```

### 2. Create a Virtual Environment (Optional but Recommended)
Create and activate an isolated Python environment to prevent dependency conflicts.
```bash
# Create the virtual environment
python3 -m venv myenv

# Activate it (Mac/Linux)
source myenv/bin/activate

# Activate it (Windows)
# myenv\Scripts\activate
```

### 3. Install Dependencies
Install all the required Python packages using the provided `requirements.txt` file.
```bash
pip install -r requirements.txt
```

### 4. Configure AWS Credentials
To allow the AI Copilot Chat to communicate with Amazon Bedrock, you must configure your AWS credentials. The application uses a `.env` file to manage these securely.

1.  In the root directory of the project (next to `app.py`), create a new file named exactly **`.env`**.
2.  Open `.env` in any text editor and paste the following, replacing the placeholders with your actual AWS keys:

```text
AWS_ACCESS_KEY_ID=your_access_key_id_here
AWS_SECRET_ACCESS_KEY=your_secret_access_key_here
AWS_DEFAULT_REGION=us-east-1
```
*(Note: Ensure your region supports Amazon Bedrock, such as `us-east-1` or `us-west-2`)*.

### 5. Run the Application
Start the Streamlit development server.
```bash
streamlit run app.py
```

Streamlit will automatically open the application in your default web browser at **http://localhost:8501**.

---
*Built for the prototype phase of the AI for Bharat Hackathon.* 🚀
