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

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": "apispec_1",
                "route": "/apispec_1.json",
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
                "specs_route": "/apidocs/",
            }
        ],
        "swagger_ui": True,
        "specs_format": "yaml",
        "openapi": "3.0.0",  # Specify OpenAPI version here
    }
