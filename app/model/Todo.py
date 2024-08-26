from bson.objectid import ObjectId
from app.connection.connection import MongoDBConnector


class Todo:
    def __init__(self) -> None:
        self.db = MongoDBConnector().get_db()
        self.collection = self.db.todo

    # utility function
    def create_todo(self, title, description):
        todo = {"title": title, "description": description, "completed": False}
        result = self.collection.insert_one(todo)
        return str(result.inserted_id)

    def get_all_todos(self):
        todos = self.collection.find()
        return list(todos)

    def get_todo_by_id(self, todo_id):
        if not self.is_valid_objectid(todo_id):
            return None
        todo = self.collection.find_one({"_id": ObjectId(todo_id)})
        return todo

    def update_todo(self, todo_id, title=None, description=None, completed=None):
        if not self.is_valid_objectid(todo_id):
            return None
        update_fields = {}
        if title:
            update_fields["title"] = title
        if description:
            update_fields["description"] = description
        if completed is not None:
            update_fields["completed"] = completed
        result = self.collection.update_one(
            {"_id": ObjectId(todo_id)}, {"$set": update_fields}
        )
        return result.modified_count

    def delete_todo(self, todo_id):
        if not self.is_valid_objectid(todo_id):
            return 0
        result = self.collection.delete_one({"_id": ObjectId(todo_id)})
        return result.deleted_count

    def is_valid_objectid(self, object_id):
        try:
            ObjectId(object_id)
            return True
        except:
            return False

    def to_json(self, data):
        if isinstance(data, list):
            for item in data:
                item["_id"] = str(item["_id"])
        elif isinstance(data, dict):
            data["_id"] = str(data["_id"])
        return data
