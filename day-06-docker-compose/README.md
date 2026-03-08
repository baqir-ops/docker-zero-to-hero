# Docker Compose Multi-Container Application (Nginx + Flask + MySQL)

## Project Overview

This project demonstrates how to run a **multi-container application** using Docker Compose.

The application architecture includes three containers:

* **Nginx** – Reverse proxy web server
* **Flask App** – Backend application
* **MySQL** – Database server

All containers communicate through a **Docker network** created automatically by Docker Compose.

---

## Architecture

```
Browser
   │
   ▼
localhost:8080
   │
   ▼
Nginx (Reverse Proxy)
   │
   ▼
Flask Application
   │
   ▼
MySQL Database
```

---

## Project Structure

```
day-06-docker-compose
│
├── docker-compose.yml
├── nginx
│   └── default.conf
├── screenshots
│
└── README.md
```

---

## Technologies Used

* Docker
* Docker Compose
* Nginx
* Flask
* MySQL

---

## Services

### Nginx

Acts as a **reverse proxy** that forwards HTTP requests to the Flask application.

Port exposed:

```
8080 → 80
```

Configuration file:

```
nginx/default.conf
```

---

### Flask Application

A simple Flask container that returns a response:

```
Hello from Docker! Built by baqir-ops
```

---

### MySQL Database

Runs inside a container and is used by the application backend.

Environment variable used:

```
MYSQL_ROOT_PASSWORD=root
```

---

## Running the Project

Start the containers:

```
docker compose up -d
```

Check running containers:

```
docker ps
```

Stop the containers:

```
docker compose down
```

---

## Docker Network

Docker Compose automatically creates a network for communication between containers.

Example command:

```
docker network inspect day-06-docker-compose_appnet
```

This network allows containers to communicate using service names like:

```
flask-app
mysql-db
```

---

## Screenshots

### Running Containers

![Running Containers](screenshots/running-containers.png)

### Docker Compose Start

![Docker Compose Start](screenshots/docker-compose-start.png)

### Docker Network

![Docker Network](screenshots/docker-network.png)

### Network Inspect

![Network Inspect](screenshots/network-inspect.png)

### Application Running in Browser

![App Running](screenshots/app-running-browser.png)

---

## DevOps Concepts Practiced

* Containerization using Docker
* Multi-container orchestration using Docker Compose
* Reverse proxy configuration with Nginx
* Container networking
* Infrastructure as Code (YAML)

---

## Author

**Muhammad Baqir Nawaz **

DevOps & Cloud Engineering Learning Journey
