# ✈️ Airline Fare Predictor — Smart Ticket Price Estimator

A machine learning-powered web tool to predict airline ticket prices based on journey details, airline, booking date, and more. It not only predicts fare but shows price **fluctuations over days** and **compares airlines** to help users make cost-effective decisions.

---

## 🚀 Features

✅ **Predict Flight Fares**  
Input your journey details and get an instant fare prediction using a trained ML model.

✅ **Price Trends Over Time**  
See how the fare changes if you book today, 10 days later, 15 days later, or 20 days later.

✅ **Compare Multiple Airlines**  
Given the same route and day, compare predicted fares for top airlines like Air India, Vistara, IndiGo, and more.

✅ **Confidence Intervals (Uncertainty)**  
Fare prediction comes with a ± range (e.g., ₹4200 ± ₹150) to reflect real-world pricing variability.

✅ **User-Friendly Input**  
Inputs like departure time, class, stops, duration, etc., are used to personalize prediction.

---

### ✈️ Sample Route Prediction

**Route:** Delhi → Mumbai on `2025-06-10`

---

#### 🛫 Air India
- **Booking today:** ₹4620 ± ₹120  
- **Booking after 10 days:** ₹4820 ± ₹140 &nbsp; 📈 *Increase of ₹200*

---

#### 🛫 Vistara
- **Booking today:** ₹4490 ± ₹110  
- **Booking after 10 days:** ₹4400 ± ₹105 &nbsp; 📉 *Decrease of ₹90*

---

#### 🛫 IndiGo
- **Booking today:** ₹4350 ± ₹130  
- **Booking after 10 days:** ₹4600 ± ₹140 &nbsp; 📈 *Increase of ₹250*



---

## 🧠 How It Works

1. **Preprocessing**: Dates, time categories, and text fields are cleaned and encoded.
2. **Feature Engineering**: Extracts features like month, year, day of journey, and time bins.
3. **Model Training**: A `RandomForestRegressor` is used for training on historical flight data.
4. **Prediction with Intervals**: Each prediction comes with a confidence interval using prediction distributions.
5. **Dynamic Input**: User can select airline, date, stops, class, and get personalized results.

---

## 🧪 Tech Stack

- Python 🐍
- Pandas, NumPy
- Scikit-learn
- Matplotlib / Seaborn (for optional visualization)
- (Optional) Streamlit or Flask for UI

---


---

## 📌 Future Enhancements

- 🌐 Integrate real-time data from airline APIs
- 📱 Build mobile-friendly UI
- 💬 Add chatbot interface for flight search
- 📈 Visualize fare trends on graphs

---

## 👨‍💻 Author

**Mohammad Anas Alam**  
Data Science & Analytics Enthusiast  
📧 anasalam9692@gmail.com  
🔗 [Portfolio](https://mohammadanas02.github.io/Anas-Portfolio/) | [GitHub](https://github.com/mohammadanas02) | [Linkedin](https://www.linkedin.com/in/mohammad-anas02/)

---

## 📄 License

This project is open-source and free to use for non-commercial purposes.  
Commercial licensing available on request.




