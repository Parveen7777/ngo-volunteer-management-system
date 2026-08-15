# NGO Volunteer Management System Architecture

## Overview

The NGO Volunteer Management System is built using a layered architecture with Flask, SQLite, and Docker.

## Architecture Diagram

User (Browser)
|
v
Flask Routes (Presentation Layer)
|
v
Services (Business Logic Layer)
|
v
Models (Data Access Layer)
|
v
SQLite Database

## Components

### Presentation Layer

* Login page
* Dashboard
* Volunteer management
* Event management
* Attendance management
* Reports

### Business Logic Layer

* Authentication
* Volunteer operations
* Event operations
* Attendance processing
* Report generation

### Data Layer

* Users table
* Volunteers table
* Events table
* Attendance table

## Security

* Session-based authentication
* Input validation
* Database parameterized queries
* Docker container isolation

## Technologies

* Python 3.11
* Flask
* SQLite
* Docker
* HTML/CSS/JavaScript
