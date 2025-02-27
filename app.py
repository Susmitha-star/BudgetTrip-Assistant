import os
import streamlit as st
from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from PIL import Image

# ✅ Set Up API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyBxOmfzVxl8XxloiShveE_2cJD6wVze7pM"

# ✅ Load Banner Image
banner = Image.open("banner.jpg")

# ✅ Initialize LangChain Model with Google Gemini
llm = GoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=os.environ["GOOGLE_API_KEY"])

# ✅ Define Prompt Template for LangChain
travel_prompt = PromptTemplate(
    input_variables=["from_location", "to_location", "travel_date", "mode", "currency", "sort_preference"],
    template="""
    You are an AI-powered travel planner. Plan a trip from {from_location} to {to_location} on {travel_date}.
    Travel mode preference: {mode}
    Preferred currency: {currency}
    Sorting preference: {sort_preference}

    Include:
    - Estimated total budget in {currency}
    - Available travel options (flight/train/bus/car) with:
      - Estimated prices in {currency}
      - Duration of each mode
    - Sort the travel options by {sort_preference} (fastest, cheapest, or recommended)
    - Hotel recommendations and estimated prices
    - Must-visit attractions and activities
    - Weather forecast for the travel period
    - Travel safety tips and local cultural insights
    - Food recommendations (local specialties)
    - Total budget breakdown (transport, hotel, meals, activities)

    Format the response in a structured and professional way.
    """
)

# ✅ Create LangChain Travel Planning Chain
travel_chain = travel_prompt | llm | RunnablePassthrough()

# ✅ Streamlit UI Setup
st.set_page_config(page_title="BudgetTrip Assistant", layout="wide")

# ✅ Display Banner Image
st.image(banner, use_container_width=True)

st.markdown("<h1 style='text-align: center; color: #0078D7;'>🌍 BudgetTrip Assistant</h1>", unsafe_allow_html=True)

# ✅ Input Fields
col1, col2 = st.columns(2)
with col1:
    from_location = st.text_input("🏠 From (Location):", placeholder="Enter your starting location")
    travel_date = st.date_input("📅 Travel Date:")

with col2:
    to_location = st.text_input("📍 To (Destination):", placeholder="Enter your destination")
    mode = st.selectbox("🚗 Preferred Mode:", ["Any", "Flight", "Train", "Bus", "Car"])

# ✅ Currency & Sort By in the Same Row
col3, col4 = st.columns(2)
with col3:
    currency = st.selectbox("💰 Select Currency:", ["INR (₹)", "USD ($)", "EUR (€)",  "GBP (£)", "JPY (¥)"])

with col4:
    sort_preference = st.selectbox("📊 Sort By:", ["Recommended", "Fastest", "Cheapest"])

# ✅ Predict Button
if st.button("🚀 Generate Travel Plan"):
    if from_location and to_location:
        with st.spinner("Generating your travel plan..."):
            result = travel_chain.invoke({
                "from_location": from_location, 
                "to_location": to_location, 
                "travel_date": travel_date.strftime("%Y-%m-%d"), 
                "mode": mode, 
                "currency": currency,
                "sort_preference": sort_preference
            })
        st.success("Here is your travel plan:")
        st.write(result)
    else:
        st.error("Please enter both locations before generating the plan.")
# Footer
st.markdown("""
    <div class='footer'style='text-align: center;'>
        Developed by <b>Susmitha Reddy</b> | Built with ❤️ using Streamlit
    </div>
    """, unsafe_allow_html=True)