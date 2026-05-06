# Treehopper Colony Task Reminder System

[![.github/workflows/web-app-ci.yml](https://github.com/swe-students-spring2026/5-final-treehopper_colony/actions/workflows/web-app-ci.yml/badge.svg)](https://github.com/swe-students-spring2026/5-final-treehopper_colony/actions/workflows/web-app-ci.yml)

[![.github/workflows/reminder-worker.yml](https://github.com/swe-students-spring2026/5-final-treehopper_colony/actions/workflows/reminder-worker.yml/badge.svg)](https://github.com/swe-students-spring2026/5-final-treehopper_colony/actions/workflows/reminder-worker.yml)

## Description

A task reminder platform that allows users to register, login, create tasks, and delete tasks. Users are able to set reminders for their tasks, which will be sent to the user's email. 

## Team

- [Diya Greben](https://github.com/diyagreben)
- [Carolina Lee](https://github.com/CarolLee04)
- [Jeffrey Solano](https://github.com/jeffnoso)
- [Uwa Igbinedion](https://github.com/uwa00)

## Features

- **Web App**: User-friendly interface for creating, managing, and viewing tasks with reminder settings.
- **Reminder Worker**: Automated background service that sends reminders based on task schedules.
- **MongoDB Integration**: Persistent storage for users, tasks, and reminder data.

## Docker Hub Links (PLACEHOLDER)

- [Web App](https://hub.docker.com/repository/docker/csl9997/reminder-web/general)
- [Reminder Worker](https://hub.docker.com/repository/docker/csl9997/reminder-worker/general)

## Local Development Setup

### Prerequisites

- Python 3.11
- Docker
- MongoDB (local or Docker)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/treehopper_colony.git
cd treehopper_colony
```

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
   ```

For the reminder worker:

Navigate to the `reminder_worker` directory.

Duplicate the `env.example` file and rename the copy to exactly `.env`

Ensure the `.env` file contains the following local database configuration:

   ```text
   MONGO_URI=mongodb://localhost:27017
   DB_NAME=task_reminder_db
   SECRET_KEY=your-secret-key
   ```

### 4. Run Locally

#### Web App

```bash
cd web_app
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5004`

#### Reminder Worker

```bash
cd reminder_worker
pip install -r requirements.txt
python -c "from reminder_service import process_due_reminders; from db import get_tasks_collection; process_due_reminders(get_tasks_collection(), lambda e,t,w: print(f'Send to {e}: {t}'))"
```

### 5. Run with Docker

#### Web App

```bash
cd web_app
docker build -t treehopper-web-app .
docker run -p 5004:5004 -e MONGO_URI=mongodb://host.docker.internal:27017 -e DB_NAME=task_reminder_db -e SECRET_KEY=secret treehopper-web-app
```

#### Reminder Worker

```bash
cd reminder_worker
docker build -t treehopper-reminder-worker .
docker run -e MONGO_URI=mongodb://host.docker.internal:27017 -e DB_NAME=task_reminder_db treehopper-reminder-worker
```