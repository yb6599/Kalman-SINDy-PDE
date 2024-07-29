import gen_experiments
from ksindy_pde_figs import config

# %%
gen_experiments.pdes.run(42,
        group= "burgers1D_periodic",
        sim_params=config.sim_params["pde-ic1"],
        diff_params=config.diff_params["kalman-auto"],
        opt_params=config.opt_params["test"],
        feat_params=config.feat_params["pde2"],
)