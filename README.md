# Treehopper Colony's Task Reminder System

[![.github/workflows/web-app-ci.yml](https://github.com/swe-students-spring2026/5-final-treehopper_colony/actions/workflows/web-app-ci.yml/badge.svg)](https://github.com/swe-students-spring2026/5-final-treehopper_colony/actions/workflows/web-app-ci.yml)

[![.github/workflows/reminder-worker.yml](https://github.com/swe-students-spring2026/5-final-treehopper_colony/actions/workflows/reminder-worker.yml/badge.svg)](https://github.com/swe-students-spring2026/5-final-treehopper_colony/actions/workflows/reminder-worker.yml)

## Description

A task reminder platform that allows users to register, login, create tasks, and delete tasks. Users are able to set reminders for their tasks, which will be sent to the user's email. 

## Live Application
[Treehopper Colony's Task Reminder System](https://web-service-production-f61d.up.railway.app/)

## Team

- [Diya Greben](https://github.com/diyagreben)
- [Carolina Lee](https://github.com/CarolLee04)
- [Jeffrey Solano](https://github.com/jeffnoso)
- [Uwa Igbinedion](https://github.com/uwa00)
- [Ed Ye](https://github.com/EdwarddYe)

## Features

- **Web App**: User-friendly interface for creating, managing, and viewing tasks with reminder settings.
- **Reminder Worker**: Automated background service that sends reminders based on task schedules.
- **MongoDB Integration**: Persistent storage for users, tasks, and reminder data.
- **Docker Compose Integration**: Multi-container orchestration for MongoDB, web app, and reminder worker services.
- **Email Notifications**: Automated Gmail-based reminder delivery system.

## Docker Hub Links

- [Web App](https://hub.docker.com/repository/docker/csl9997/reminder-web/general)
- [Reminder Worker](https://hub.docker.com/repository/docker/csl9997/reminder-worker/general)

## Run with Docker Compose

From the project root:

```bash
docker compose up --build
```
The web app will be available at:

```text
http://localhost:5004
```

## Local Development Setup

### Prerequisites

- Python 3.11
- Docker
- MongoDB (local or Docker)

### 1. Clone the Repository

### 2. Set Up MongoDB

Run MongoDB locally or via Docker:

```bash
docker run -d --name treehopper-mongo -p 27017:27017 mongo:7
```

### 3. Configure Environment Variables

Navigate to the `web_app` directory.

Duplicate the `env.example` file and rename the copy to exactly `.env`

Ensure the `.env` file contains the following local database configuration:

   ```text
   MONGO_URI=mongodb://localhost:27017
   DB_NAME=task_reminder_db
   SECRET_KEY=your-secret-key
   ```

For the reminder worker:

Navigate to the `reminder_worker` directory.

Duplicate the `env.example` file and rename the copy to exactly `.env`

Ensure the `.env` file contains the following local database configuration:

   ```text
   MONGO_URI=mongodb://mongodb:27017
   DB_NAME=task_reminder_db
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USER=your_email@gmail.com
   SMTP_PASS=your_app_password_here
   ```

### 4. Run Locally

#### Web App
Open a terminal and run:
```bash
cd web_app
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5004`

#### Reminder Worker
Open a new terminal and run:

```bash
cd reminder_worker
pip install -r requirements.txt
python worker.py
```
