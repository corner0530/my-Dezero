# simple version

# from dezero.core_simple import (
#     Function,
#     Variable,
#     as_array,
#     as_variable,
#     no_grad,
#     setup_variable,
#     using_config,
# )

# full version

from dezero.core import (
    Function,
    Parameter,
    Variable,
    as_array,
    as_variable,
    no_grad,
    setup_variable,
    using_config,
)
from dezero.layers import Layer
from dezero.models import Model
from dezero.datasets import Dataset
from dezero.dataloaders import DataLoader

import dezero.datasets
import dezero.dataloaders
import dezero.functions
import dezero.layers
import dezero.optimizers
import dezero.transforms

setup_variable()
