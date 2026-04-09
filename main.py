from fastapi import FastAPI
from pydantic import BaseModel
from environment import AdaptiveSmartFarmingEnv

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
