# Deployment Guide

## Local Deployment

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Initialize Database

```bash
python database/schema.py
python database/seed.py
```

### Run Application

```bash
python app.py
```

Open: `http://localhost:5000`

## Docker Deployment

### Build Containers

```bash
docker-compose build
```

### Start Application

```bash
docker-compose up
```

### Stop Application

```bash
docker-compose down
```

## Project Structure

* `app.py` – Flask application
* `routes/` – Route handlers
* `services/` – Business logic
* `models/` – Database models
* `database/` – SQLite database
* `templates/` – HTML templates
* `static/` – CSS, JS, images
* `docker/` – Docker configuration
* `reports/` – PDF, CSV, Excel exports

## Default Admin Login

* **Email:** [admin@ngo.org](mailto:admin@ngo.org)
* **Password:** admin123

## Docker Ports

* Flask: 5000
* Nginx: 80
