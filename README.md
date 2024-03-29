# Django Authentication Project
![example workflow](https://github.com/github/docs/actions/workflows/main.yml/badge.svg)

This Django project provides user authentication features including signup, login, password reset,password change, and logout functionalities.

## Key Features

Signup: Users can create a new account by providing their username, email, and password. Upon successful signup, they are redirected to the login page.

Login: Registered users can log in to their accounts using their username and password. After successful authentication, they are redirected to the home page.

Password Reset: Users who forget their passwords can request a password reset by providing their email address. Upon submission, an email containing a password reset link is sent to the provided email address. Users can then follow the link to reset their passwords securely.

Password Change: Authenticated users can change their passwords securely through the password change functionality. This allows users to update their passwords as needed for security purposes.

Logout: Users can log out of their accounts to end their session securely. After logging out, they are redirected to the home page.

## Implementation Details

Views: The project defines views for home, signup, login, password reset request, password confirmation, and logout functionalities. These views handle user requests and interact with Django's authentication system and user models.

Forms: Custom forms are created for signup, password reset request, and password confirmation, using Django's form handling capabilities.

Templates: HTML templates are used to render user-facing pages, including forms for signup, login, password reset, and password confirmation. These templates provide a user-friendly interface for interacting with the authentication system.

URLs: URL patterns are defined to map user requests to appropriate views. URLs for signup, login, password reset, password confirmation, and logout are configured to enable navigation within the application.

## Requirements

* Python 3.6+
* Django 5.0, 4.2, 4.1, 4.0, 3.2, 3.1, 3.0

We **highly recommend** and only officially support the latest patch release of
each Python and Django series.

## Usage

Users can access the application through a web browser. They can sign up for a new account, log in to existing accounts, request password resets, and log out securely. The application provides a seamless and user-friendly experience for managing user authentication.

## Installation

install using `clone`......

        git clone https://github.com/amirhoseinshojaei/django-authentication.git

**migrations**

        python manage.py makemigrations

        python manage.py migrate

**create super user** 

        python manage.py createsuperuser

## Happy Mood

**Be happy and Enjoy this project , And Always learning**

