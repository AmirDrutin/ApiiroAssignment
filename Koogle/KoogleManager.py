from typing import List, Tuple

from Koogle.KoogleDB import KoogleDB
from Koogle.KoogleExceptions import BadSearchInputException, BadSuggestionInputException
from Koogle.SearchManager import SearchManager
from Koogle.SuggestionManager import SuggestionManager


class KoogleManager:

    def __init__(self):
        self._koogle_db = KoogleDB()
        self._search_manager = SearchManager(self._koogle_db)
        self._suggestion_manager = SuggestionManager(self._koogle_db)

    def koogle_search(self, search_term: str):
        if not isinstance(search_term, str):
            raise BadSearchInputException()

        self._search_manager.search(search_term)

    def koogle_suggestion(self, suggestion_term: str) -> List[Tuple[str, int]] | None:
        if not isinstance(suggestion_term, str):
            raise BadSuggestionInputException()

        return self._suggestion_manager.suggest(suggestion_term)
