from flask import Flask, jsonify
from flasgger import Swagger
from app.utils.config import Config

# blueprints here
from app.controllers.Todo import todo_bp

app = Flask(__name__)

app.config["SWAGGER"] = Config.get_swagger_config()
swagger = Swagger(app, template=Config.template)

# reg blueprints here
app.register_blueprint(todo_bp, url_prefix="/todo")


@app.route("/")
def index():
    return jsonify("hello!")


if __name__ == "__main__":
    app.run(debug=True)
