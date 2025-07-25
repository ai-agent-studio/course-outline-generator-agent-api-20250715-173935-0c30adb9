# Course Outline Generator

This agent generates structured, pedagogically-aligned course outlines 


Generated using Enhanced Agent Studio with advanced memory, FastAPI integration, and production-ready features.

## 🚀 Quick Start

### 1. Setup Environment
```bash
# Install dependencies
pip install -r requirements.txt
pip install -r agents/requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your API keys
```

### 2. Configure API Keys
Edit `.env` file with your credentials:
```bash
# Required API keys
GEMINI_API_KEY=your_gemini_api_key_here
GOOGLE_API_KEY=your_google_api_key_here

# Database (if using SQL tools)
DATABASE_URL=postgresql://user:password@host:port/database
```

## 💬 Usage Options

### Option 1: Interactive Chat (Recommended for testing)
```bash
python chat.py
```

Features:
- ✅ Direct agent interaction
- ✅ Enhanced memory (remembers conversation)
- ✅ Follow-up question support
- ✅ Context debugging

### Option 2: FastAPI Server (Production)
```bash
# Start the API server
python -m uvicorn api.main:app --reload --host 0.0.0.0 --port 8000

# Access API documentation
open http://localhost:8000/docs
```

#### API Endpoints:
- `GET /v1/agents` - List available agents
- `POST /v1/agents/course_outline_generator/runs` - Chat with agent
- `GET /docs` - Swagger API documentation
- `GET /redoc` - Alternative API documentation

### Option 3: API Testing
```bash
python test_agent.py
```

## 🧠 Memory Features

This agent has enhanced conversation memory that follows your YAML configuration:
- **Context Awareness**: Remembers previous queries in the same session
- **Follow-up Support**: Understands references like "those", "that", "same"
- **Format Compliance**: Follows exact output format from your YAML

---

Generated by Enhanced Agent Studio - Ready for production use! 🚀
