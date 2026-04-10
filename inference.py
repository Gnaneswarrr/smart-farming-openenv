import os
from openai import OpenAI
from server.environment import AdaptiveSmartFarmingEnv

# 1. Environment Variables
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable is required")

# 2. Initialize Client
client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

def run_task():
    env = AdaptiveSmartFarmingEnv()
    obs = env.reset()
    
    task_name = "smart-farming-task"
    benchmark = "openenv-farming"
    
    # [START] Line
    print(f"[START] task={task_name} env={benchmark} model={MODEL_NAME}")
    
    rewards_list = []
    done = False
    step_count = 0

    while not done:
        step_count += 1
        
        # Use LLM to decide the action based on observation
        prompt = f"Observation: {obs}. What is the next action for the farm? Respond with one word."
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )
        action = response.choices[0].message.content.strip()

        # Step the environment
        obs, reward, done, info = env.step(action)
        rewards_list.append(f"{reward:.2f}")
        
        # [STEP] Line
        print(f"[STEP] step={step_count} action={action} reward={reward:.2f} done={str(done).lower()} error=null")

    env.close()
    
    # [END] Line
    success = "true" if sum([float(r) for r in rewards_list]) > 0 else "false"
    print(f"[END] success={success} steps={step_count} rewards={','.join(rewards_list)}")

if __name__ == "__main__":
    try:
        run_task()
    except Exception as e:
        # Fallback [END] line if something crashes
        print(f"[END] success=false steps=0 rewards=0.00 error={str(e)}")
