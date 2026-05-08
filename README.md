# Project 3: Audio Analyzer DevOps Lifecycle (INTERACTIVE CHALLENGE) 🚀

This project is a full-stack application for audio analysis. **Note:** The infrastructure files (Docker, Compose, Jenkins) have been removed. Your task is to create them from scratch using the hints provided below.

## 📁 Current Structure
- `backend/main.py`: The FastAPI application.
- `backend/requirements.txt`: Dependencies.
- `frontend/index.html`: The Web UI.

---

## 🛠️ The Challenge: Implement the DevOps Lifecycle

### 1. Create Backend Dockerfile (`backend/Dockerfile`)
**Hints:**
- Start with a `python:3.9-slim` base image.
- **Crucial:** You must install `ffmpeg` and `libsndfile1` using `apt-get` or the analysis will fail.
- Remember to `pip install` the requirements.
- The app runs on port `8000`.

### 2. Create Frontend Dockerfile (`frontend/Dockerfile`)
**Hints:**
- Use an `nginx:alpine` image.
- Where does Nginx expect HTML files to be located? (`/usr/share/nginx/html/`)
- Just copy the `index.html` there.

### 3. Create Multi-Container Orchestration (`docker-compose.yml`)
**Hints:**
- Define two services: `backend` and `frontend`.
- Map ports so you can access them from your browser.
- Use `depends_on` to ensure the backend is ready before the frontend.
- Create a custom bridge network for them to talk to each other.

### 4. Create the CI/CD Pipeline (`Jenkinsfile`)
**Hints:**
- Use a `pipeline { agent any }` block.
- **Stage 1 (Build):** Use the `docker build` command for both images.
- **Stage 2 (Push):** How do you handle `docker login` and `docker push`? (Think about credentials).
- **Stage 3 (Deploy):** Use `docker-compose up -d` to finish the job.

---

## 🎯 Interview Focus Points
- **Layer Caching:** How can you optimize the `backend/Dockerfile` so it doesn't re-install dependencies every time you change a line of code?
- **Security:** Should the container run as `root`? How do you fix that?
- **Networking:** How does the frontend `fetch()` call know where to find the backend container?

*This project is now a workbook for your DevOps Interview preparation.*
