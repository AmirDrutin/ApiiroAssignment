from Koogle.KoogleDB import KoogleDB
from Koogle.KoogleSearchEntry import KoogleSearchEntry


class SearchManager:
    def __init__(self, koogle_db: KoogleDB):
        self._koogle_db = koogle_db

    def search(self, search_term: str):
        new_search_count = self._koogle_db.insert_entry(search_term=search_term, is_new_search=True)
        for index in range(1, len(search_term) + 1):
            search_prefix = search_term[:index]
            prefix_entry = self._koogle_db.get_entry(search_prefix)
            if not prefix_entry:
                prefix_entry = self._koogle_db.insert_entry(search_term=search_prefix, is_new_search=False)
            SearchManager.add_search_suggestion(prefix_entry=prefix_entry, search_term=search_term,
                                                new_search_count=new_search_count)

    @staticmethod
    def add_search_suggestion(prefix_entry: KoogleSearchEntry, search_term: str, new_search_count: int):
        if not prefix_entry.has_in_suggestion_list(search_term):
            old_last_suggestion = prefix_entry.get_last_suggestion()
            if old_last_suggestion and old_last_suggestion[1] < new_search_count:
                prefix_entry.add_suggestion_last(search_term, new_search_count)
        else:
            prefix_entry.increase_suggestion_count(search_term)
        prefix_entry.sort_suggestion_list()
