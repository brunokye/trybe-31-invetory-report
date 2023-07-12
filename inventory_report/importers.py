import json
from typing import Dict, Type
from abc import ABC, abstractmethod
from inventory_report.product import Product


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        stock = []

        with open(self.path, 'r') as file:
            data = json.load(file)

        for product in data:
            stock.append(
                Product(
                    product['id'],
                    product['product_name'],
                    product['company_name'],
                    product['manufacturing_date'],
                    product['expiration_date'],
                    product['serial_number'],
                    product['storage_instructions']
                )
            )

        return stock


class CsvImporter(Importer):
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
