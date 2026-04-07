import os
from agents.baseline_agent import baseline_agent
from env.curriculum_env import CurriculumEnv

TASK_NAME = "adaptive_learning"
BENCHMARK = "openenv"
MODEL_NAME = os.getenv("MODEL_NAME", "baseline")


def run(student_type):
    env = CurriculumEnv(student_type)
    state = env.reset()

    print(f"[START] task={TASK_NAME} env={BENCHMARK} model={MODEL_NAME}")

    rewards = []
    step_num = 0
    done = False

    while not done and step_num < 20:
        action = baseline_agent(state)
        state, reward, done, _ = env.step(action)

        rewards.append(reward)
        step_num += 1

        print(f"[STEP] step={step_num} action={action} reward={reward:.2f} done={str(done).lower()} error=null")

    print(f"[END] success={str(done).lower()} steps={step_num} rewards={','.join([f'{r:.2f}' for r in rewards])}")


if __name__ == "__main__":
    for level in ["easy", "medium", "hard"]:
        run(level)