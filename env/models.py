from pydantic import BaseModel
from typing import List, Optional


class Observation(BaseModel):
    concept_mastery: List[float]
    quiz_accuracy: float
    time_spent: float
    attempt_count: int
    fatigue: float
    engagement: float


class Action(BaseModel):
    action_type: str


class Reward(BaseModel):
    value: float
    reason: Optional[str] = Nonegf