from inventory_report.product import Product


def test_product_report() -> None:
    product = Product(
        '1',
        'Rexona',
        'Unilever',
        '2023-07-12',
        '2024-12-11',
        '1234',
        'Armazenar em local com materais comburentes'
    )

    result = (
        "The product 1 - Rexona "
        "with serial number 1234 "
        "manufactured on 2023-07-12 "
        "by the company Unilever "
        "valid until 2024-12-11 "
        "must be stored according to the following instructions: "
        "Armazenar em local com materais comburentes."
    )

    assert str(product) == result
