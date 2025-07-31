# agents/booking_agent.py
from agents import Agent
from tools.booking_tools import get_flights, suggest_hotels

def create_booking_agent(model):
    return Agent(
        name="Booking Agent",
        instructions="""
You help the user simulate travel bookings for their selected destination.
- Use `get_flights` to show flight options.
- Use `suggest_hotels` to suggest accommodation.
- Ask the user to choose from the options.
- Once booking simulation is complete, pass control to the next agent.
""",
        model=model,
        tools=[get_flights, suggest_hotels],
    )
