from env.models import Action


class RuleAgent:

    def select_action(self, obs):

        avg_mastery = sum(obs.concept_mastery) / len(obs.concept_mastery)

        if obs.fatigue > 0.7:
            return Action(action_type="take_break")

        if avg_mastery < 0.3:
            return Action(action_type="show_video")

        if avg_mastery < 0.6:
            return Action(action_type="interactive_exercise")

        if obs.quiz_accuracy < 0.7:
            return Action(action_type="give_quiz")

        if avg_mastery > 0.8:
            return Action(action_type="skip_topic")

        return Action(action_type="revision_notes")