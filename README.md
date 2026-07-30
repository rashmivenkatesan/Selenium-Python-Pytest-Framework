# Selenium Python Pytest Framework

## Project Overview

This project is a Selenium Automation Testing Framework developed using **Python**, **Pytest**, and the **Page Object Model (POM)** design pattern. The framework automates the login functionality of the SauceDemo application and follows industry-standard automation practices.

---

## Technologies Used

* Python
* Selenium WebDriver
* Pytest
* Git
* GitHub
* Page Object Model (POM)
* HTML Reports (pytest-html)

---

## Project Structure

```text
SeleniumPytestFramework
│
├── pages/
│   └── login_page.py
│
├── tests/
│   └── test_login.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Features

* Automated login test using Selenium WebDriver
* Page Object Model (POM) implementation
* Pytest framework integration
* Browser setup and teardown using Pytest fixtures
* HTML test report generation using pytest-html
* Version control using Git and GitHub

---

## Installation

Clone the repository:

```bash
git clone https://github.com/rashmivenkatesan/Selenium-Python-Pytest-Framework.git
```

Navigate to the project folder:

```bash
cd Selenium-Python-Pytest-Framework
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Tests

Execute all tests:

```bash
pytest
```

Generate an HTML report:

```bash
pytest --html=report.html
```

---

## Test Scenario

**Login Test**

* Launch Chrome browser
* Open SauceDemo application
* Enter valid username
* Enter valid password
* Click Login
* Verify successful login by checking the inventory page

---

## Future Enhancements

* Explicit waits
* Data-driven testing
* Cross-browser testing
* Screenshot capture on test failure
* CI/CD integration with GitHub Actions
* Allure reporting

---

## Author

**Rashmi Venkatesan**

GitHub: https://github.com/rashmivenkatesan
