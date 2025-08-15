This project is a basic test automation setup built with Playwright and Pytest using the Page Object Model. 

It includes fixtures for login, environment variable support through a .env file, and artifact generation (screenshots and HTML) on test failure to help with debugging. 
To get started, install the dependencies with pip install -r requirements.txt and playwright install, then create a .env file containing your base URL, username, and password. 

Once configured, you can run tests by simply executing pytest from the command line, and you may use pytest --headed to run them with a visible browser. 

The project is structured with a pages/ folder for page objects, a tests/ folder for test cases, and a conftest.py file for fixtures and hooks. 

For CI/CD integration, you can add a simple GitHub Actions workflow that installs Python, sets up Playwright browsers, and runs pytest automatically on each push or pull request, ensuring tests are executed consistently in your pipeline.