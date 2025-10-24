from models import Item


def load_seed_data():
    """Retorna una lista con 5 ítems iniciales de la tienda de productos."""
    return [
        Item(id=1, name="Laptop", price=2500.0, available=True),
        Item(id=2, name="Mouse", price=80.0, available=True),
        Item(id=3, name="Keyboard", price=150.0, available=True),
        Item(id=4, name="Monitor", price=700.0, available=False),
        Item(id=5, name="Headphones", price=300.0, available=True),
    ]
