# Blind Date with a Book 📚✨  

## Overview  
Blind Date with a Book is a fun web application where users can discover a new book without knowing its title or cover beforehand. 
Inspired by the “blind date” concept, it encourages readers to explore outside their usual genres and find hidden gems.  

This app was primarily designed to be used by book club leaders to generate a new book and set deadlines. However, it could also be
used by avid readers that are seeking some inspiration for their next read.

This project was developed as part of the Code First Girls course, showcasing our learning in Python, MySQL, and Flask while collaborating as a team.  

---

## Features  
- 🎲 **Random Book Generator** – get a surprise book suggestion at the click of a button.  
- 📖 **Genre Selection** – choose a genre and let the app recommend a book.  
- 💾 **Database Storage** – all books are stored in a MySQL database for easy retrieval.  
- 🌐 **Flask API** – provides endpoints to fetch books by genre or at random.  
- 🖥️ **User-friendly Interface** – simple design for quick discovery.  

---

## Tech Stack  
- **Backend:** Python (Flask)  
- **Database:** MySQL  
- **Frontend:** Terminal UI  
- **Other:** Git/GitHub for version control  

---

## Installation & Setup  

### 1. **Clone the repo**  
```bash
git clone https://github.com/your-repo/blind-date-with-a-book.git
cd blind-date-with-a-book
```
### 2. **Set up a virtual environment**  
```bash
python -m venv venv
# Mac/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3) Install dependencies
Requirements include: Requests, Flask and MySQLConnector.
```bash
pip install -r requirements.txt
```

### 4) Update Config file
Update `config.py` with your database credentials:
```ini
USER = "YOUR USERNAME"
PASSWORD = "YOUR PASSWORD"
HOST = "localhost"
DATABASE = "LibraryDB"
```

### 5) Set up the database
- Open your MySQL terminal and run the provided SQL script (`database_setup.sql`) to create the required
database ('LibraryDB') and tables.


### 6) Run the app
```bash
# Start the Flask API
python flask_api.py

# Start the main app
python main.py
```
Now interact with the terminal-based user interface.  

---

## API Endpoints
- `GET /books` → returns all books in the database  
- `GET /books/current` → returns the most recent book in the database  
- `GET /books/add` → adds a new book to the database

**Example response**
```json
{
  "title": "Example Book",
  "author": "Jane Doe",
  "genre": "Romance"
}
```

---

## Project Structure  
```
group-2-blind-date-with-a-book/
├─ venv/                     # Python virtual environment
├─ .gitignore
├─ README.md                 # Project documentation
├─ requirements.txt          # Python dependencies
├─ database/
│   ├─ database_setup.sql    # SQL script to create DB and tables
│   └─ config.py             # Database configuration
├─ app/                      # Source code for the project
│   ├─ __init__.py
│   ├─ book.py               # Book logic
│   ├─ book_api.py           # API helper functions
│   ├─ db_utils.py           # Database helper functions
│   ├─ deadline.py           # Deadline management
│   ├─ flask_api.py          # Flask API server
│   └─ ui.py                 # Terminal UI logic (renamed to lowercase)
├─ tests/                    # Unit tests
│   ├─ __init__.py
│   └─ test.py               # Tests for main functions
└─ main.py                   # Terminal UI entrypoint
```

---

## Testing
Unit tests are included in `test.py`. To run the tests:  
```bash
python test.py
```
Ensure the virtual environment is active and dependencies are installed. These tests cover core functionalities like book retrieval, API responses, and database interactions.  

---

## Roadmap / Future Improvements
- Wider genre and book choices
- User registration and personalised recommendations
- Genre voting
- Options to choose and adjust deadlines
- Ratings, reviews and favourites
- Deadline reminders
- Responsive UI improvements
- Further amendments to reduce errors (e.g. books in different languages)

---

## Contributors
Developed by **Group 2 – Code First Girls CFGdegree**  
- Rachel Fuller
- Debbie Richford
- Allize Renae
- Maisie Pepper
- Kav Ravikumar
- Nemi Imoh
- Janine O'Connor

---

