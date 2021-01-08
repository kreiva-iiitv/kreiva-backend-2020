# Kreiva backend 2020

This project is the backend for Kreiva 2020. It will provide APIs for every thing required by the website, which includes registrations, submissions, displaying submissions for people to view.


# Features!

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
Make a .env file at the root of your project directory. Generate a secret key and add the following to the file

SECRET_KEY=A_RANDOM_SECRET_KEY

Replace this A_RANDOM_SECRET_KEY with your own secret key. Now run the following commands

```sh
$ python manage.py makemigrations && python manage.py migrate
$ python manage.py runserver
```
Open a browser tab and write http://localhost:8000/ to see the website.

## APIs available

1) /team/ - Organising team names
2) /team_member/ - Organising team members
3) /event/ - Event details in the fest
4) /event_member/ - Event organising member details

Open a browser tab and write https://gaurKrishna.pythonanywhere.com/ to see the website.

If you'd like to contribute, just make an issue and start working on it!

Contributors - [Tanmay Ambadkar](https://github.com/TanmayAmbadkar), [Yash Shah](https://github.com/theyashshahs)
