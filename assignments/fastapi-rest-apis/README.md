# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using the FastAPI framework by creating endpoints that create, read, update, and delete task records.

## 📝 Tasks

### 🛠️ Set Up the FastAPI Application

#### Description
Prepare the starter project and run a FastAPI application locally.

#### Requirements
Completed program should:

- Install the packages listed in `requirements.txt`.
- Create a FastAPI application named `app`.
- Provide a root endpoint that returns a welcome message.
- Start the server with `uvicorn` and open the interactive documentation at `/docs`.

Example root response:

```json
{"message":"Welcome to the Task API"}
```

### 🛠️ Return Task Resources

#### Description
Create endpoints that return task data from an in-memory collection.

#### Requirements
Completed program should:

- Provide a `GET /tasks` endpoint that returns all tasks.
- Provide a `GET /tasks/{task_id}` endpoint that returns one task.
- Return an HTTP 404 response when the requested task does not exist.
- Use a task ID integer for the path parameter.

Example response:

```json
{"id":1,"title":"Study FastAPI","completed":false}
```

### 🛠️ Create and Update Tasks

#### Description
Accept task data from API request bodies and update the in-memory collection.

#### Requirements
Completed program should:

- Define a Pydantic model for creating a task.
- Provide a `POST /tasks` endpoint that creates and returns a task.
- Assign a new integer ID to each created task.
- Provide a `PUT /tasks/{task_id}` endpoint that updates an existing task.
- Return an HTTP 404 response when the task to update does not exist.

Example request body:

```json
{"title":"Submit the API project","completed":false}
```

### 🛠️ Delete Tasks

#### Description
Complete the API by removing tasks and confirming when they were deleted.

#### Requirements
Completed program should:

- Provide a `DELETE /tasks/{task_id}` endpoint.
- Remove the matching task from the in-memory collection.
- Return the deleted task in the response.
- Return an HTTP 404 response when the task does not exist.
