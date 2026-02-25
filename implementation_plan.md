# Microservices & DevOps Learning Project: Implementation Plan

Welcome! This plan is designed to take you from a beginner level to a practical understanding of Microservices and DevOps by building a simple, yet comprehensive system. 

We will build a **Task Management System** consisting of two backend services, a frontend, and a full suite of DevOps tools.

## Project Architecture Overview
- **Frontend**: SvelteKit (Modern UI)
- **API Gateway**: Kong (Route management, Auth)
- **Service A (Task Service)**: Python (FastAPI) + MongoDB (Task storage)
- **Service B (Notification Service)**: Python + Redis (Async worker for notifications)
- **Communication**: 
    - REST (Sync) for internal service requests.
    - Redis (Async) for message queuing.
- **Monitoring**: Prometheus, Grafana, Loki (The "LGP" stack)
- **Infrastructure**: Docker & Docker Compose

---

## Phase 1: Foundation & Local Environment
*Goal: Set up the project structure and shared infrastructure.*

### Step 1.1: Project Initialization
- Create the project folder structure.
- Initialize a Git repository.
- Create a `docker-compose.yml` for shared services (MongoDB, Redis).

### Step 1.2: Base Infrastructure
- Deploy MongoDB and Redis using Docker.
- Verify connectivity using simple scripts.

---

## Phase 2: Service A - The "Task Service" (Sync Microservice)
*Goal: Build your first microservice with a database.*

### Step 2.1: FastAPI Setup
- Create a Python FastAPI application.
- Implement CRUD (Create, Read, Update, Delete) operations for "Tasks".
- Connect to MongoDB using an ODM like `Beanie` or `Motor`.

### Step 2.2: Dockerization
- Create a `Dockerfile` for Service A.
- Add it to `docker-compose.yml`.

---

## Phase 3: Service B - The "Notification Service" (Async Microservice)
*Goal: Learn asynchronous communication using a message queue.*

### Step 3.1: Redis Worker
- Create a second Python service.
- Implement a Redis-based message consumer (worker) that listens for "Task Created" events.
- Simulate sending a notification (e.g., logging to console).

### Step 3.2: Async Integration
- Update Service A to push a message to Redis whenever a task is created.
- Test the flow: Service A -> Redis -> Service B.

---

## Phase 4: API Gateway - Kong
*Goal: Centralize your API access point.*

### Step 4.1: Kong Setup
- Add Kong (and its database, PostgreSQL) to `docker-compose.yml`.
- Configure Kong to route traffic to Service A.

### Step 4.2: Gateway Features
- Learn how to use Kong for simple routing and potentially adding a plugin (like rate limiting).

---

## Phase 5: Frontend - SvelteKit
*Goal: Create a user interface to interact with the system.*

### Step 5.1: SvelteKit Initialization
- Set up a SvelteKit project.
- Build a dashboard to view tasks and a form to create tasks.

### Step 5.2: Connecting to the Gateway
- Make API calls from SvelteKit to Service A *through* the Kong API Gateway.

---

## Phase 6: Monitoring & Observability
*Goal: Visualize what's happening in your system.*

### Step 6.1: Metrics with Prometheus & Grafana
- Instrument Service A to expose metrics.
- Set up Prometheus to scrape those metrics.
- Create a Grafana dashboard to visualize request rates and errors.

### Step 6.2: Logs with Loki
- Configure Docker to send logs to Loki.
- View application logs directly in Grafana alongside your metrics.

---

## Phase 7: Advanced Concepts (Optional/Next Steps)
*Goal: Broaden your DevOps knowledge.*

### Step 7.1: CI/CD Pipeline
- Create a GitHub Action to build Docker images and run linting.

### Step 7.2: Service Discovery & Health Checks
- Implement proper health check endpoints in your microservices.

---

## How to use this plan
We will go through these steps one by one. I will provide the code and explain the concepts behind each line so you can learn while you build.

**Ready to start with Unit 1?**
