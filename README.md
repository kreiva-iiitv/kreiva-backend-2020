# Kreiva backend 2020

This project is the backend for Kreiva 2020. It will provide APIs for every thing required by the website, which includes registrations, submissions, displaying submissions for people to view.


# Features!

  - Google oauth2 for every participant
  - Submissions for every event
  - APIs to call for different organising teams for the event

## Tech

Kreiva-backend-2020 uses the following:

* Django - as the backend for the services
* DRF - to provide REST APIs

## Installation

Kreiva-backend-2020 requires django 3.1.1 to run.

For linux users
```sh
$ git clone https://github.com/kreiva-iiitv/kreiva-backend-2020.git
$ cd kreiva-backend-2020
$ sudo pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

For windows users with conda
```sh
$ git clone https://github.com/kreiva-iiitv/kreiva-backend-2020.git
$ cd kreiva-backend-2020
$ conda create -n myenv python=3.8
$ conda activate myenv
$ pip install -r requirements.txt
```

To run the app, follow these steps

```sh
$ python manage.py makemigrations && python manage.py migrate
$ python manage.py runserver
```
Open a browser tab and write http://localhost:8000/ to see the website.


If you'd like to contribute, just make an issue and start working on it!

Contributors - [Tanmay Ambadkar](https://github.com/TanmayAmbadkar), [Yash Shah](https://github.com/theyashshahs)
