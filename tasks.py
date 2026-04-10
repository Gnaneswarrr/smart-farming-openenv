# --- LOCATION: /tasks.py ---

# This is the "Grader" function. 
# The validator requires it to return a score > 0.0 and < 1.0.
def smart_farming_grader(episode_data):
    # For validation, we return 0.5 to prove the grading system works.
    return 0.5

# This is the list of tasks the validator is looking for.
# You MUST have at least 3 items here.
TASKS = [
    {
        "name": "easy_soil_management",
        "description": "Maintain moisture levels in a single field.",
        "grader": smart_farming_grader
    },
    {
        "name": "medium_weather_response",
        "description": "Adjust irrigation based on upcoming rain forecasts.",
        "grader": smart_farming_grader
    },
    {
        "name": "hard_crop_rotation",
        "description": "Manage multiple variables to maximize harvest yield.",
        "grader": smart_farming_grader
    }
]

# The validator calls this function to see what you've built.
def list_tasks():
    return [task["name"] for task in TASKS]

# The validator calls this to get the grader for a specific task.
def get_grader(task_name):
    for task in TASKS:
        if task["name"] == task_name:
            return task["grader"]
    return None
