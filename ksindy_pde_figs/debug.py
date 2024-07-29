# %%
import gen_experiments
from ksindy_pde_figs import config

# %%
gen_experiments.gridsearch.run(seed=19,
                               group="diffuse1D_periodic",
                               grid_params=config.grid_params["rel-noise"],
                               grid_vals=config.grid_vals["rel-noise"],
                               grid_decisions=config.grid_decisions["plot2"],
                               other_params=config.other_params["test-pde1"],
                               skinny_specs=config.skinny_specs["duration-noise"],
                               series_params=config.series_params["multikalman"],
                               metrics=config.metrics["all"],
                               plot_prefs=config.plot_prefs["absrel-newloc"])

# %%
gen_experiments.pdes.run(42,
        group= "burgers1D_periodic",
        sim_params=config.sim_params["pde-ic1"],
        diff_params=config.diff_params["autoks"],
        opt_params=config.opt_params["test"],
        feat_params=config.feat_params["pde2"],
)
# %%
# gen_experiments.pdes.run(42,
#         group= "diffuse1D_periodic",
#         sim_params=config.sim_params["pde-ic1"],
#         diff_params=config.diff_params["test_axis"],
#         opt_params=config.opt_params["test"],
#         feat_params=config.feat_params["pde2"],
# )
# %%
