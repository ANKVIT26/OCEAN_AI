# Autonomous QA Agent

This project implements an intelligent, autonomous QA agent capable of constructing a "testing brain" from project documentation. It generates test cases and Selenium scripts based on support documents and target HTML.

## Setup Instructions

### Prerequisites
- Python 3.8+
- Ollama (for local LLM inference) or OpenAI API Key
- pip

### Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Key** (Choose one):
   
   **Option A: Google Gemini API (Recommended)**
   - Get your free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Set the environment variable:
     ```bash
     # Windows (PowerShell)
     $env:GEMINI_API_KEY="your_api_key_here"
     
     # Linux/Mac
     export GEMINI_API_KEY="your_api_key_here"
     ```
   
   **Option B: OpenAI API (Alternative)**
   - Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
   - Set the environment variable:
     ```bash
     # Windows (PowerShell)
     $env:OPENAI_API_KEY="your_api_key_here"
     
     # Linux/Mac
     export OPENAI_API_KEY="your_api_key_here"
     ```

### Running the Application

This project uses a Client-Server architecture. You need to run both the Backend and Frontend.

**1. Start the Backend Server:**
   ```bash
   python -m uvicorn backend.app:app --reload
   ```
   The backend will start at `http://localhost:8000`.

**2. Start the Frontend Interface:**
   Open a new terminal and run:
   ```bash
   streamlit run frontend/streamlit_app.py
   ```
   The application will open in your browser at `http://localhost:8501`.

## Usage Guide

1. **Ingestion Phase**:
   - Upload the support documents (located in `assets/support_docs/`) in the sidebar.
   - Upload the target `checkout.html` file (located in `assets/`).
   - Click "Build Knowledge Base".

2. **Test Case Generation**:
   - Go to the "Test Case Generation" tab.
   - Enter a prompt (e.g., "Generate test cases for discount codes").
   - View the generated test cases in a Markdown table.

3. **Script Generation**:
   - Go to the "Selenium Script Generation" tab.
   - Copy a scenario from the generated test cases.
   - Paste it into the "Test Case Scenario" box.
   - Click "Generate Script".
   - Copy the generated Python code.

## Support Documents Description

- **product_specs.md**: Contains business logic and feature specifications, such as discount code rules (e.g., "SAVE15" gives 15% off) and shipping costs.
- **ui_ux_guide.txt**: Defines the visual and user experience requirements, such as error message colors (red) and button styles (green for "Pay Now").
- **api_endpoints.json**: Lists the backend API endpoints that the frontend interacts with, useful for understanding data flow and expected payloads.

## Project Structure

```
Assignment/
├── backend/                # FastAPI Backend
│   ├── app.py              # Main Server
│   ├── models/             # Data Models
│   └── services/           # Business Logic
│       ├── document_processor.py
│       ├── vector_store.py
│       ├── rag_agent.py
│       └── script_agent.py
├── frontend/               # Streamlit Frontend
│   └── streamlit_app.py
├── assets/                 # Test Assets
│   ├── checkout.html
│   └── support_docs/
├── data/                   # Persistent Data (ChromaDB)
└── requirements.txt
```
