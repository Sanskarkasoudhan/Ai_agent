# AI Agent Chatbot with LangGraph

A production-ready AI Agent Chatbot built with FastAPI, Streamlit, and LangGraph that supports multiple LLM providers and web search capabilities.

## 🌟 Features

- **Multiple LLM Providers**: Support for Google Gemini, Anthropic Claude, Cohere, and Mistral AI
- **Interactive UI**: Clean Streamlit interface for engaging with your AI agents
- **Web Search Capabilities**: Integrated with Tavily for web search functionality
- **Modular Architecture**: Clearly separated frontend, backend, and agent components
- **Production Ready**: Built with FastAPI for robust API endpoints

## 📋 Project Structure

```
├── frontend.py          # Streamlit UI
├── backend.py           # FastAPI server
├── ai_agent.py          # LangGraph agent implementation
├── requirements.txt     # Dependencies
└── README.md            # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- API keys for at least one LLM provider
- Tavily API key (for search functionality)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/Sanskarkasoudhan/Ai_agent.git
cd Ai_agent
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the project root with your API keys:

```
# Required: At least one of these LLM provider keys
GEMINI_API_KEY=your_gemini_api_key
OPEN_API_KEY=your open_api_key
# Optional: For web search capability
TAVILY_API_KEY=your_tavily_api_key
```

### Running the Application

1. **Start the backend server**

```bash
python backend.py
```

2. **In a new terminal, start the Streamlit frontend**

```bash
streamlit run frontend.py
```

3. **Open your browser** at `http://localhost:8501`

## 🔧 Configuration

### LLM Models

The application supports various models from different providers:

- **Gemini**: `gemini-1.5-pro`, `gemini-1.5-flash`
- **OopenAI**: `gpt-4o`

To add or modify supported models, update the model lists in `frontend.py` and the `ALLOWED_MODEL_NAMES` in `backend.py`.

### System Prompts

You can customize your AI agent's behavior by providing a system prompt in the UI. Some examples:

- "Act as a helpful customer service representative for a tech company."
- "You are a creative writing assistant who helps brainstorm story ideas."
- "Behave as a data scientist who explains complex concepts in simple terms."

## 📊 Project Phases

This project follows a 3-phase architecture:

### Phase 1: Create AI Agent
- Setup LLM providers (Gemini, Anthropic, etc.)
- Configure search tool functionality
- Implement agent framework with LangGraph

### Phase 2: Setup Backend
- Pydantic models for request/response validation
- FastAPI endpoints for agent interaction
- Swagger UI documentation

### Phase 3: Setup Frontend
- Streamlit UI with model selection
- System prompt customization
- Search functionality toggle

## 🔍 How It Works

1. User enters a query and configures agent settings in the Streamlit UI
2. Frontend sends the request to the FastAPI backend
3. Backend validates the request and initiates the AI agent
4. LangGraph agent processes the request, potentially using search tools
5. Response is sent back to the frontend and displayed to the user

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain) - The foundation for LLM applications
- [LangGraph](https://github.com/langchain-ai/langgraph) - For creating structured reasoning agents
- [FastAPI](https://fastapi.tiangolo.com/) - For the high-performance backend
- [Streamlit](https://streamlit.io/) - For the interactive frontend
- [Tavily](https://tavily.com/) - For search API integration
