

# Password Reset Feature for Django App

## Overview
This project extends the existing Django application by implementing a password reset feature for registered users. It also improves the security and organization of the application by using environment variables stored in a `.env` file for configuration settings.

## Features
- **Password Reset Mechanism**:
  - Allows registered users to reset their passwords.
  - Includes email-based password reset links.
- **Environment Variable Management**:
  - Configuration settings are managed via environment variables.
  - Utilizes a `.env` file for storing sensitive data.

## Technical Details
- **Password Reset Process**:
  - Integration with Django's built-in password reset views and URLs.
  - Email delivery of password reset links to users.
- **Environment Variables**:
  - Use of a `.env` file to store variables like secret key, database credentials, and email settings.
  - Environment variables are accessed in `settings.py`.

## Usage
- **Initiating Password Reset**:
  - Users can request a password reset from the login page.
  - A password reset link is sent to the user's registered email.
- **Resetting Password**:
  - Users follow the link in their email to set a new password.

## Installation and Dependencies
- Clone the repository.
- Requires Python, Django, and any additional libraries for handling emails and environment variables (e.g., `python-decouple` or `django-environ`).
- Set up a `.env` file with necessary environment variables.
