from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
# The dot (.) is needed because environment.py is now in the same folder
from .environment import AdaptiveSmartFarmingEnv 

app = FastAPI()
env = None

class StepRequest(BaseModel):
    action: str

@app.post("/reset")
def reset():
    global env
    env = AdaptiveSmartFarmingEnv()
    obs = env.reset()
    return {"observation": obs}

@app.post("/step")
def step(request: StepRequest):
    global env
    if env is None:
        return {"error": "Environment not reset"}
    obs, reward, done, info = env.step(request.action)
    return {
        "observation": obs,
        "reward": float(reward),
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return {"status": "running"}

# This function is what the validator looks for to "start" your app
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)