# BashaShareBD – Accommodation Sharing System

## Overview

BashaShareBD is a web-based accommodation-sharing platform developed to help people in Bangladesh find and share accommodation information. Users can register, log in, add accommodation listings, view available places, and search for accommodation by location. Administrators can manage listings through an admin panel.

This project was developed as part of an undergraduate Software Quality and Testing (SQT) course. It focuses on web application development, basic security, functional testing, and automated testing.

## Problem Statement

Finding suitable accommodation can be difficult because information is often scattered across different sources. Users may also struggle to find places that match their preferred location and rent.

BashaShareBD provides a centralized platform where users can easily share and search accommodation information.

## Objectives

- Develop a simple and organized accommodation-sharing platform.
- Implement user registration and login functionality.
- Allow users to add, view, and search accommodation listings.
- Provide administrators with listing management features.
- Implement basic authentication and access control.
- Test important system functionalities using Selenium and pytest.

## Key Features

### User Features
- User registration and login
- Duplicate email validation
- Password hashing and session-based authentication
- User dashboard
- Add accommodation listings
- View approved accommodation listings
- Search accommodations by location
- Logout functionality

### Admin Features
- Admin panel with access control
- View accommodation listings
- Approve or reject listings
- Manage submitted accommodation information

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Flask | Backend web framework |
| HTML and CSS | Webpage structure and design |
| SQLite | Database |
| SQLAlchemy | Database operations |
| Werkzeug | Password hashing |
| Selenium WebDriver | Browser automation |
| pytest | Automated test execution |
| Google Chrome | Browser used for testing |

## System Architecture

The application follows a simple web architecture in which users interact with HTML pages, Flask handles application logic, SQLAlchemy manages database operations, and SQLite stores user and accommodation information.

For automated testing, pytest runs test cases, Selenium WebDriver controls Google Chrome, and the browser interacts with the BashaShareBD application just as a real user would.

## Database

The application uses SQLite with two main models:

- **User:** Stores user information, including name, email, phone, password, role, and trust score.
- **Listing:** Stores accommodation details, including title, location, rent, description, status, and owner ID.

The `owner_id` connects each accommodation listing to the user who created it.

## Testing

Automated testing is performed using Selenium WebDriver and pytest. The tests simulate user actions in the browser and verify whether the application behaves as expected.

The test suite covers:

- Homepage loading
- User registration
- Valid and invalid login
- Adding accommodation listings
- Viewing and searching listings
- Logout functionality
- Dashboard access without login
- Access control for protected pages
- Admin access and listing management

Screenshots are also captured during selected tests as evidence of test execution.

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd BashaShareBD
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/Scripts/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open the following URL in your browser:

http://127.0.0.1:5000

## Running Automated Tests

Make sure the application and Selenium environment are properly configured.

Run all tests:

```bash
python -m pytest tests -v -s
```

Run a specific listing test:

```bash
python -m pytest tests/test_listing.py::test_add_listing -v -s
```

The test results show which test cases pass and which fail, helping identify problems in the application.

## Security

The project includes basic security features such as password hashing, session-based authentication, protected routes, admin access control, duplicate email validation, and rejection of invalid login credentials.

## Limitations

- The system uses SQLite, which is suitable for a small academic project.
- Search functionality mainly focuses on location.
- Online booking and payment are not included.
- Authentication and security features are basic.
- Automated testing mainly focuses on functional behavior and access control.

## Future Improvements

Possible improvements include advanced search filters, accommodation image uploads, user reviews and ratings, online booking, real-time availability, email notifications, and additional security testing.

## Learning Outcomes

Through this project, we gained practical experience in Flask development, database management, authentication, automated browser testing, test case execution, debugging, and software quality assurance.

## Conclusion

BashaShareBD provides a simple solution for sharing and searching accommodation information. By combining web development with Selenium and pytest, the project demonstrates the importance of functional testing and access control in software quality assurance. It also provides practical experience in developing, testing, and improving a web application as part of an undergraduate SQT project.
