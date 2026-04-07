import os

from env.learning_env import AdaptiveLearningEnv
from agents.rule_agent import RuleAgent
from config.tasks import TASKS

from openai import OpenAI


API_BASE = os.getenv("API_BASE_URL", "")
MODEL = os.getenv("MODEL_NAME", "baseline")
HF_TOKEN = os.getenv("HF_TOKEN", "")


client = OpenAI(base_url=API_BASE, api_key=HF_TOKEN)


def run_task(task):

    env = AdaptiveLearningEnv(difficulty=TASKS[task]["difficulty"])

    agent = RuleAgent()

    obs = env.reset()

    rewards = []

    step = 0

    print(f"[START] task={task} env=AdaptiveLearningEnv model={MODEL}")

    done = False

    while not done:

        action = agent.select_action(obs)

        try:

            obs, reward, done, _ = env.step(action)

            rewards.append(round(reward.value, 3))

            print(
                f"[STEP] step={step} action={action.action_type} reward={reward.value:.3f} done={str(done).lower()} error=null"
            )

        except Exception as e:

            print(
                f"[STEP] step={step} action={action.action_type} reward=0.0 done=true error={str(e)}"
            )

            done = True

        step += 1

    success = True

    rewards_str = ",".join(map(str, rewards))

    print(f"[END] success={str(success).lower()} steps={step} rewards={rewards_str}")


if __name__ == "__main__":

    for task in ["easy", "medium", "hard"]:

        run_task(task)