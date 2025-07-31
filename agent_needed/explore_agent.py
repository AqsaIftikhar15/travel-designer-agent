# agents/explore_agent.py
from agents import Agent
from tools.explore_tools import suggest_attractions, suggest_food

def create_explore_agent(model):
    return Agent(name="Explore Agent",
        instructions="""
You help users explore activities and food options in their selected destination.
- Use the tool `get_attractions_and_food` to suggest attractions and local cuisine.
- Provide a fun, helpful list based on the destination.
- Let the user choose or ask for more suggestions if needed.
- End the session on a helpful note.
""",
        model=model,
        tools=[suggest_attractions, suggest_food],
    )
