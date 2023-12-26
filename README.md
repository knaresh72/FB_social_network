Social Network API using Django Rest Framework
Problem Statement
Create an API for a social networking application using Django Rest Framework with the following functionalities.

Constraints
Use any database of your choice.
You are free to design Request/Response fields/formats.
User Login/Signup
Users should be able to login with their email and password (email should be case insensitive).
User should be able to signup with their email only (no OTP verification required, valid email format is sufficient).
Except signup and login, every API should be called for authenticated users only.
API Functionalities
Search Users API

API to search other users by email and name (paginate up to 10 records per page).
If the search keyword matches the exact email, return the user associated with the email.
If the search keyword contains any part of the name, return a list of all users.
Example: Amarendra, Amar, Aman, Abhirama are three users. If users search with "am," then all of these users should be shown in the search result because "am" substring is part of all of these names.
There will be only one search keyword that will search either by name or email.
Friend Request API

API to send/accept/reject friend requests.
List Friends API

API to list friends (list of users who have accepted friend requests).
List Pending Friend Requests API

API to list pending friend requests (received friend requests).
Friend Request Throttling

Users cannot send more than 3 friend requests within a minute.
Project Setup
Install Django and Django Rest Framework:

bash

pip install django djangorestframework
Create a Django Project and App:

bash

django-admin startproject social_network
cd social_network
python manage.py startapp api
Define Models:

Define models for users, friend requests, and friendships in api/models.py.

Create Serializers:

Create serializers in api/serializers.py to convert model instances to JSON and vice versa.

Create Views:

Define views in api/views.py that handle the business logic for the APIs.

Configure URLs:

Configure your API URLs in api/urls.py.

Include API URLs in Project URLs:

Include your API URLs in the project's urls.py.

Configure Django Rest Framework:

Configure DRF settings in your project's settings.py.

Run Migrations:

Run migrations to apply changes to the database.

bash

python manage.py makemigrations
python manage.py migrate
Run Development Server:

Start the development server.


python manage.py runserver
