from typing import Literal
from flask import Blueprint, request, jsonify
from flask.wrappers import Response
from app.model.Todo import Todo
from flasgger.utils import swag_from

todo_bp = Blueprint("todos", __name__)
todo_model = Todo()


# CLASSIC CRUD ..
# Route for getting all todos
@todo_bp.route("", methods=["GET"])
@swag_from("../docs/todo/get_todos.yaml", methods=["GET"])
def get_todos():
    todos = todo_model.get_all_todos()
    clean_todos = [todo_model.to_json(todo) for todo in todos]
    return jsonify(clean_todos), 200


# Route for getting a specific todo by ID
@todo_bp.route("/<string:todo_id>", methods=["GET"])
@swag_from("../docs/todo/get_todo_by_id.yaml", methods=["GET"])
def get_todo(todo_id):
    todo = todo_model.get_todo_by_id(todo_id)
    if not todo:
        return jsonify({"err": "todo Not found"}), 404
    return jsonify(todo_model.to_json(todo)), 200


@todo_bp.route("", methods=["POST"])
@swag_from("../docs/todo/create_todo.yaml", methods=["POST"])
def create_todo():
    data = request.json
    title = data.get("title")
    description = data.get("description")
    if not title or not description:
        return (jsonify({"message": "fill the title and desc you stupid bitch"}), 400)
    todo_id = todo_model.create_todo(title, description)

    if todo_id:
        return jsonify({"message": f"Successfully added {title}", "id": todo_id}), 200
    else:
        return jsonify({"message": "Server error! "}), 500


@todo_bp.route("/<string:todo_id>", methods=["PUT"])
@swag_from("../docs/todo/update_todo.yaml", methods=["PUT"])
def update_todo(todo_id):
    data = request.json
    title = data.get("title")
    description = data.get("description")
    completed = data.get("completed")

    if title or description or completed is not None:
        modified_count = todo_model.update_todo(todo_id, title, description, completed)
        if modified_count:
            return jsonify({"message": f"updated no. {todo_id}"}), 200

        else:
            return jsonify({"message": "No changes made or todo not found"}), 404
    else:
        return (jsonify({"message": "You must provide  update"}), 400)


@todo_bp.route("/<string:todo_id>", methods=["DELETE"])
@swag_from("../docs/todo/delete_todo.yaml", methods=["DELETE"])
def delete_todo_route(todo_id):
    if todo_id:
        deleted_count = todo_model.delete_todo(todo_id)
        if deleted_count > 0:
            return jsonify({"message": f"Successfully deleted {todo_id}"}), 200
        else:
            return jsonify({"message": "Todo not found"}), 404
    else:
        return jsonify({"message": "Invalid ID provided"}), 400
