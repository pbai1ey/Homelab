from cpu import CPU
from gpu import DiscreteGPU, IntegratedGPU
from ram import RAM
from storage import Storage
from computer import Computer

if __name__ == "__main__":
    cpu = CPU("AMD", "Ryzen AI 7 350", 8, 16, 2.0, 5.1)
    nvidia_gpu = DiscreteGPU("NVIDIA GeForce RTX 5070", 8, 2347, 4608, 50, 144)
    amd_gpu = IntegratedGPU("AMD Radeon 860M", 0.5, 3000, 512, 16, 8)
    ram = RAM("Micron Technology", "SODIMM", 32, "DDR5", 5600, 8)
    storage = Storage("Kingston OM8PGP41024Q-A0", 1, 4700, 3400, 0.002, 5)
    aero = Computer("aero", cpu, nvidia_gpu, amd_gpu, ram, storage)
    aero.display()
