# AI-Powered Chat Application

## Overview

This project is an AI-powered Chat application. It leverages advanced language models and vector databases to provide intelligent document management, search capabilities, and interactive chat functionalities.

## Features

- **AI Chat**: Engage in conversations with an AI agent powered by state-of-the-art language models.
- **Document Management**: Add and search documents within the CRM system.
- **Intent Classification**: Automatically classify user intents for more accurate responses.
- **SQL Integration**: Utilize an SQL agent for database operations.

## Tech Stack

- **Backend**: Python with FastAPI
- **AI/ML**: Custom LLM integration
- **Vector Database**: Qdrant for efficient similarity search
- **Containerization**: Docker and Docker Compose

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.11

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/filipeth/chat-ollama
   cd chat-ollama
   ```

2. Set up environment variables:
   - Modify `.env` with your specific configurations

3. Build and run the Docker containers:
   ```
   docker-compose up --build
   ```

4. Access the application at `http://localhost:8777`

## API Documentation

Once the application is running, you can access the API documentation at:
- Swagger UI: `http://localhost:8777/docs`
- ReDoc: `http://localhost:8777/redoc`

## Development

To set up a development environment:

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application in development mode:
   ```
   uvicorn main:app --reload
   ```
