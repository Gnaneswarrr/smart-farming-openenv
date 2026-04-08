import os

from openai import OpenAI

from environment import AdaptiveSmartFarmingEnv
from tasks import list_tasks


API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")
TASK_NAME = os.getenv("TASK_NAME", "easy")


def select_action(obs):
    return "WAIT"


def main():
    print(f"[START] task=smart-farming env=openenv model={MODEL_NAME}")

    total_rewards = []
    total_steps = 0
    success = False
    env = AdaptiveSmartFarmingEnv()
    client = None

    try:
        if HF_TOKEN is None:
            raise ValueError("HF_TOKEN environment variable is required")

        client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)
        _ = client

        task_names = list_tasks()
        selected_task = TASK_NAME if TASK_NAME in task_names else task_names[0]
        _ = selected_task

        obs = env.reset()

        done = False
        while not done:
            action = select_action(obs)
            obs, reward, done, _info = env.step(action)

            reward_val = reward.value if hasattr(reward, "value") else float(reward)
            total_rewards.append(f"{reward_val:.2f}")
            total_steps += 1

            print(
                f"[STEP] step={total_steps} action={action} "
                f"reward={reward_val:.2f} done={str(done).lower()} error=null"
            )

        success = True
    except Exception:
        success = False
    finally:
        env.close()

        rewards_str = ",".join(total_rewards)
        print(f"[END] success={str(success).lower()} steps={total_steps} rewards={rewards_str}")


if __name__ == "__main__":
    main()
