from models.prompt import Prompt
from models.user import User
import utils


class PromptBuilder:

    def __init__(self):
        self._instruction = None
        self._prompt_data = None

    @property
    def system_instruction(self) -> str | None:
        return self._instruction

    @property
    def prompt(self) -> str:
        js = "```json\n{}```"
        if self._prompt_data:
            return js.format(self._prompt_data)
        return js.format("{}")

    def build(self, prompt: Prompt) -> None:
        self._instruction = utils.load_system_instruction()
        self._prompt_data = prompt.to_json()
