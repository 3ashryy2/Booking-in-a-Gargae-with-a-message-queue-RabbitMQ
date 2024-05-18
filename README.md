# Booking Garage Spot using RabbitMQ
 
Welcome to our microservices project! This project consists of three microservices: Booking, Garage Management, and Notification. Each microservice handles specific functionalities and communicates with others through HTTP requests or message queues.

## Installation and Setup

### Prerequisites
- Python 3.11.6
- Django
- Django REST Framework
- RabbitMQ (for message queue)

### Installation
1. Clone this repository to your local machine.
2. Install dependencies for each microservice using pip:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up RabbitMQ for message queue communication between microservices.
4. Migrate databases for each microservice:
    ```bash
    python manage.py migrate
    ```

## Microservices Overview

### 1. Booking Microservice
- Manages booking requests from clients.
- Provides endpoints for creating, updating, and viewing bookings.
- Communicates with the Garage Management microservice to check garage availability and confirm bookings.
- Sends notifications to clients and garage owners via the Notification microservice.

### 2. Garage Management Microservice
- Manages garages and their availability.
- Provides endpoints for adding, updating, and viewing garage information.
- Receives booking requests from the Booking microservice and confirms availability.
- Sends availability updates to the Booking microservice.

### 3. Notification Microservice
- Handles sending notifications to clients and garage owners.
- Provides an endpoint for sending notifications via FCM (Firebase Cloud Messaging).
- Receives notification requests from the Booking microservice and sends notifications accordingly.

## Interconnection
- **Booking Microservice to Garage Management Microservice:** Booking microservice sends booking requests to Garage Management microservice to check availability and confirm bookings.
- **Garage Management Microservice to Booking Microservice:** Garage Management microservice sends availability updates to Booking microservice after receiving booking requests.
- **Booking Microservice to Notification Microservice:** Booking microservice sends notification requests to Notification microservice for sending notifications to clients and garage owners.
- **Notification Microservice to Clients and Garage Owners:** Notification microservice sends notifications to clients and garage owners based on requests received from the Booking microservice.

## Usage

### 1. Booking Microservice Endpoints
- **Create Booking:** POST `/bookings/`
- **Update Booking:** PUT `/bookings/{id}/`
- **View Booking:** GET `/bookings/{id}/`

### 2. Garage Management Microservice Endpoints
- **Add Garage:** POST `/garages/`
- **Update Garage:** PUT `/garages/{id}/`
- **View Garage:** GET `/garages/{id}/`

### 3. Notification Microservice Endpoint
- **Send Notification:** POST `/send-notification/`

Refer to the API documentation or Swagger UI for detailed information on each endpoint and request/response formats.

## Contributing
Contributions are welcome! Please follow the standard contribution guidelines and code of conduct.


