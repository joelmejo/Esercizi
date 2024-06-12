def make_car(manufacturer: str, model: str, **kwargs) -> None:
    car: dict = {'manufacturer': manufacturer, 'model': model, **kwargs}
    return car