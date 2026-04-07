# agents/baseline_agent.py

class BaselineAgent:
    def __init__(self):
        self.current_idx = 0

    def act(self, state):
        mastery_list = state.get("concept_mastery", [])
        fatigue = state.get("fatigue", 0)
        engagement = state.get("engagement", 1)

        # find weakest / current concept
        idx = min(self.current_idx, len(mastery_list) - 1)
        mastery = mastery_list[idx]

        # -------- FATIGUE CONTROL --------
        if fatigue > 0.75:
            return "take_break"

        # -------- MAIN STRATEGY --------
        if mastery < 0.4:
            return "show_video"

        elif mastery < 0.65:
            return "interactive_exercise"

        else:
            # after quiz, move to next concept
            self.current_idx += 1
            return "give_quiz"


agent_instance = BaselineAgent()

def baseline_agent(state):
    return agent_instance.act(state)