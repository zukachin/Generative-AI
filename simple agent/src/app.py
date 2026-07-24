from loguru import logger
from graph import agent
from prompt import SYSTEM_PROMPT

logger.info("Starting the application...")

while True:
    question = input("Ask a question (or type 'exit' to quit): ")
    if question.lower() == 'exit':
        break
    response = agent.invoke(
        {"messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ]}
    )

    answer = response['messages'][-1].content
 
    logger.info(f"User question: {question}")
    logger.info(f"Agent response: {answer}")