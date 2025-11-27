class GPU:
    def __init__(self, brand: str, vram: float, clock_speed: float, shaders: int):
        self.brand = brand
        self.vram = vram
        self.clock_speed = clock_speed  # MHz
        self.shaders = shaders
        self.type = "Generic"  # Overridden in subclasses

    def display(self) -> None:
        print(
            f"{self.brand} {self.type} GPU, VRAM: {self.vram}GB, Clock: {self.clock_speed} MHz, Shaders: {self.shaders}"
        )


class DiscreteGPU(GPU):
    def __init__(
        self,
        brand: str,
        vram: float,
        clock_speed: float,
        shaders: int,
        tgp: int,
        ray_tracing_cores: int,
    ):
        super().__init__(brand, vram, clock_speed, shaders)
        self.type = "Discrete"
        self.tgp = tgp  # W
        self.ray_tracing_cores = ray_tracing_cores

    def display(self) -> None:
        super().display()
        print(f"  TGP: {self.tgp}W, Ray Tracing Cores: {self.ray_tracing_cores}")


class IntegratedGPU(GPU):
    def __init__(
        self,
        brand: str,
        vram: float,
        clock_speed: float,
        shaders: int,
        shared_memory_max: float,
        compute_units: int,
    ):
        super().__init__(brand, vram, clock_speed, shaders)
        self.type = "Integrated"
        self.shared_memory_max = shared_memory_max  # GB
        self.compute_units = compute_units

    def display(self) -> None:
        super().display()
        print(
            f"  Shared Memory Max: {self.shared_memory_max}GB, Compute Units: {self.compute_units}"
        )


# Examples with accurate specs
nvidia_gpu = DiscreteGPU(
    "NVIDIA GeForce RTX 5070", 8, 2347, 4608, 50, 144
)  # Boost clock, shaders, TGP, RT cores
nvidia_gpu.display()

amd_gpu = IntegratedGPU(
    "AMD Radeon 860M", 0.5, 3000, 512, 16, 8
)  # Dedicated VRAM, max clock, shaders, shared max, CUs
amd_gpu.display()
