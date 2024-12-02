# Azure Database Connector Web App

This is a simple web app built with Flask (Python) to connect and interact with an Azure SQL database. The app provides a user-friendly interface for inputting database credentials and testing connections, designed to be mobile-friendly.

## Features

- User-friendly form for entering:
  - Server Name
  - Database Name
  - Username
  - Password
- Connects securely to an Azure SQL database using `pyodbc`.
- Load default credentials from a JSON file (`azure_credentials.json`).
- Responsive design for mobile and desktop users.
- Button to open a SQL client for managing the database.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, Bootstrap 5
- **Database**: Azure SQL
- **Dependency Management**: `pip`

## Prerequisites

- Azure SQL Database configured and running.
- Azure App Service created (if hosting on Azure).
- Python installed (recommended version: 3.12).
- Git installed for version control.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repository>.git
   cd <your-repository>
