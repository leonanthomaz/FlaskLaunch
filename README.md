<div align="center">
  <img src="https://i.postimg.cc/prT5cLCd/logo-flaskaunch-transparent.png" alt="Logo do FlaskLaunch" width="200">
</div>

## FlaskLaunch: Supercharge Your Flask Development

FlaskLaunch is a command-line tool designed to supercharge the creation of Flask-based web applications. It provides a standardized, best-practice project structure and streamlines the integration of essential features, empowering developers to focus on building core application logic rather than tedious project scaffolding.

## Key Features


*   **Lightning-Fast Project Initialization:** Bootstrap a fully functional Flask project structure in seconds with a single, intuitive command. Get up and running quickly and start coding your application logic immediately.
*   **Modular and On-Demand Feature Integration:** Seamlessly integrate support for RESTful APIs (powered by Flask-RESTful), databases (using Flask-SQLAlchemy), and modern web templating (with Flask-Bootstrap) only when needed. Avoid unnecessary dependencies and keep your project lean.
*   **Robust and Adaptable Configuration:** Leverage the power of `settings.yaml` and Dynaconf for flexible and manageable configuration. Easily switch between development, testing, and production environments without code changes.
*   **Intuitive and User-Friendly CLI:** A clean and easy-to-use command-line interface simplifies project setup, feature integration, and common development tasks. Spend less time wrestling with configuration and more time building.
*   **Best-Practice Project Structure:** The generated project adheres to best practices for Flask development, promoting maintainability, scalability, and avoiding common pitfalls like circular imports. Write clean, organized code from the start.
*   **Extensible and Customizable:** FlaskLaunch provides a solid foundation that's easy to extend and customize to your specific project needs. Adapt the generated project to match your unique requirements.

## Inspiration

This project was inspired by a video lesson by Bruno Rocha ([@rochacbruno](https://github.com/rochacbruno)) on structuring Flask applications to avoid circular import issues, specifically his approach using the `init_app` pattern.  You can find the video lesson here: [https://www.youtube.com/watch?v=-qWySnuoaTM&ab_channel=CodeShow](https://www.youtube.com/watch?v=-qWySnuoaTM&ab_channel=CodeShow)

## Installation

```bash
pip install flasklaunch
````

## Getting Started

After installation, you can initialize a new Flask project with:

```bash
flasklaunch init-project
```

This will create a new directory (named after your project) with the basic Flask project structure. Navigate into the new directory:

```bash
cd <your_project_name>
```

Then, you can start the development server:

```bash
flask run
```

## Available Commands

FlaskLaunch offers a suite of helpful commands:

  * `flasklaunch init-project`: Initializes a new Flask project with the standard structure.
  * `flasklaunch add-api`: Integrates support for a RESTful API using Flask-RESTful.
  * `flasklaunch add-db`: Adds database integration via Flask-SQLAlchemy.
  * `flasklaunch add-web`: Incorporates web templating with Flask-Bootstrap.
  * `flasklaunch create-db`: Creates the database schema using Flask-Migrate.
  * `flasklaunch drop-db`: Drops all database tables (for development/testing purposes).
  * `flasklaunch generate-requirements`: Generates the `requirements.txt` file listing project dependencies.
  * `flasklaunch run-app`: Runs the Flask development server.
  * `flasklaunch version`: Displays the current FlaskLaunch version.

## Contributing

Contributions are welcome\!  Please see the [CONTRIBUTING.md](https://www.google.com/url?sa=E&source=gmail&q=CONTRIBUTING.md) file for guidelines.

## License
```
MIT License

Copyright (c) 2025 Leonan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


