# BudgetTrip-Assistant

BudgetTrip-Assistant is a Streamlit-based web application that leverages Google Gemini AI to provide optimized travel plans based on user preferences.

## 🚀 Features

✅ **AI-Powered Travel Planning**: Uses Google Gemini AI to generate personalized travel itineraries.

✅ **Smart Budgeting**: Estimates total trip costs, including transport, hotels, and activities.

✅ **Multiple Travel Modes**: Provides options for flights, trains, buses, and cars.

✅ **Real-Time Sorting**: Sorts travel options by price, duration, or recommendation.

✅ **Currency Selection**: Supports multiple currencies for cost estimation.

✅ **Weather Forecast & Local Insights**: Offers weather predictions and cultural tips for destinations.

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini Pro
- **Backend**: Python

## 💡 How It Works

1️⃣ **Enter Travel Details**: Users provide travel dates, destinations, budget, and preferences.

2️⃣ **AI Processing**: Google Gemini AI analyzes and suggests the best travel plan.

3️⃣ **Optimized Results**: Users receive a structured itinerary with cost breakdowns and recommendations.

## 🚀 Installation & Usage

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Susmitha-star/BudgetTrip-Assistant.git
cd BudgetTrip-Assistant
```

### 2️⃣ Install Dependencies
Make sure you have Python installed, then install the required libraries:
```sh
pip install streamlit google-generativeai pillow
```

### 3️⃣ Set Up the API Key
- Get a Google Gemini AI API key from Google AI Studio.
- Add your API key in the `os.environ["GOOGLE_API_KEY"]` line inside the script.

### 4️⃣ Run the Application
```sh
streamlit run app.py
```

## 📈 Upcoming Features

🌟 **Multi-Destination Trips**  
🛠️ **Customizable Itinerary Editing**  
✨ **Offline Mode with Cached Data**  
👨‍💻 **Collaborative Travel Planning**  
🛡️ **AI-Based Travel Safety Tips**  

## 📜 License

This project is open-source and licensed under the MIT License.

## 🖼️ Repository Structure
```
BudgetTrip-Assistant/
├── LICENSE                   # License information
├── README.md                 # Project documentation  
├── app.py                    # Main Streamlit application  
├── requirements.txt          # Python dependencies  
```

## 🤝 Contributing

Contributions are welcome! Feel free to submit a Pull Request or report issues.
