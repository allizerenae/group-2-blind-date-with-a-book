Blind Date with a Book 📚

Group Two CFG Project
Marker: Asma

Team Members

Debbie Richford

Allize Renae

Rachel Fuller

Janine O’Connor

Maisie Pepper

Kav Ravikumar

Nemi Imoh

#Introduction

Project Objective
The goal of Blind Date with a Book is to build a command line interface tool that helps a book club admin select the club’s next read. The app integrates with the Open Library API, stores reading history in an SQL database, and automatically sets reading deadlines.

Project Solution
This app streamlines decision-making for book clubs, keeping monthly selections fun, fair, and organized, while saving admins valuable time.

#Background
App Workflow

User is welcomed with a message.

Main menu presents three options:

Choose New Book

Select from genres: Horror, Comedy, Romance, Random

Fetch book details from Open Library API

Save book with assigned date + deadline in SQL database

View Current Book and Deadline

Displays current book details + reading deadline

View Book History

Shows previous selections with deadlines and genres

# API used: Open Library API

  Specifications and Design
  Required Features

SQL Database

Open Library API

Reading Deadline (auto-generated)

User Input & Validation

Random Book Suggestions

Flask API

Book Tracker

# Tools and Technologies

Python (with OOP)

SQL / MySQLConnector

Flask

Open Library API

GitHub (collaboration & version control)

Pytest (unit testing)

Itertools & Collections (logic helpers)

Error Handling

# Possible Issues

Duplicate book selections → Need to avoid books already in the database.

# V2 Features (Future Enhancements)

Genre voting

Custom reading deadlines (1 week, 2 weeks, 1 month)

Reminder notifications

Member registration & user accounts

Reviews & ratings

Audiobook option

# Architecture

CLI App: Main program where users interact.

Database Layer: Stores books, history, deadlines, reviews.

API Layer (Flask): Custom endpoints to serve and manage data.

External API: Open Library API for book suggestions.

(Architecture diagram can be inserted here if available.)

# Implementation
# Workload Distribution

Allize – main.py, book.py (Book class), GitHub coordination, project manager, README, documentation

Debbie – ui.py (UI class), documentation

Rachel – ui.py, documentation, unit test setup

Maisie – book_api.py (Open Library API integration), Flask + SQL endpoints

Kav – SQL schema

Nemi – DB utilities

Janine – deadline.py (deadline logic with datetime)

Full Team Contributions:

requirements.txt

Manual testing, unit testing, UAT, regression testing

Code reviews

Presentation slides

# Tools and Libraries Used

Random – Select random book

Datetime – Manage deadlines

Flask – Build custom API

MySQLConnector – Connect app to SQL database

Requests – API calls

Itertools – Logic helpers (e.g., cycling options)

# Testing and Evaluation

Testing approach:

Manual testing of features

Unit testing with Pytest

UAT (User Acceptance Testing)

Regression testing

Elements Tested:

Database connection

Open Library API calls

Random book selection

Adding books to DB

Viewing current book & deadline

Viewing history

OOP class object creation

User flow & input validation

# Implementation Process
Achievements

All members contributed and voted on the final idea

Regular team meetings to track progress

Agile methodology with pair programming in some parts

Challenges

Dividing tasks effectively

Scheduling meetings across availability

Key Decisions

Streamlined initial scope for a working MVP

Deferred advanced features into Future Enhancements

# Conclusion

Blind Date with a Book successfully demonstrates how a CLI app can combine API integration, SQL storage, and OOP design to support book club management.

Future Improvements

User-driven genre choices

Flexible deadline options

Member registration and user accounts

Book reviews and ratings

Reminder notifications for deadlines

Audiobook support

# Installation & Setup
1. Clone Repo
2. Set up virtual environment
3. Install dependencies
4. Configure MySQL database
5. Run the app
6. Run tests
