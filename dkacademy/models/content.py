from models.base import BaseModel
from dataclasses import dataclass


@dataclass
class Question(BaseModel):
    question: str
    answers: list[str]
    correct_answer: str
    explanation: str

    def to_json(self):
        return {
            "question": self.question,
            "answers": self.answers,
            "correct_answer": self.correct_answer,
            "explanation": self.explanation
        }


@dataclass
class Panel(BaseModel):
    panel_number: int
    story: str
    visual_prompts: list[str]
    question: Question | None
    learned: str

    def to_json(self):
        return {
            "panel_number": self.panel_number,
            "story": self.story,
            "visual_prompts": self.visual_prompts,
            "question": self.question.to_json() if self.question else None,
            "learned": self.learned
        }


@dataclass
class Content(BaseModel):
    title: str
    panels: list[Panel]

    def to_json(self):
        return {
            "title": self.title,
            "panels": [panel.to_json() for panel in self.panels]
        }
