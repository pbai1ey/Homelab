class Storage:
    def __init__(
        self,
        brand: str,
        capacity: int,
        read: int,
        write: int,
        power_low: float,
        power_high: int,
    ):
        self.brand = brand
        self.capacity = capacity
        self.read = read
        self.write = write
        self.power_low = power_low
        self.power_high = power_high

    def display(self) -> None:
        print(
            f"{self.brand} Storage: {self.capacity}TB, Read: {self.read}MB/s, "
            f"Write: {self.write}MB/s, Power: {self.power_low}-{self.power_high}W"
        )


storage = Storage("Kingston OM8PGP41024Q-A0", 1, 4700, 3400, 0.002, 5)
storage.display()
