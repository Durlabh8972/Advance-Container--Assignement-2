# Advanced Containers – Assignment 2

## 🧪 Assignment Overview

This project is developed for the **Advanced Containers** course at Conestoga College.  
The assignment demonstrates a simple Flask-based RESTful API containerized using Docker. The application supports user creation and retrieval, with persistent logging.

---

## 📦 Features Implemented

- Flask REST API with endpoints:
  - `POST /user` – Add a user
  - `GET /user/<id>` – Retrieve user by ID
- JSON-based request/response
- Logging implemented using `app.log` file
- Dockerized app with Dockerfile
- Verified using `curl` commands from terminal
- Docker image built and run locally
- Screenshots captured for each step

---

## 🔧 Technologies Used

- Python 3.x
- Flask
- Docker
- SQLite (in-memory)
- Logging
- Git & GitHub

---

## 🚀 How to Run This App (Locally)

1. **Clone this repository**
   ```bash
   git clone https://github.com/Durlabh8972/Advance-Container--Assignement-2.git
   cd Advance-Container--Assignement-2
Build the Docker image

bash
Copy
Edit
docker build -t flask-user-api .
Run the Docker container

bash
Copy
Edit
docker run -d -p 5000:5000 flask-user-api
Test the API using curl

bash
Copy
Edit
curl -X POST http://localhost:5000/user -H "Content-Type: application/json" -d "{\"first_name\": \"Durlabh\", \"last_name\": \"Tilavat\"}"
curl http://localhost:5000/user/1
📸 Screenshots Included
Docker build and run terminal

Successful curl requests

App running in browser (http://localhost:5000/user/1)

Files in GitHub repository

app.log file verification

📁 File Structure
bash
Copy
Edit
├── app.py               # Main Flask application
├── Dockerfile           # Docker build instructions
├── requirements.txt     # Python dependencies
├── app.log              # Log file (created on run)
├── README.md            # Assignment documentation

👨‍💻 Developed By
Durlabh Tilavat
Conestoga College – Cloud Development and Operations
Student ID: 8938972
