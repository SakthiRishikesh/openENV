"""
Baseline agent for CurriculumEnv
Input: state dictionary
Output: action string
"""

# simple memory to avoid loops
action_history = []
quiz_failures = 0


def baseline_agent(state):

    global action_history
    global quiz_failures

    mastery = state["concept_mastery"]
    fatigue = state["fatigue"]
    quiz_accuracy = state.get("quiz_accuracy", 0)
    engagement = state.get("engagement", 1)

    avg_mastery = sum(mastery) / len(mastery)

    # fatigue handling
    if fatigue > 0.75:
        action = "take_break"

    # early learning
    elif avg_mastery < 0.25:
        action = "show_video"

    # practice phase
    elif avg_mastery < 0.55:
        action = "interactive_exercise"

    # quiz phase
    elif avg_mastery < 0.85:

        if quiz_accuracy < 0.6:
            quiz_failures += 1

            if quiz_failures >= 2:
                action = "revision_notes"
            else:
                action = "give_quiz"

        else:
            action = "interactive_exercise"

    # mastery complete
    else:
        action = "skip_topic"

    # prevent loops
    action_history.append(action)
    if len(action_history) > 5:
        action_history.pop(0)

    return action