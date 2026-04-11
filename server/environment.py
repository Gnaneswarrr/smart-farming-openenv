class AdaptiveSmartFarmingEnv:
    def __init__(self):
        self.max_steps = 5
        self.current_step = 0

    def reset(self):
        self.current_step = 0
        return {"step": self.current_step, "status": "ready"}

    def step(self, action):
        self.current_step += 1
        done = self.current_step >= self.max_steps
        observation = {"step": self.current_step, "last_action": action}
        reward = 1.0
        info = {"task": "easy"}
        return observation, reward, done, info

    def close(self):
        return None
