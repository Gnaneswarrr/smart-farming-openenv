from fastapi import FastAPI
from environment import AdaptiveSmartFarmingEnv

app = FastAPI()

env = None


@app.post("/reset")
def reset():
    global env
    env = AdaptiveSmartFarmingEnv()
    obs = env.reset()
    return {"observation": obs}


@app.post("/step")
def step(action: str):
    global env
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs,
        "reward": float(reward),
        "done": done,
        "info": info
    }


@app.get("/state")
def state():
    return {"status": "running"}
