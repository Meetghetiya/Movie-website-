
# Movie website using django

This repository contains a Django-based movie website that allows users to register, login, activate their account via email verification, reset their password using a verification code, and browse movies based on categories.


## Features

 - #### User Registration :
Users can create an account by providing their details and receive an activation link via email.

 - #### Email Activation :
The activation link sent to the user's email allows them to activate their account and gain access to the website.

 - #### User Login:
Registered users can log in securely to access the movie website.

 - #### Password Reset: 
In case a user forgets their password, they can request a password reset. A verification code is sent to their email, which they can use to reset their password.


 - #### Movie Categories:
Movies are categorized into different genres or categories, making it easier for users to browse and find movies of their interest.
## Setup and Installation

- #### Clone the repository to your local machine:

```bash
  git clone https://github.com/Meetghetiya/Movie-website-using-django.git
```

- #### Navigate to the project directory:

```bash
  cd movie-website
```

- #### Create a virtual environment (recommended) and activate it:

```bash
 python3 -m venv env
source env/bin/activate
```
- #### Install the required Python packages:

```bash
 pip install -r requirements.txt
```

- #### Set up the database:

```bash
 python manage.py migrate
```

- #### Start the development server:

```bash
 python manage.py runserver
```
Access the movie website by opening a web browser and visiting http://localhost:8000.



## Screenshots

<img width="822" alt="website1" src="https://github.com/Meetghetiya/Movie-website-using-django/assets/89141817/93e9e755-5da0-4ec0-8891-924107e52b7a">

<img width="792" alt="website2" src="https://github.com/Meetghetiya/Movie-website-using-django/assets/89141817/808a7098-81f9-4572-b3dd-a179b6587b01">

<img width="839" alt="website3" src="https://github.com/Meetghetiya/Movie-website-using-django/assets/89141817/72543cd7-e601-4431-94c6-323045d1d166">

