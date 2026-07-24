from loguru import logger
from config import GOOGLE_API_KEY
from tools import get_current_time, weather_tool
from prompt import SYSTEM_PROMPT as system_prompt

from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI


logger.add("app.log", rotation="1 MB", level="INFO")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY
)

tools = [get_current_time, weather_tool]
agent = create_react_agent(model=llm, tools=tools)
