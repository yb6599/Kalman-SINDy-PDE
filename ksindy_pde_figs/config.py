from collections.abc import Iterable, Sequence
from typing import TypeVar, cast

import numpy as np
import pysindy as ps
from numpy.typing import NDArray

from gen_experiments.data import _signal_avg_power
from gen_experiments.gridsearch.typing import (
    GridLocator,
    SeriesDef,
    SeriesList,
    SkinnySpecs,
)
from gen_experiments.plotting import _PlotPrefs
from gen_experiments.typing import NestedDict
from gen_experiments.utils import FullSINDyTrialData

T = TypeVar("T", bound=str)
U = TypeVar("U")


def ND(d: dict[T, U]) -> NestedDict[T, U]:
    return NestedDict(**d)


plot_prefs = {
    "absrel-newloc": _PlotPrefs(
        True,
        False,
        GridLocator(
            ["coeff_mse", "coeff_f1"],
            (..., (2, 3, 4)),
            (
                {"diff_params.kind": "kalman", "diff_params.alpha": None},
                {
                    "diff_params.kind": "kalman",
                    "diff_params.alpha": lambda a: isinstance(a, float | int),
                },
                {"diff_params.kind": "trend_filtered"},
                {"diff_params.diffcls": "SmoothedFiniteDifference"},
            ),
        ),
    ),
}
sim_params = {
    "pde-ic1": ND({"init_cond": np.exp(-((np.linspace(-8, 8, 256) + 2) ** 2) / 2),
                   "rel_noise": 0.1}),
    "pde-ic2": ND({
        "init_cond": (np.cos(np.linspace(0, 100, 1024))) * (
            1 + np.sin(np.linspace(0, 100, 1024) - 0.5)
        ),
        "rel_noise": 0.1
    }),
}
diff_params = {
    "test-axis": ND({"diffcls": "FiniteDifference", "axis":-2}),
    "sfd-ps": ND({"diffcls": "SmoothedFiniteDifference", "axis":-2}),
    "savgol": ND({"diffcls": "sindy", "kind": "savitzky_golay", "axis": -2, "left":0.1, "right":0.1, "order":3}),
    "tv": ND({"diffcls": "sindy", "kind": "trend_filtered", "order": 0, "axis":-2, "alpha": 1}),
    "kalman": ND({"diffcls": "sindy", "kind": "kalman", "alpha": 0.000055, "axis":-2}),
    "autoks": ND({"diffcls": "sindy", "kind": "kalman", "alpha": "gcv", "axis":-2}),
}
feat_params = {
    "pde2": ND({
        "featcls": "pde",
        "function_library": ps.PolynomialLibrary(degree=2, include_bias=False),
        "derivative_order": 2,
        "spatial_grid": np.linspace(-8, 8, 256),
        "include_interaction": True,
    }),
    "pde4": ND({
        "featcls": "pde",
        "function_library": ps.PolynomialLibrary(degree=2, include_bias=False),
        "derivative_order": 4,
        "spatial_grid": np.linspace(0, 100, 1024),
        "include_interaction": True,
    }),
}
opt_params = {
    "test": ND({"optcls": "STLSQ"}),
    "test_low": ND({"optcls": "STLSQ", "threshold": 0.09}),
    "miosr": ND({"optcls": "MIOSR"}),
}

metrics = {
    "test": ["coeff_f1", "coeff_mae"],
    "all-coeffs": ["coeff_f1", "coeff_mae", "coeff_mse"],
    "all": ["coeff_f1", "coeff_precision", "coeff_recall", "coeff_mae", "coeff_mse"],
    "lorenzk": ["coeff_f1", "coeff_precision", "coeff_recall", "coeff_mae"],
    "1": ["coeff_f1", "coeff_precision", "coeff_mse", "coeff_mae"],
}

other_params = {
    "test-pde1": ND({
        "sim_params": sim_params["pde-ic1"],
        "diff_params": diff_params["test-axis"],
        "feat_params": feat_params["pde2"],
        "opt_params": opt_params["test_low"],
    }),
    "test-pde2": ND({
        "sim_params": sim_params["pde-ic2"],
        "diff_params": diff_params["test-axis"],
        "feat_params": feat_params["pde4"],
        "opt_params": opt_params["test"],
    }),
}
grid_params = {
    "duration-absnoise": ["sim_params.t_end", "sim_params.noise_abs"],
    "rel-noise": ["sim_params.t_end", "sim_params.noise_rel"],
}
grid_vals: dict[str, list[Iterable]] = {
    "duration-absnoise": [[0.5, 1, 2, 4, 8, 16], [0.1, 0.5, 1, 2, 4, 8]],
    "rel-noise": [[0.5, 1, 2, 4, 8, 16], [0.05, 0.1, 0.15, 0.2, 0.25, 0.3]],
}
grid_decisions = {
    "test": ["plot"],
    "plot1": ["plot", "max"],
    "lorenzk": ["plot", "plot", "max"],
    "plot2": ["plot", "plot"],
}
diff_series: dict[str, SeriesDef] = {
    "kalman": SeriesDef(
        "Kalman",
        diff_params["kalman"],
        ["diff_params.alpha"],
        [np.logspace(-4, 0, 5)],
    ),
    "auto-kalman": SeriesDef(
        "Auto Kalman",
        diff_params["auto-ks"],
        ["diff_params.alpha"],
        [(None,)],
    ),
    "tv": SeriesDef(
        "Total Variation",
        diff_params["tv"],
        ["diff_params.alpha"],
        [np.logspace(-4, 0, 5)],
    ),
    "sg": SeriesDef(
        "Savitsky-Golay",
        diff_params["sfd-ps"],
        ["diff_params.smoother_kws.window_length"],
        [[5, 8, 12, 15]],
    ),
}
series_params: dict[str, SeriesList] = {
    "multikalman": SeriesList(
        "diff_params",
        "Differentiation Method",
        [
            diff_series["auto-kalman"],
            diff_series["kalman"],
            diff_series["tv"],
            diff_series["sg"],
        ],
    ),
}
skinny_specs: dict[str, SkinnySpecs] = {
    "duration-noise": (("sim_params.t_end", "sim_params.noise_rel"), ((1,), (-1,))),
}
lookup_dict = {
    "plot_prefs": plot_prefs,
    "sim_params": sim_params,
    "diff_params": diff_params,
    "feat_params": feat_params,
    "opt_params": opt_params,
    "metrics": metrics,
    "other_params": other_params,
    "grid_params": grid_params,
    "grid_vals": grid_vals,
    "grid_decisions": grid_decisions,
    "diff_series": diff_series,
    "series_params": series_params,
    "skinny_specs": skinny_specs
}
