# IoT Device Monitoring System

## Overview

This project is a Django-based IoT device monitoring system that allows you to manage IoT devices, record temperature and humidity readings, and visualize the data through a graphical interface.

## Features

- **Create Device:** Add a new IoT device with a unique identifier and a name.

- **Get Device:** Retrieve information about a specific IoT device using its unique identifier.

- **Reading View:** Get temperature or humidity readings for a specific device within a specified time range.

- **Device Graph View:** Visualize temperature and humidity vs time for a specific device.

## Project Structure

- **models.py:** Defines the database models for Device, TemperatureReading, and HumidityReading.

- **serializers.py:** Contains serializers for converting model instances to JSON.

- **views.py:** Implements view functions for API endpoints and rendering the graphical interface.

- **urls.py:** Configures URL patterns for different views.

- **templates/:** Contains HTML templates, including `home.html` for API documentation and `graph.html` for device graphs.

## Setup

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run migrations:

    ```bash
    python manage.py migrate
    ```

3. Create a superuser (for admin access):

    ```bash
    python manage.py createsuperuser
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

5. Access the admin panel at http://localhost:8000/admin/ to manage devices and readings.

## Usage

- API Endpoints:
  - Create Device: POST /api/devices/
  - Get Device: GET /api/devices/<str:uid>/
  - Reading View: GET /api/devices/<str:uid>/readings/<str:parameter>/?start_on=yyyy-mm-ddTHH:MM:SS&end_on=yyyy-mm-ddTHH:MM:SS
  - Device Graph View: GET /devices-graph/<str:uid>/

- API Documentation:
  - Access the API documentation at http://localhost:8000/ for details on each endpoint.

## Dependencies

- Django
- Django Rest Framework
- Plotly (for graph visualization)

## License

This project is licensed under the [MIT License](LICENSE).
