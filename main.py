import streamlit as st
from agents import RunConfig , Runner, Agent
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel
import os
from dotenv import load_dotenv
from agent_needed.destination_agent import create_destination_agent
from agent_needed.booking_agent import create_booking_agent
from agent_needed.explore_agent import create_explore_agent
import asyncio

st.set_page_config(page_title="Travel Designer Agent", page_icon="🌍")

load_dotenv()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

client = AsyncOpenAI(
    api_key = openrouter_api_key,
    base_url="https://openrouter.ai/api/v1"
)


model_ai = OpenAIChatCompletionsModel(
    model = "openai/gpt-3.5-turbo",
    openai_client = client,
)

config = RunConfig(
    model = model_ai,
    tracing_disabled= True,
)
destination_agent = create_destination_agent(model_ai)
booking_agent = create_booking_agent(model_ai)
explore_agent = create_explore_agent(model_ai)

st.title("🌍 Travel Designer Agent")
if "step" not in st.session_state:
    st.session_state.step = "mood"

if st.session_state.step == "mood":
    mood = st.selectbox("How are you feeling today?", ["Adventurous and Mountains", "Relaxing and Beach", "Romantic and City-walks"])

    if st.button("Find Destinations"):
        st.session_state.mood = mood
        dest_result = asyncio.run(Runner.run(destination_agent, mood))
        st.session_state.destinations = dest_result.final_output.strip().split("\n")
        st.session_state.step = "destination"


if st.session_state.step == "destination":
    st.subheader("📍 Suggested Destinations:")
    for d in st.session_state.destinations:
        st.markdown(f"- {d}")
    destination = st.text_input("Which destination would you like to book?")
    if st.button("Book Trip"):
        st.session_state.destination = destination
        booking_result = asyncio.run(Runner.run(booking_agent, f"I want to book a trip to {destination}"))
        st.session_state.booking_info = booking_result.final_output
        st.session_state.step = "flight"


if st.session_state.step == "flight":
    st.subheader("🛫 Booking Details:")
    st.write(st.session_state.booking_info)
    selected_flight = st.selectbox("Select flight option:", ["1", "2", "3"])
    if st.button("Confirm Flight"):
        st.session_state.selected_flight = selected_flight
        st.success(f"✈️ You've selected flight option {selected_flight} for {st.session_state.destination}.")
        explore_result = asyncio.run(Runner.run(explore_agent, f"What can I do in {st.session_state.destination}?"))
        st.session_state.attractions = explore_result.final_output.strip().split("\n")
        st.session_state.step = "explore"


if st.session_state.step == "explore":
    st.subheader(f"🎒 Things to do in {st.session_state.destination.title()}:")
    for place in st.session_state.attractions:
        st.markdown(f"- {place}")