from flask import Blueprint, request, jsonify
from app.model.Todo import Todo
from flasgger.utils import swag_from

todo_bp = Blueprint("todos", __name__)
todo_model = Todo()


# Route for getting all todos
@todo_bp.route("", methods=["GET"])
@swag_from(r"docs/todo.yaml", endpoint="paths./todo.get", methods=["GET"])
def get_todos():
    todos = todo_model.get_all_todos()
    return jsonify(todo_model.to_json(todos)), 200


# Route for getting a specific todo by ID
@todo_bp.route("/<string:todo_id>", methods=["GET"])
@swag_from(r"docs/todo.yaml", endpoint="paths./todo/{todo_id}.get", methods=["GET"])
def get_todo(todo_id):
    todo = todo_model.get_todo_by_id(todo_id)
    if not todo:
        return jsonify({"err": "todo Not found"}), 404
    return jsonify(todo_model.to_json(todo)), 200
