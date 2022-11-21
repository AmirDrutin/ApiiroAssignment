from typing import List, Tuple

from Koogle.KoogleManager import KoogleManager


def Search(search_term: str):
    KoogleManager().koogle_search(search_term)


def Suggest(suggestion_term: str) -> List[Tuple[str, int]] | None:
    return KoogleManager().koogle_suggestion(suggestion_term)


if __name__ == '__main__':
    Search("Hello")
    print(Suggest("Hel"))
