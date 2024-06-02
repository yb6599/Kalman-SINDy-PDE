nohup mitosis gen_experiments.gridsearch \
    -e seed=19 \
    -g diffuse1D_periodic \
    -F trials \
    --param metrics=all \
    --param other_params=test-pde-sg \
    --param grid_params=rel-noise \
    --param grid_vals=rel-noise \
    --param grid_decisions=plot2 \
    --param series_params=None \
    --param +plot_prefs=absrel-newloc \
    --param +skinny_specs=duration-noise &> diffuse1D_periodic.log &

nohup mitosis pde_grid \
    -e seed=19 \
    -g burgers1D_periodic \
    -F trials \
    --param metrics=all \
    --param other_params=test-pde-sg \
    --param grid_params=rel-noise \
    --param grid_vals=rel-noise \
    --param grid_decisions=plot2 \
    --param series_params=None \
    --param +plot_prefs=absrel-newloc \
    --param +skinny_specs=duration-noise &> burgers1D_periodic.log &

nohup mitosis gen_experiments.gridsearch \
    -e seed=19 \
    -g ks_periodic \
    -F trials \
    --param metrics=all \
    --param other_params=test-pde-sg \
    --param grid_params=rel-noise \
    --param grid_vals=rel-noise \
    --param grid_decisions=plot2 \
    --param series_params=None \
    --param +plot_prefs=absrel-newloc \
    --param +skinny_specs=duration-noise &> ks_periodic.log &
