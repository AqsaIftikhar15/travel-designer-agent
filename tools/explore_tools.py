# tools/explore_tools.py
from agents.tool import function_tool

@function_tool
def suggest_attractions(destination: str):
    return [
        f"{destination.title()} Museum",
        f"{destination.title()} City Tour",
        f"{destination.title()} National Park",
        f"{destination.title()} Historic Fort"
    ]
@function_tool
def suggest_food(destination: str):
    return [
        f"Try the famous Street Food in {destination.title()}",
        f"Don't miss {destination.title()}'s Traditional Cuisine",
        f"Top-rated Café in downtown {destination.title()}",
        f"Michelin-star Restaurant in {destination.title()}"
    ]
