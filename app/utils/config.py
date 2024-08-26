import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    USERNAME = os.getenv("SERVER_USERNAME")
    PASSWORD = os.getenv("SERVER_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    CLUSTER_NAME = os.getenv("CLUSTER_NAME")
    # Create URI
    DB_URI = f"mongodb+srv://{USERNAME}:{PASSWORD}@{CLUSTER_NAME}.lmhro.mongodb.net/{DB_NAME}?retryWrites=true&w=majority&appName={DB_NAME}"

    @staticmethod
    def get_swagger_config():
        return {
            "title": "flask-mongodb mongo with MVC pattern ",
            "uiversion": 3,
            "description": "todo app ",
            "version": "1.0.0",
            "termsOfService": "tos-tos-tos",
            "contact": {
                "name": "wicaksonolxn",
                "email": "wicaksonolxn@gmail.com",
            },
            "license": {
                "name": "MIT License",
                "url": "https://opensource.org/licenses/MIT",
            },
            "host": "localhost:5000",
            "basePath": "/",
            "schemes": ["http", "https"],
            "operationId": "getmyData",
            "produces": ["application/json"],
            "consumes": ["application/json"],
        }

    @staticmethod
    def template():
        return {
            "swagger": "2.0",  # You can set it to "3.0.0" for OpenAPI 3.0
            "info": {
                "title": "flask-mongodb mongo with MVC pattern ",
                "description": "This is a sample todo app using Flask with MongoDB and MVC pattern.",
                "version": "1.0.0",
                "termsOfService": "tos-tos-tos",
                "contact": {
                    "name": "wicaksonolxn",
                    "url": "https://example.com/contact",
                    "email": "wicaksonolxn@gmail.com",
                },
                "license": {
                    "name": "MIT License",
                    "url": "https://opensource.org/licenses/MIT",
                },
            },
            "host": "localhost:5000",  # Your application's host
            "basePath": "/",  # Base path for the API
            "schemes": ["http", "https"],  # Supported schemes
            "paths": {},  # Placeholder for paths, usually filled by Flasgger
            "definitions": {},  # Placeholder for model definitions
            "securityDefinitions": {
                "Bearer": {
                    "type": "apiKey",
                    "name": "Authorization",
                    "in": "header",
                }
            },
            "security": [{"Bearer": []}],
            "tags": [
                {"name": "todos", "description": "Operations related to todo items"}
            ],
        }
