from fastapi import FastAPI, Request
from pydantic import BaseModel
from environment import AdaptiveSmartFarmingEnv

app = FastAPI()

env = None


# ✅ Request model for /step
class StepRequest(BaseModel):
    action: str


# ✅ FIXED /reset (accepts empty JSON safely)
@app.post("/reset")
async def reset(request: Request):
    global env
    env = AdaptiveSmartFarmingEnv()
    obs = env.reset()

    return {
        "observation": obs
    }


# ✅ FIXED /step
@app.post("/step")
def step(request: StepRequest):
    global env

    obs, reward, done, info = env.step(str(request.action))

    return {
        "observation": obs,
        "reward": float(reward),
        "done": done,
        "info": info
    }


# ✅ Optional state check
@app.get("/state")
def state():
    return {"status": "running"}
