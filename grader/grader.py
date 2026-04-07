def evaluate_episode(history):

    mastery = history["final_mastery"]
    steps = history["steps"]

    learning_gain = sum(mastery) / len(mastery)

    completion_rate = sum(1 for m in mastery if m > 0.8) / len(mastery)

    efficiency = max(0.0, 1 - (steps / 40))

    score = (learning_gain * 0.5) + (completion_rate * 0.3) + (efficiency * 0.2)

    return {
        "learning_gain": learning_gain,
        "completion_rate": completion_rate,
        "efficiency": efficiency,
        "score": min(1.0, score)
    }