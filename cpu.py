class CPU:
    def __init__(
        self,
        brand: str,
        model: str,
        cores: int,
        threads: int,
        base_clock: float,
        boost_clock: float,
    ):
        self.brand = brand
        self.model = model
        self.cores = cores
        self.threads = threads
        self.base_clock = base_clock
        self.boost_clock = boost_clock

    def display(self) -> None:
        print(
            f"{self.brand} {self.model}: {self.cores} cores, {self.threads} threads, "
            f"base {self.base_clock} GHz, boost {self.boost_clock} GHz"
        )


if __name__ == "__main__":
    cpu = CPU("AMD", "Ryzen AI 7 350", 8, 16, 2.0, 5.1)
    cpu.display()
