from typing import Dict, Any, TypeVar, Generic

T = TypeVar('T')

class Registry(Generic[T]):
    def __init__(self):
        self._items: Dict[str, T] = {}

    def register(self, key: str, item: T):
        self._items[key] = item

    def get(self, key: str) -> T:
        if key not in self._items:
            raise KeyError(f"Item '{key}' not found in registry.")
        return self._items[key]

    def list_all(self) -> Dict[str, T]:
        return self._items.copy()
