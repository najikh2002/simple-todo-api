from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"id": 1, "task": "Belajar Python", "done": False},
    {"id": 2, "task": "Membuat API", "done": False},
    {"id": 3, "task": "Deploy ke Render", "done": False}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({"todos": todos})

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((item for item in todos if item["id"] == todo_id), None)
    if todo:
        return jsonify({"todo": todo})
    return jsonify({"message": "Tugas tidak ditemukan"}), 404

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    new_todo = {
        "id": len(todos) + 1,
        "task": data.get("task", ""),
        "done": False
    }
    todos.append(new_todo)
    return jsonify({"message": "Tugas berhasil ditambahkan", "todo": new_todo})

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((item for item in todos if item["id"] == todo_id), None)
    if todo:
        todo["done"] = True
        return jsonify({"message": "Status tugas berhasil diubah", "todo": todo})
    return jsonify({"message": "Tugas tidak ditemukan"}), 404

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [item for item in todos if item["id"] != todo_id]
    return jsonify({"message": "Tugas berhasil dihapus"})

if __name__ == '__main__':
    app.run(debug=True)
