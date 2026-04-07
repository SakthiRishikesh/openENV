import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from env.curriculum_env import CurriculumEnv
from agents.baseline_agent import BaselineAgent


def evaluate(student_type="medium"):
    env = CurriculumEnv(student_type)
    state = env.reset()

    agent = BaselineAgent()

    total_reward = 0
    steps = 0
    initial_mastery = sum(state["concept_mastery"])

    done = False
    while not done:
        action = agent.act(state)
        state, reward, done, _ = env.step(action)

        total_reward += reward
        steps += 1

    final_mastery = sum(state["concept_mastery"])

    learning_gain = final_mastery - initial_mastery
    completion_rate = final_mastery / len(state["concept_mastery"])
    efficiency = 1 / steps if steps > 0 else 0

    score = 0.5 * learning_gain + 0.3 * completion_rate + 0.2 * efficiency

    return max(0, min(1, score))


if __name__ == "__main__":
    for level in ["easy", "medium", "hard"]:
        print(level, evaluate(level))