# My Flask Project

This is a basic Flask project generated with FlaskLaunch. It serves as a starting point for developing robust and scalable web applications.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the development server](#running-the-development-server)
  - [Adding routes](#adding-routes)
  - [Using the database](#using-the-database)
  - [Integrating with the frontend](#integrating-with-the-frontend)
- [Project Structure](#project-structure)
- [Commands](#commands)
- [Tests](#tests)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project was generated with FlaskLaunch, a Python command-line package that assists in creating Flask projects. It sets up the initial folder structure, dependencies, and files, allowing you to focus on the business logic of your application.

## Installation

1. Clone this repository:

   ```
   git clone [https://github.com/your-username/your-project-name.git](https://www.google.com/search?q=https://www.google.com/search%3Fq%3Dhttps://github.com/your-username/your-project-name.git)


2. Create a virtual environment:

   ```
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   ```
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```

4. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

### Running the development server

```
flask run
```

### Adding routes

1. Create a new Python file inside the `app/api/resources` folder (or use the existing files).
2. Define your routes using Flask decorators (`@app.route`) or `flask_restful` (`api.add_resource`).
3. Register your routes in the `app/api/__init__.py` file.

### Using the database

1. Configure the database URI in the `settings.yaml` file.
2. Create the database tables:

   ```
   flask db upgrade
   ```

### Integrating with the frontend

1. Create your HTML templates inside the `app/templates` folder.
2. Render the templates from your routes using the Flask `render_template` function.

## Project Structure

```
.
├── .env                # Environment variables file
├── README.md           # This file
├── requirements.txt    # Project dependencies
├── run.py              # Application execution file
├── settings.yaml       # Configuration file
└── app/
    ├── __init__.py     # Application initialization
    ├── api/
    │   ├── __init__.py   # API initialization
    │   └── resources/   # API resources
    │       └── home.py   # Example resource
    ├── config/
    │   ├── __init__.py   # Configurations initialization
    │   └── configuration.py # Application configurations
    ├── extensions/
    │   └── __init__.py   # Extensions initialization
    └── tests/          # Application tests
```

## Commands

FlaskLaunch provides the following commands to help you manage your project:

- `flasklaunch add-api`: Adds support for a RESTful API (flask-restful).
- `flasklaunch add-db`: Adds support for a database (flask-sqlalchemy).
- `flasklaunch add-web`: Adds support for web templates and views (flask-bootstrap).
- `flasklaunch create-db`: Creates the database using Flask-Migrate and dynamic configurations.
- `flasklaunch drop-db`: Removes all database migrations.
- `flasklaunch generate-requirements`: Generates the `requirements.txt` file with the installed dependencies.
- `flasklaunch init-project`: Initializes the basic structure of the Flask project.
- `flasklaunch run-app`: Runs the Flask application.
- `flasklaunch version`: Displays the FlaskLaunch version.

## Tests

To run the tests, use the following command:

```
pytest
```

## Contributing

Feel free to contribute to this project! To do so:

1. Fork this repository.
2. Create a branch with your feature (`git checkout -b my-feature`).
3. Make the changes and submit a pull request.

**How to use:**

1. Copy the texte above.
2. Paste it into a file named `README.md` at the root of your Flask project.


