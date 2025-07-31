# tools/travel_info.py

from agents.tool import function_tool

@function_tool
def get_destinations_by_mood(mood: str, interest: str):
    """
    This is a mock version that returns predefined options.
    """
    mood = mood.lower().strip()
    interest = interest.lower().strip()

    if mood == "relaxing" and interest == "beach":
        return ["Bali", "Maldives", "Phuket"]

    elif mood == "adventurous" and interest == "mountains":
        return ["Swiss Alps", "Rocky Mountains", "Nepal"]

    elif mood == "romantic" and interest == "city-walks":
        return ["Paris", "Venice", "Barcelona"]

    else:
        return ["New York", "Tokyo", "London"]  # fallback list
