import os
import sys
from openai import OpenAI
from server.environment import AdaptiveSmartFarmingEnv

# Mandatory Environment Variables
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    print("Error: HF_TOKEN environment variable is required")
    sys.exit(1)

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

def run_inference():
    env = AdaptiveSmartFarmingEnv()
    obs = env.reset()
    
    # [START] Line - Required Format
    print(f"[START] task=farming-task env=smart-farming model={MODEL_NAME}")
    
    rewards = []
    done = False
    step_n = 0

    while not done and step_n < 10:
        step_n += 1
        prompt = f"The farm state is {obs}. What action should I take? (e.g., water, harvest, wait). Answer in one word."
        
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": prompt}]
            )
            action = response.choices[0].message.content.strip()
            obs, reward, done, info = env.step(action)
            rewards.append(f"{reward:.2f}")
            
            # [STEP] Line - Required Format
            print(f"[STEP] step={step_n} action={action} reward={reward:.2f} done={str(done).lower()} error=null")
        except Exception as e:
            print(f"[STEP] step={step_n} action=none reward=0.00 done=true error={str(e)}")
            break

    # [END] Line - Required Format
    success = "true" if step_n > 0 else "false"
    print(f"[END] success={success} steps={step_n} rewards={','.join(rewards)}")

if __name__ == "__main__":
    run_inference()
