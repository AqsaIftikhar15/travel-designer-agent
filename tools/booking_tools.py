# tools/booking_tools.py
from agents.tool import function_tool

@function_tool
def get_flights(destination: str, dates: str = "Flexible"):
    return [
        {
            "airline": "FlyHigh Airlines",
            "price": "$450",
            "duration": "8h",
            "departure": "LHR",
            "arrival": destination.upper(),
            "dates": dates
        },
        {
            "airline": "SkyJet",
            "price": "$500",
            "duration": "7h 30m",
            "departure": "KHI",
            "arrival": destination.upper(),
            "dates": dates
        },
         {
            "airline": "Etihad Airways",
            "price": "$600",
            "duration": "9h",
            "departure": "ISB",
            "arrival": destination.upper(),
            "dates": dates
        }
    ]

@function_tool
def suggest_hotels(destination: str, budget: str = "medium"):
    if budget == "luxury":
        return [
            "Grand Palace Hotel - $300/night",
            "Royal Orchid Resort - $250/night"
        ]
    elif budget == "budget":
        return [
            "City Inn - $70/night",
            "Travelers Hostel - $40/night"
        ]
    else:  # medium
        return [
            "Comfort Stay - $120/night",
            "Metro Lodge - $90/night"
        ]
