import streamlit as st
import requests
import json

OPENROUTER_API_KEY = "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"
LLAMA_API_ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
}
def llama_generate(query):
    payload = {
        "model": "meta-llama/llama-3.1-8b-instruct:free",  # Specify the model
        "messages": [
            {"role": "user", "content": query}
        ]
    }

    response = requests.post(LLAMA_API_ENDPOINT, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        response_data = response.json()
        return response_data["choices"][0]["message"]["content"]  # Assuming this structure from the API response
    else:
        st.error(f"Error: {response.status_code}, {response.text}")
        return None

# Travel Places Suggestion
def suggest_travel_places(query):
    return llama_generate(query)

# Explaining the History of a Place
def explain_history(query):
    return llama_generate(query)

# Booking Travel Cancellations
def book_cancellation(query):
    return f"Booking cancellation for query: {query} has been processed."

# Refunding
def process_refund(query):
    return f"Refund processed for query: {query}."

# Local Cuisine Guides
def local_cuisine_guides(query):
    return llama_generate(query)

# Router Function
def router(query):
    if "suggest" in query.lower() or "recommend" in query.lower() or "suggestion" in query.lower() or "recommendation" in query.lower():
        return suggest_travel_places(query)
    elif "history" in query.lower():
        return explain_history(query)
    elif "cancel" in query.lower() or "cancellation" in query.lower():
        return book_cancellation(query)
    elif "refund" in query.lower():
        return process_refund(query)
    elif "cuisine" in query.lower() or "food" in query.lower() or "restaurant" in query.lower():
        return local_cuisine_guides(query)
    else:
        return "I'm not sure how to help with that. Please try rephrasing your query."

# Streamlit App
st.title("Travel Assistant App")

# Section 1: Travel Options
st.header("1. Travel Options")
travel_query = st.text_input("Enter your travel query (e.g., suggest places, explain history, etc.):")
if st.button("Get Travel Suggestions"):
    if travel_query:
        travel_response = router(travel_query)
        st.write(travel_response)

# Section 2: Refund Options and Cancelling Operations
st.header("2. Refund Options and Cancelling Operations")
refund_cancel_query = st.text_input("Enter your refund or cancellation query (e.g., cancel booking, process refund):")
if st.button("Handle Refund/Cancel"):
    if refund_cancel_query:
        refund_cancel_response = router(refund_cancel_query)
        st.write(refund_cancel_response)

# Section 3: Flight Assistant (Questions related to Check-In)
st.header("3. Flight Assistant (Questions related to Check-In)")
flight_query = st.text_input("Enter your flight-related query (e.g., check-in information):")
if st.button("Get Flight Information"):
    if flight_query:
        flight_response = llama_generate(flight_query)
        st.write(flight_response)
