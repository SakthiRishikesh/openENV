"""
Deterministic Evaluation System

Tasks:
    easy student
    medium student
    hard student

Metrics:
    learning_gain
    completion_rate
    efficiency

Score:
    score = 0.5 * learning_gain + 0.3 * completion_rate + 0.2 * efficiency
"""

class Evaluator:

    def __init__(self, total_concepts: int):
        self.total_concepts = total_concepts


    def evaluate(self, initial_state: dict, final_state: dict, steps: int):
        """
        Evaluate episode performance
        """

        initial_mastery = self._average(initial_state["concept_mastery"])
        final_mastery = self._average(final_state["concept_mastery"])

        # -----------------------------
        # Learning Gain
        # -----------------------------
        learning_gain = final_mastery - initial_mastery

        if learning_gain < 0:
            learning_gain = 0.0

        # -----------------------------
        # Completion Rate
        # -----------------------------
        completed_concepts = 0

        for mastery in final_state["concept_mastery"]:

            if mastery >= 0.8:
                completed_concepts += 1

        completion_rate = completed_concepts / self.total_concepts

        # -----------------------------
        # Efficiency
        # -----------------------------
        if steps <= 0:
            efficiency = 0
        else:
            efficiency = 1 / steps

        # -----------------------------
        # Final Score
        # -----------------------------
        score = (
            0.5 * learning_gain +
            0.3 * completion_rate +
            0.2 * efficiency
        )

        # clamp score to [0,1]
        score = max(0.0, min(score, 1.0))

        return {
            "learning_gain": round(learning_gain, 4),
            "completion_rate": round(completion_rate, 4),
            "efficiency": round(efficiency, 4),
            "score": round(score, 4)
        }


    # -----------------------------
    # helper function
    # -----------------------------

    def _average(self, values):

        if len(values) == 0:
            return 0

        return sum(values) / len(values)