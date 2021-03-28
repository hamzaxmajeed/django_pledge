# Do Nation Pledges

## About

Using the design and requirements:

- Created an application that allows individuals to pledge to do an action to improve their lives and make an environmental impact. 

- Each action in the system is capable of supporting multiple metrics, for example, CO2, water and waste.

- When a user pledges to do an action, they answer a few questions which generate the savings expected if they do as promised.

- Created a url file inside impacts app and included that file from the url file of project. 

- Made two Models: Bills and Veg model to save the pledges in db and list them on home page.

- Created two different view functions and html pages, one for veg out pledge and one for clean your bills pledge.

- Grabbing data from html forms and calculating the impacts made inside views and then saving them inside the model. 

## Things To Improve

If I had more time, I would make the following changes or improvements:

- Adding a login authentication functionality for each user that makes a pledge.

- Making the application responsive and mobile friendly.

- Creating a dynamic header title that changes based on what page we're on rather than hard coding it.

- Creating a better UI.

- Cleaning HTML templates by writing code that allows better readability.

- Do further unit testing in tests.py, including some edge cases and more variations for each pledge.

## Setup

Ensure you have python 3.6+ installed.

```bash
pip install -r requirements.txt
```

## To Run Server

```bash
python manage.py runserver
```