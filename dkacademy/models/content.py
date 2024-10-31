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

    @classmethod
    def from_json(cls, data):
        return cls(question=data["question"],
                   answers=data["answers"],
                   correct_answer=data["correct_answer"],
                   explanation=data["explanation"])


@dataclass
class Panel(BaseModel):
    panel_number: int
    story: str
    visual_prompts: list[str]
    question: Question
    learned: str

    def to_json(self):
        return {
            "panel_number": self.panel_number,
            "story": self.story,
            "visual_prompts": self.visual_prompts,
            "question": self.question.to_json(),
            "learned": self.learned
        }

    @classmethod
    def from_json(cls, data):
        return cls(panel_number=data["panel_number"],
                   story=data["story"],
                   visual_prompts=data["visual_prompts"],
                   question=Question.from_json(data["question"]),
                   learned=data["learned"])


@dataclass
class Content(BaseModel):
    title: str
    panels: list[Panel]

    def to_json(self):
        return {
            "title": self.title,
            "panels": [panel.to_json() for panel in self.panels]
        }

    @classmethod
    def from_json(cls, data):
        return cls(title=data["title"],
                   panels=[Panel.from_json(panel) for panel in data["panels"]])
