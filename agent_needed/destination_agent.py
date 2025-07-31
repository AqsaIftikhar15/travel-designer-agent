# agents/destination_agent.py
from agents import Agent
from tools.travel_info import get_destinations_by_mood

def create_destination_agent(model):
    return Agent( name="Destination Agent",
        instructions="""
You help users find ideal travel destinations based on their mood or interests.
- Ask the user to select a mood (e.g. romantic, adventurous, relaxing).
- Use the tool `get_destinations_by_mood` to suggest destination options.
- Present the options and wait for user selection.
- When user selects a destination, pass it to the next agent.
""",
        model=model,
        tools=[get_destinations_by_mood],
    )
