
from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    conn = get_db()
    tasks = conn.execute("SELECT * FROM tasks ORDER BY id DESC").fetchall()
    conn.close()
    return jsonify([dict(task) for task in tasks])

@app.route("/api/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    title = data.get("title", "").strip()

    if not title:
        return jsonify({"error": "Title is required"}), 400

    conn = get_db()
    cursor = conn.execute(
        "INSERT INTO tasks (title) VALUES (?)", (title,)
    )
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()

    return jsonify({"id": task_id, "title": title, "completed": 0}), 201

@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    title = data.get("title", "").strip()

    if not title:
        return jsonify({"error": "Title is required"}), 400

    conn = get_db()
    cursor = conn.execute(
        "UPDATE tasks SET title=? WHERE id=?",
        (title, task_id)
    )
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({"message": "Task updated"})

@app.route("/api/tasks/<int:task_id>/complete", methods=["PATCH"])
def complete_task(task_id):
    conn = get_db()
    cursor = conn.execute("""
        UPDATE tasks
        SET completed = CASE WHEN completed = 0 THEN 1 ELSE 0 END
        WHERE id = ?
    """, (task_id,))
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({"message": "Status updated"})

@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = get_db()
    cursor = conn.execute(
        "DELETE FROM tasks WHERE id=?", (task_id,)
    )
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({"message": "Task deleted"})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
