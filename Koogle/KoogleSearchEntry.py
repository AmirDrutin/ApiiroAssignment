from typing import List, Tuple

MAX_SUGGESTIONS_COUNT = 10


class KoogleSearchEntry:

    def __init__(self):
        self._search_count = 0
        self._suggestion_list = list(("", 0) for _ in range(MAX_SUGGESTIONS_COUNT))

    def increae_count(self):
        self._search_count += 1

    def get_search_count(self):
        return self._search_count

    def get_suggestion_list(self) -> List[Tuple[str, int]]:
        return self._suggestion_list

    def increase_suggestion_count(self, suggestion_term: str):
        for suggestion in self._suggestion_list:
            if suggestion[0] == suggestion_term:
                suggestion[1] += 1

    def has_in_suggestion_list(self, suggestion_term: str):
        for suggestion in self._suggestion_list:
            if suggestion[0] == suggestion_term:
                return True
        return False

    def get_last_suggestion(self) -> Tuple[str, int]:
        return self._suggestion_list[MAX_SUGGESTIONS_COUNT]

    def add_suggestion_last(self, suggestion_term: str, suggestion_count: int):
        for index in range(MAX_SUGGESTIONS_COUNT):
            if not self._suggestion_list[index][0]:
                self._suggestion_list[index] = (suggestion_term, suggestion_count)

                return
        self._suggestion_list[MAX_SUGGESTIONS_COUNT] = (suggestion_term, suggestion_count)

    def sort_suggestion_list(self):
        self._suggestion_list = self._suggestion_list.sort(key=lambda suggestion: suggestion[1])
