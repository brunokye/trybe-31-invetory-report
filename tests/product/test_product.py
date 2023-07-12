from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
        '1',
        'Rexona',
        'Unilever',
        '2023-07-12',
        '2024-12-11',
        '1234',
        'Armazenar em local com materais comburentes'
    )

    assert product.id == '1'
    assert product.product_name == 'Rexona'
    assert product.company_name == 'Unilever'
    assert product.manufacturing_date == '2023-07-12'
    assert product.expiration_date == '2024-12-11'
    assert product.serial_number == '1234'
    assert product.storage_instructions == (
        'Armazenar em local com materais comburentes'
    )
