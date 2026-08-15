# API Documentation

## Authentication

### Login

* **URL:** `/login`
* **Method:** `POST`
* **Parameters:** email, password

### Logout

* **URL:** `/logout`
* **Method:** `GET`

## Dashboard

### Dashboard

* **URL:** `/dashboard`
* **Method:** `GET`

## Volunteers

### List Volunteers

* **URL:** `/volunteers`
* **Method:** `GET`

### Add Volunteer

* **URL:** `/volunteers/add`
* **Method:** `POST`

### Delete Volunteer

* **URL:** `/volunteers/delete/<id>`
* **Method:** `GET`

## Events

### List Events

* **URL:** `/events`
* **Method:** `GET`

### Add Event

* **URL:** `/events/add`
* **Method:** `POST`

### Delete Event

* **URL:** `/events/delete/<id>`
* **Method:** `GET`

## Attendance

### Attendance Page

* **URL:** `/attendance`
* **Method:** `GET`

### Mark Attendance

* **URL:** `/attendance/mark`
* **Method:** `POST`

## Reports

### Reports Dashboard

* **URL:** `/reports`
* **Method:** `GET`

### PDF Report

* **URL:** `/reports/pdf`
* **Method:** `GET`

### CSV Export

* **URL:** `/reports/csv`
* **Method:** `GET`

### Excel Export

* **URL:** `/reports/excel`
* **Method:** `GET`
