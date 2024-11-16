class Dollar:
    def __init__(self, value: float = 0.0):
        self.value = value

    def __str__(self):
        return f'${self.value}'
