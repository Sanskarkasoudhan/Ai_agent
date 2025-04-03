import os
from dotenv import load_dotenv  # Import dotenv

# Load environment variables from .env file
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Get API keys from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Check if API keys are properly loaded
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")
if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY not found in environment variables")

# Function to get response from AI agent
def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider == "Gemini":
        llm = ChatGoogleGenerativeAI(
            model=llm_id,
            google_api_key=GEMINI_API_KEY  # Explicitly pass the API key
        )
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)  # Assuming OpenAI setup remains unchanged
    else:
        raise ValueError(f"Unsupported provider: {provider}")

    tools = [TavilySearchResults(max_results=2, tavily_api_key=TAVILY_API_KEY)] if allow_search else []

    # Create the agent with the system prompt
    agent = create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=SystemMessage(content=system_prompt)  # Use SystemMessage for system_prompt
    )

    # Properly format the state with a HumanMessage
    state = {"messages": [HumanMessage(content=query)]}
    response = agent.invoke(state)

    # Extract AI messages from the response
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1] if ai_messages else None


