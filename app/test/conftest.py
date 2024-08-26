import pytest
import sys
import os

# Add the root directory (the parent directory of `app`) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from index import app  # Now this should work


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
