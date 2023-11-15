# Small Demo of Python Server

## Overview
This project showcases a simple Python server implemented with **FastAPI**, designed to handle CRUD requests. The server leverages the power of **pydantic** for creating a robust Event model. This choice not only facilitates smooth interactions with the API but also ensures that invalid objects trigger appropriate error responses, gracefully aborting the request.

## Features
**FastAPI**: The server is built on the FastAPI framework, providing a high-performance and easy-to-use platform for web development.

**pydantic**: Utilized for crafting the Event model, pydantic enhances data validation and promotes structured interactions between the client and the API.

## WeatherAPI Integration: 
The server mimics WeatherAPI functionality with a mock implementation that randomly selects forecasts. With minimal modifications to the service and the addition of an API request, third-party integration with a real WeatherAPI can be easily incorporated.

## Database
The project incorporates services to seamlessly interact with the database. In its current state, a json file (db.json) serves as the database. However, extending support to a SQL server with ODBC Driver is straightforward.

## Testing
A comprehensive test file is included, leveraging fastapi.testclient and designed to be run with Pytest. This ensures robust testing of the server's functionality.
