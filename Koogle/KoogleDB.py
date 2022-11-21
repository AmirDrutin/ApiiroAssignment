from Koogle.KoogleSearchEntry import KoogleSearchEntry


class KoogleDB:

    def __init__(self):
        self._db = {}

    def get_entry(self, search_term: str) -> KoogleSearchEntry | None:
        if not self._db or self._db[search_term][0]:
            return None
        return self._db[search_term]

    def insert_entry(self, search_term: str, is_new_search: bool) -> int:
        entry = self.get_entry(search_term)
        if not entry:
            entry = KoogleSearchEntry()
        if is_new_search:
            entry.increae_count()
        self._db[search_term] = entry
        return entry.get_search_count()
