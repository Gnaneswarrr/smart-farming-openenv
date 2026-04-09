import os
from openai import OpenAI

from environment import AdaptiveSmartFarmingEnv


API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable is required")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)


def main():
    print(f"[START] task=smart-farming env=openenv model={MODEL_NAME}")

    total_rewards = []
    total_steps = 0
    success = False

    env = None

    try:
        env = AdaptiveSmartFarmingEnv()
        obs = env.reset()

        done = False

        while not done:
            action = "WAIT"

            obs, reward, done, _ = env.step(action)

            reward_val = float(reward)
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
        if env is not None:
            env.close()

        print(
            f"[END] success={str(success).lower()} steps={total_steps} rewards={','.join(total_rewards)}"
        )


if __name__ == "__main__":
    main()
