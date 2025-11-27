from .cpu import CPU
from .gpu import GPU, DiscreteGPU, IntegratedGPU
from .ram import RAM
from .storage import Storage
from .computer import Computer

__all__ = ["CPU", "GPU", "DiscreteGPU", "IntegratedGPU", "RAM", "Storage", "Computer"]
