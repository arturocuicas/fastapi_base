# FastAPI Base Project

## Description
This is a base project using FastAPI, a modern and fast web framework for building APIs with Python 3.7+ based on standards like OpenAPI and JSON Schema. The project uses Poetry for package management.

## Requirements
- Python 3.7+
- FastAPI
- Uvicorn
- Poetry

## Installation
1. Clone the repository:
    ```bash
    git clone git@github.com:arturocuicas/fastapi_base.git
    cd fastapi_base
    ```

2. Install Poetry if you don't have it installed:
    ```bash
    pip install poetry
    ```

3. Install the dependencies:
    ```bash
    poetry install
    ```

## Usage
To start the development server, run:
    ```bash
    poetry run uvicorn main:app --reload
    ```
This will start the server at `http://127.0.0.1:8000`.

## Contribution
1. Fork the project.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push your changes (`git push origin feature/new-feature`).
5. Open a Pull Request.

## License
This project is licensed under the terms of the MIT license.
