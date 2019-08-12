# SentimentalHackerNews

### Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [How To use?](#how-to-use?)
* [Features](#features)

### General info
SentimentalHackerNews is a django project to detect sentiments of titles of trending hacker news stories.

### Technologies
Project is created with:
* Django==2.2.3
* aylien_apiclient==0.7.0
* django_apscheduler==0.3.0
* requests==2.22.0
* APScheduler==3.6.1
* python-dotenv==0.10.3
* gunicorn==19.9.0

### How to use?
To use this app locally, follow these steps:
1. Clone the project
2. Install requirements using `pip install -r requirements.txt`
3. Make migrations ` python manage.py makemigrations `
4. Migrate `python manage.py migrate `
5. Run `python manage.py runserver`
6. Default access on browser via `http://127.0.0.1:8000/`

### Features
* Sentimental Analysis using AYLIEN API
* Cron Job/Backgroud Task using django_apscheduler to update top story list after every 30 minutes
* Trending Stories list hacker news
* Partial Searching

