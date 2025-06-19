import json
import os
from datetime import datetime

TASK_FILE = "data/tasks.json"

def load_tasks():
    """Load tasks from JSON file"""
    if not os.path.exists(TASK_FILE):
        os.makedirs(os.path.dirname(TASK_FILE), exist_ok=True)
        return []
    
    try:
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    """Save tasks to JSON file"""
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(title, description, priority):
    """Add a new task"""
    tasks = load_tasks()
    new_task = {
        'id': len(tasks) + 1,
        'title': title,
        'description': description,
        'priority': priority,
        'completed': False,
        'created_at': datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)

def get_tasks():
    """Get all tasks"""
    return load_tasks()

def update_task_status(task_id, completed):
    """Update task completion status"""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = completed
            break
    save_tasks(tasks)

def delete_task(task_id):
    """Delete a task by ID"""
    tasks = load_tasks()
    tasks = [t for t in tasks if t['id'] != task_id]
    save_tasks(tasks)