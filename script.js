
const taskInput = document.getElementById("taskInput");
const taskList = document.getElementById("taskList");

async function loadTasks() {
    const response = await fetch("/api/tasks");
    const tasks = await response.json();

    taskList.innerHTML = "";

    tasks.forEach(task => {
        const li = document.createElement("li");

        const title = document.createElement("span");
        title.textContent = task.title;
        if (task.completed) {
            title.classList.add("completed");
        }

        const actions = document.createElement("div");
        actions.className = "actions";

        const completeBtn = document.createElement("button");
        completeBtn.textContent = task.completed ? "Undo" : "Done";
        completeBtn.onclick = () => toggleTask(task.id);

        const editBtn = document.createElement("button");
        editBtn.textContent = "Edit";
        editBtn.className = "edit";
        editBtn.onclick = () => editTask(task.id, task.title);

        const deleteBtn = document.createElement("button");
        deleteBtn.textContent = "Delete";
        deleteBtn.className = "delete";
        deleteBtn.onclick = () => deleteTask(task.id);

        actions.append(completeBtn, editBtn, deleteBtn);
        li.append(title, actions);
        taskList.appendChild(li);
    });
}

async function addTask() {
    const title = taskInput.value.trim();

    if (!title) {
        alert("Enter a task!");
        return;
    }

    const response = await fetch("/api/tasks", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({title})
    });

    if (!response.ok) {
        alert("Could not add task");
        return;
    }

    taskInput.value = "";
    loadTasks();
}

async function editTask(id, oldTitle) {
    const newTitle = prompt("Edit your task:", oldTitle);

    if (newTitle === null || !newTitle.trim()) return;

    const response = await fetch(`/api/tasks/${id}`, {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({title: newTitle.trim()})
    });

    if (response.ok) loadTasks();
}

async function toggleTask(id) {
    await fetch(`/api/tasks/${id}/complete`, {
        method: "PATCH"
    });

    loadTasks();
}

async function deleteTask(id) {
    if (!confirm("Delete this task?")) return;

    await fetch(`/api/tasks/${id}`, {
        method: "DELETE"
    });

    loadTasks();
}

loadTasks();
