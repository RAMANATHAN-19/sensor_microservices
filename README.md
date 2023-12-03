# Sensor_microservices

A web application project with microservices architecture for sensor integration and data processing.

## Table of Contents

- [Microservices Architecture](#microservices-architecture)
- [Components](#components)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Dockerization](#dockerization)
- [Deployment](#deployment)
- [Scalability and Fault Tolerance](#scalability-and-fault-tolerance)
- [Contributing](#contributing)
- [License](#license)

## Microservices Architecture

The project follows a microservices architecture consisting of the following components:

- **Sensor Integration Service**
- **Data Processing Service**
- **Web Application Backend**
- **Angular Frontend (Dashboard)**

For detailed information about each microservice and their interactions, refer to the [Microservices Architecture documentation](docs/microservices_architecture.md).

## Components

1. **Sensor Integration Service:**
   - Integrates data from different sensors.
   - API Endpoint: `/sensor-data`

2. **Data Processing Service:**
   - Processes data based on sensor types.
   - API Endpoint: `/process-data`

3. **Web Application Backend:**
   - Serves as the backend for the Angular frontend.
   - API Endpoint: `/get-sensor-data`

4. **Angular Frontend (Dashboard):**
   - Displays dummy values of temperature, motion, and humidity.
   - Integrates with microservices through REST API services.

For detailed information about each component, refer to the documentation in the 'docs/' directory.

## Technology Stack

- **Backend:** Django
- **Frontend:** Angular
- **Containerization:** Docker
- **Orchestration:** Docker Compose

## Getting Started

### Prerequisites

- Docker installed on your machine.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/RAMANATHAN-19/sensor_microservices.git
## Deployment

To deploy this project run

1. Change your working directory:

```bash
  cd sensor_microservices
```

2.Build Docker containers:
```bash
  docker-compose build
```
3.Start the application:
```bash
  docker-compose up
```


## Usage

Access the Angular frontend at http://localhost:
Dockerization
The project uses Docker for containerization. Each microservice has its own Dockerfile for easy deployment. For more information, refer to the Dockerization documentation.

Deployment:

Instructions for deploying and scaling the Dockerized services can be found in the Deployment and Scaling documentation.

Scalability and Fault Tolerance:

The microservices architecture is designed for scalability and fault tolerance. For detailed information, refer to the Scalability and Fault Tolerance documentation.

Contributing:

If you would like to contribute to the project, please follow the guidelines outlined in the CONTRIBUTING.md file.
