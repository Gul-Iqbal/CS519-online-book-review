# 📚 Online Book Review and Recommendation System

A Django-based web application to help users discover, review, and share books. Developed as a Final Year Project for CS-519 at Virtual University of Pakistan.

---

## 🔧 Features

- 👤 User Registration, Login, Logout
- 📘 Book Catalog with Search
- 📝 Book Details with Reviews & Ratings (1–5)
- 🌟 Personalized Recommendations (by genre)
- 📌 Wishlist (Add/remove books)
- ✍️ User Profile (Reviews, Wishlist, Bio, Profile Picture)
- 🧑‍💻 Admin Panel (Add/edit/delete books)
- 🚩 Report Inappropriate Reviews
- 📤 Social Sharing (Twitter, Facebook, WhatsApp)
- 📄 About & Contact Pages

---

## 💡 Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, Tailwind CSS, JavaScript
- **Database:** SQLite3
- **Tools:** PyCharm, GitHub, Django Admin

---

## 📂 Folder Structure
online_book_review/
├── accounts/
├── books/
├── templates/
├── static/
├── db.sqlite3
└── manage.py


---

## 🚀 How to Run

```bash
# Clone project
git clone <your-repo-url>

# Setup virtual environment (optional)
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows

# Install Django
pip install django

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run server
python manage.py runserver


