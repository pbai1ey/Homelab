class RAM:
    def __init__(
        self, brand: str, form: str, capacity: int, ddr_type: str, speed: int, swap: int
    ):
        self.brand = brand
        self.form = form
        self.capacity = capacity
        self.ddr_type = ddr_type
        self.speed = speed
        self.swap = swap

    def display(self) -> None:
        print(
            f"{self.brand} {self.form}: {self.capacity}GB, {self.ddr_type}, "
            f"{self.speed} MT/s, swap {self.swap}GB"
        )


if __name__ == "__main__":

    ram = RAM("Micron Technology", "SODIMM", 32, "DDR5", 5600, 8)
    ram.display()
