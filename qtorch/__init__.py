from .number import *

__all__ = ["FixedPoint", "BlockFloatingPoint", "FloatingPoint"]

import os
import torch

current_dir = os.path.dirname(os.path.abspath(__file__))
lib = os.path.join(*[current_dir, 'quant/quant_cpu/build/libqtorch_ops.so'])
torch.ops.load_library(lib)
