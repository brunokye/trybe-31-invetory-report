from typing import Optional
from inventory_report.product import Product


class Inventory:
    def __init__(self, data: Optional[list[Product]] = None):
        if data is None:
            self._data = []
        else:
            self._data = data

    @property
    def data(self) -> list[Product]:
        return self._data.copy()

    def add_data(self, data: list[Product]) -> None:
        return self._data.extend(data)
