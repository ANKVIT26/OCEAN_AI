# 🤖 Autonomous QA Agent

An intelligent, autonomous QA agent that constructs a "testing brain" from project documentation and generates comprehensive test cases and Selenium scripts using AI.

## 🎯 Overview

This system uses RAG (Retrieval-Augmented Generation) with Google Gemini API to:
- **Ingest** project documentation (MD, TXT, JSON, HTML)
- **Generate** comprehensive test cases grounded in documentation
- **Create** executable Selenium Python scripts for automated testing

## ✨ Features

### Core Capabilities
- 📄 **Multi-Format Document Ingestion**: Supports Markdown, Text, JSON, and HTML
- 🧠 **Semantic Search**: ChromaDB vector database for intelligent document retrieval
- 🤖 **AI-Powered Generation**: Uses Google Gemini 2.0 Flash for test case creation
- 🐍 **Selenium Script Generation**: Automated Python script generation with proper selectors
- 🎨 **Clean UI**: Streamlit interface with API key configuration

### Technical Stack
- **Backend**: FastAPI with modular service architecture
- **Frontend**: Streamlit web application
- **AI**: Google Gemini API (Flash 2.0)
- **Vector Store**: ChromaDB with sentence-transformers
- **Deployment**: Docker & Docker Compose support

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Gemini API Key ([Get one free](https://makersuite.google.com/app/apikey))
- Docker & Docker Compose (optional, for containerized deployment)

### Option 1: Docker Deployment (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/ANKVIT26/OCEAN_AI.git
   cd OCEAN_AI
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

3. **Start with Docker Compose**
   ```bash
   docker-compose up -d
   ```

4. **Access the application**
   - Frontend: http://localhost:8501
   - Backend API: http://localhost:8000

### Option 2: Local Development

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Key**
   
   Create a `.env` file:
   ```bash
   GEMINI_API_KEY=your_api_key_here
   ```

3. **Run the Application**

   **Terminal 1 - Start Backend:**
   ```bash
   python -m uvicorn backend.app:app --reload
   ```
   Backend will run at: http://localhost:8000

   **Terminal 2 - Start Frontend:**
   ```bash
   streamlit run frontend/streamlit_app.py
   ```
   Frontend will open at: http://localhost:8501

> **Note**: You need to run both commands in separate terminal windows simultaneously.

## 🎮 Running the Application

### Quick Start Commands

**Backend (Terminal 1):**
```bash
cd OCEAN_AI
python -m uvicorn backend.app:app --reload
```

**Frontend (Terminal 2):**
```bash
cd OCEAN_AI
streamlit run frontend/streamlit_app.py
```

**Access the app**: Open http://localhost:8501 in your browser

## 💻 Usage

### 1. Build Knowledge Base
- Upload support documents from `assets/support_docs/`:
  - `product_specs.md` - Business logic and features
  - `ui_ux_guide.txt` - UI/UX requirements
  - `api_endpoints.json` - API specifications
- Upload target HTML: `assets/checkout.html`
- Click "Build Knowledge Base"

### 2. Generate Test Cases
- Enter requirement (e.g., "Test discount code feature")
- Click "Generate Test Cases"
- View AI-generated test plan in Markdown table format

### 3. Generate Selenium Scripts
- Copy a test case scenario
- Paste into "Test Case Scenario" field
- Click "Generate Script"
- Get executable Python Selenium code

## 📁 Project Structure

```
OCEAN_AI/
├── backend/                    # FastAPI Backend
│   ├── app.py                  # Main FastAPI server
│   ├── config.py               # Configuration
│   ├── models/                 # Pydantic data models
│   │   └── request_models.py
│   └── services/               # Business logic
│       ├── document_processor.py
│       ├── vector_store.py
│       ├── rag_agent.py
│       ├── script_agent.py
│       └── llm_factory.py
├── frontend/                   # Streamlit Frontend
│   └── streamlit_app.py
├── assets/                     # Test Assets
│   ├── checkout.html
│   └── support_docs/
├── data/                       # Persistent Data
│   └── chroma_db/             # Vector database
├── docker-compose.yml          # Multi-container orchestration
├── Dockerfile.backend          # Backend container
├── Dockerfile.frontend         # Frontend container
├── requirements.txt            # Python dependencies
├── .env.example               # Environment template
└── README.md                  # This file
```

## 🔧 Configuration

### Environment Variables
- `GEMINI_API_KEY`: Your Google Gemini API key (required)
- `OPENAI_API_KEY`: OpenAI API key (optional fallback)

### Docker Environment
Set these in your `.env` file before running `docker-compose up`.

## 📝 Support Documents

The project includes sample documents in `assets/support_docs/`:
- **product_specs.md**: Business rules (e.g., "SAVE15" discount code)
- **ui_ux_guide.txt**: Visual requirements (error colors, button styles)
- **api_endpoints.json**: Backend API specifications

## 🐳 Docker Commands

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild containers
docker-compose up -d --build
```

## 🛠️ Development

### Running Tests
```bash
python -m pytest tests/
```

### Code Structure
- **Modular Services**: Separated concerns (document processing, vector store, agents)
- **Type Hints**: Full Pydantic model validation
- **Error Handling**: Comprehensive try-except blocks
- **API Design**: RESTful FastAPI endpoints


## 🙏 Acknowledgments

Built with:
- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [Google Gemini](https://ai.google.dev/)
- [ChromaDB](https://www.trychroma.com/)

