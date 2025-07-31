# 🌍 Travel Designer Agent

**Travel Designer Agent** is a smart, multi-agent travel planning assistant built using the [OpenAI Agent SDK](https://openai.com/blog/assistants-api) and powered by OpenRouter models. It helps users choose travel destinations based on their mood, book flights, and explore local attractions — all through a conversational UI built with **Streamlit**.

---

## ✨ Features

- 🤖 **Multi-Agent Intelligence**
  - `DestinationAgent`: Recommends travel destinations based on user mood.
  - `BookingAgent`: Suggests flight options and handles booking.
  - `ExploreAgent`: Provides a list of things to do at the chosen destination.

- 🧠 **Model-Powered Decisions**
  - Uses OpenRouter-hosted LLMs for agent logic and conversation handling.

- 🖼️ **Interactive UI with Streamlit**
  - Mood-based destination selection.
  - Flight booking and confirmation.
  - Real-time suggestions on what to explore.

---

## 🚀 How It Works

1. The user selects their **mood** (e.g., adventurous, relaxing, romantic).
2. The `DestinationAgent` suggests suitable travel spots.
3. The user picks one destination and proceeds to **book a trip**.
4. The `BookingAgent` shows flight options.
5. After selecting a flight, the `ExploreAgent` recommends things to do at that location.

All interactions happen live inside the Streamlit app.

---

## 🛠️ Tech Stack

| Tech           | Purpose                                 |
|----------------|------------------------------------------|
| `OpenAI Agent SDK` | Manages agent creation and handoff      |
| `OpenRouter`   | Hosts the LLMs used for agents           |
| `Python`       | Core logic                               |
| `Streamlit`    | User interface                           |
| `.env`         | Securely loads API keys                  |

---


