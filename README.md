# BashaShareBD – Accommodation Sharing System

## Overview

BashaShareBD is a web-based accommodation-sharing platform developed to make it easier for people in Bangladesh to find and share accommodation information.

The system allows users to create accounts, log in, add accommodation listings, and search for available places by location. It also includes an admin panel where administrators can manage accommodation listings.

This project was developed as part of an undergraduate Software Quality and Testing (SQT) course. It focuses on basic web application development, functional testing, and automated testing using Selenium WebDriver and pytest.

## Objectives

- Develop a simple platform for sharing accommodation information.
- Implement user registration and login functionality.
- Allow users to add, view, and search accommodation listings.
- Provide administrators with listing management features.
- Implement basic authentication and access control.
- Test important system features using automated testing tools.

## Key Features

### User Features
- User registration and login
- Duplicate email validation
- Password hashing
- User dashboard
- Add accommodation listings
- View approved accommodation listings
- Search accommodations by location
- Logout functionality

### Admin Features
- Admin login and access control
- View pending accommodation listings
- Approve or reject listings
- Manage submitted accommodation information

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Flask | Web application framework |
| HTML and CSS | Frontend design |
| SQLite | Database |
| SQLAlchemy | Database management |
| Werkzeug | Password hashing |
| Selenium WebDriver | Browser automation |
| pytest | Automated test execution |
| Google Chrome | Browser used for testing |

## System Testing

Automated testing is an important part of this project. Selenium WebDriver is used to simulate user actions in a browser, while pytest is used to execute test cases and check the results.

The test suite covers:

- Homepage loading
- User registration
- Valid and invalid login
- Adding accommodation listings
- Viewing and searching listings
- Logout functionality
- Dashboard access control
- Unauthorized access to protected pages
- Admin access and listing management

Screenshots are also captured during selected tests to provide evidence of test execution.

## Project Structure

```text
BashaShareBD/
├── instance/
│   └── bashashare.db
├── screenshots/
├── static/
├── templates/
│   ├── add_listing.html
│   ├── admin.html
│   ├── base.html
│   ├── dashboard.html
│   ├── index.html
│   ├── listings.html
│   ├── login.html
│   └── register.html
├── tests/
│   ├── test_admin.py
│   ├── test_home.py
│   ├── test_listing.py
│   ├── test_login.py
│   ├── test_register.py
│   └── test_security.py
├── app.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd BashaShareBD
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

For Git Bash on Windows:

```bash
source .venv/Scripts/activate
```

### 4. Install the required dependencies

```bash
pip install -r requirements.txt
```

If the requirements file is not configured, install the packages manually:

```bash
pip install flask flask-sqlalchemy werkzeug selenium pytest
```

### 5. Run the application

```bash
python app.py
```

Open the following URL in your browser:

http://127.0.0.1:5000

## Running Automated Tests

Make sure the application and Selenium WebDriver environment are properly configured before running the tests.

Run all test cases:

```bash
python -m pytest tests -v -s
```

Run a specific listing test:

```bash
python -m pytest tests/test_listing.py::test_add_listing -v -s
```

The test results indicate whether individual test cases pass or fail.

## Security Features

The application includes basic security measures such as:

- Password hashing
- Session-based authentication
- Protected routes for logged-in users
- Role-based access control for administrators
- Validation of duplicate email addresses
- Rejection of invalid login credentials

## Limitations

- The application uses SQLite, which is suitable for a small academic project.
- Search functionality is mainly based on location.
- Online booking and payment are not included.
- The application uses basic authentication mechanisms.
- Automated testing mainly focuses on functionality and access control.
- The current implementation does not include advanced features such as real-time availability or email notifications.

## Future Improvements

The system can be improved by adding:

- Advanced search and filtering options
- Accommodation image uploads
- User reviews and ratings
- Online booking functionality
- Real-time accommodation availability
- Email notifications
- Additional security testing
- Deployment to a production server

## Learning Outcomes

Through this project, we gained practical experience in:

- Developing a web application using Flask
- Working with databases using SQLite and SQLAlchemy
- Implementing basic authentication and access control
- Writing automated test cases using Selenium and pytest
- Testing positive and negative scenarios
- Identifying and debugging software issues
- Understanding the importance of software quality and testing

## Conclusion

BashaShareBD is a simple accommodation-sharing web application developed as an undergraduate academic project. It combines basic web development with automated software testing to demonstrate how an application can be developed, tested, and improved. The project provides practical experience in functional testing, browser automation, authentication testing, and software quality assurance.
