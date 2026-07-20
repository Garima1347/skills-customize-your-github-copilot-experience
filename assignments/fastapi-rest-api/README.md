# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn the fundamentals of building a REST API with FastAPI by creating endpoints for managing a simple collection of items. Students will practice routing, request validation, and JSON responses.

## 📝 Tasks

### 🛠️ Create a FastAPI App

#### Description
Create a new FastAPI application that serves a simple API for managing items.

#### Requirements
Completed program should:

- Import and initialize a FastAPI app instance
- Provide a root endpoint that returns a welcome message
- Run successfully with Uvicorn or another local server

### 🛠️ Build CRUD Endpoints

#### Description
Implement endpoints to create, read, update, and delete items in memory.

#### Requirements
Completed program should:

- Create a `GET /items` endpoint that returns all items
- Create a `POST /items` endpoint that adds a new item
- Create a `GET /items/{item_id}` endpoint that returns one item by ID
- Create a `PUT /items/{item_id}` endpoint that updates an existing item
- Create a `DELETE /items/{item_id}` endpoint that removes an item

### 🛠️ Validate Data with Pydantic Models

#### Description
Use Pydantic models to define the shape of incoming and outgoing data.

#### Requirements
Completed program should:

- Define an item schema with fields such as `name`, `description`, and `price`
- Ensure invalid payloads are rejected with appropriate validation errors
- Return JSON responses that clearly describe created, updated, or deleted items
