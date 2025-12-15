# 🎬 Movie Recommender System

A **movie recommendation web application** built using **Python and Streamlit**, which uses data from **TMDB (The Movie Database)** to recommend movies. In this project, the user selects a movie and the system recommends **5 highly similar movies** based on content similarity, along with their posters fetched in real time using the TMDB API.

This project demonstrates the end-to-end pipeline of a recommendation system — from data preprocessing and similarity computation to deploying an interactive web interface.

---

## 🚀 Features

* Content-based movie recommendations using cosine similarity
* Interactive web interface built with Streamlit
* Real-time movie posters fetched via TMDB API
* Clean and user-friendly UI
* Scalable and deployable project structure

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Web Framework:** Streamlit
* **Machine Learning:** Content-Based Movie Recommendation
* **Libraries:** Pandas, NumPy, AST, NLTK, Requests
* **API:** TMDB (The Movie Database)

---

## 📁 Project Structure

```
MovieRecSystem/
│
├── app.py                    # Main Streamlit application
├── model/
│   ├── movie_list.pkl        # Processed movie dataset
│   └── similarity.pkl        # Similarity matrix
├── requirements.txt
├── README.md
```

---

## 🔑 TMDB API Setup

1. Create an account at **themoviedb.org**
2. Generate an API key (v3 auth)
3. Add your API key inside the application:

```python
API_KEY = "YOUR_TMDB_API_KEY"
```

> ⚠️ Do not expose your API key publicly when deploying

---

## ▶️ How to Run the Project

1. Clone the repository

```bash
git clone <repository-url>
cd MovieRecSystem
```

2. Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app

```bash
streamlit run app.py
```

5. Open your browser and go to:

```
http://localhost:8501
```

---

## 📌 Sample Output

* Dropdown to select a movie
* Displays top 5 recommended movies
* Shows movie posters dynamically

---

## 🌱 Future Improvements

* Add movie overview, ratings, and release year
* Implement collaborative filtering
* Add search-based recommendations
* Deploy on Streamlit Cloud

---

## 📚 Learning Outcomes

* Practical understanding of recommender systems
* Hands-on experience with APIs
* Building and deploying ML-powered web apps
* Writing production-ready Python code

---

## 🙋‍♀️ Author

**Manya Khandelwal**
Computer Science Student | AI & ML Enthusiast

---

⭐ If you like this project, feel free to star the repository!
