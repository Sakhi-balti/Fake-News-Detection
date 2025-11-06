import tkinter as tk
from tkinter import messagebox
import pickle

# Load saved model and vectorizer
lr_model = pickle.load(open('model_LR.pkl', 'rb'))
vect = pickle.load(open('vectorizer.pkl', 'rb'))

# Clean text (simple version)
import re
def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Predict function
def predict_news():
    news = entry.get("1.0", tk.END).strip()
    if not news:
        messagebox.showwarning("Input Error", "Please enter some news text!")
        return
    
    cleaned_news = clean_text(news)
    vect_news = vect.transform([cleaned_news])
    prediction = lr_model.predict(vect_news)[0]

    if prediction == 0:
        result_label.config(text="❌ This is Fake News", fg="red")
    else:
        result_label.config(text="✅ This is Real News", fg="green")

# Create GUI window
root = tk.Tk()
root.title("Fake News Detection System")
root.geometry("1200x800")
root.config(bg="#1e1e1e")

# Title
tk.Label(root, text="📰 Fake News Detector", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="white").pack(pady=10)

# Text box
entry = tk.Text(root, height=10, width=55, font=("Arial", 11))
entry.pack(pady=10)

# Predict button
tk.Button(root, text="Check News", command=predict_news, bg="#0078D7", fg="white", font=("Arial", 12, "bold"), width=20).pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#1e1e1e")
result_label.pack(pady=10)

root.mainloop()
