from gen_experiments import pdes
from collections.abc import Iterable
from typing import TypeVar
import numpy as np
from gen_experiments.typing import NestedDict

T = TypeVar("T", bound=str)
U = TypeVar("U")

def ND(d: dict[T, U]) -> NestedDict[T, U]:
    return NestedDict(**d)


group = {
    "diffuse1D_periodic": pdes.diffuse1D_periodic,
    "burgers1D_periodic": pdes.burgers1D_periodic,
    "ks_periodic": pdes.ks_periodic,
}
sim_params = {
    "pde-ic1": ND({
        "spatial_grid": np.linspace(-8, 8, 256),
        "init_cond": np.exp(-((np.linspace(-8, 8, 256) + 2) ** 2) / 2),
        "rel_noise": 1e-4,
        "t_end": 10, 
        "dt": 0.1}),
    "pde-ic2": ND({
        "spatial_grid": np.linspace(0, 100, 1024),
        "init_cond": (np.cos(np.linspace(0, 100, 1024))) * (
            1 + np.sin(np.linspace(0, 100, 1024) - 0.5)
        ),
        "rel_noise": 0.1,
        "t_end": 100,
        "dt": 0.4
    }),
}
grid_params = {
    "duration-absnoise": ["sim_params.t_end", "sim_params.noise_abs"],
    "rel-noise": ["sim_params.t_end", "sim_params.rel_noise"],
}
grid_vals: dict[str, list[Iterable]] = {
    "duration-absnoise": [[0.5, 1, 2, 4, 8, 16], [0.1, 0.5, 1, 2, 4, 8]],
    "rel-noise": [[8, 16, 32, 64, 128], [0.05, 0.1, 0.15, 0.2, 0.25]],
}

lookup_dict = {
    "group": group,
    "sim_params": sim_params,
    "grid_vals": grid_vals,
    "grid_params": grid_params
}