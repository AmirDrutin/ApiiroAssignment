from typing import List, Tuple

from Koogle.KoogleDB import KoogleDB


class SuggestionManager:
    def __init__(self, koogle_db: KoogleDB):
        self._koogle_db = koogle_db

    def suggest(self, suggest_term: str) -> List[Tuple[str, int]] | None:
        suggest_entry = self._koogle_db.get_entry(suggest_term)
        if not suggest_entry:
            return None
        return suggest_entry.get_suggestion_list()
