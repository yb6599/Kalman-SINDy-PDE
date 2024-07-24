nohup mitosis pde_grid \
    --debug \
    --eval-param pde_grid.seed=19 \
    --eval-param pde_grid.group=\"diffuse1D_periodic\" \
    -F trials \
    --param pde_grid.metrics=all \
    --param pde_grid.other_params=test-pde1 \
    --param pde_grid.grid_params=rel-noise \
    --param pde_grid.grid_vals=rel-noise \
    --param pde_grid.grid_decisions=plot2 \
    --param pde_grid.series_params=multikalman \
    --param +pde_grid.plot_prefs=absrel-newloc \
    --param +pde_grid.skinny_specs=duration-noise &> diffuse1D_periodic.log &

nohup mitosis pde_grid \
    --debug \
    --eval-param pde_grid.seed=19 \
    --eval-param pde_grid.group=\"burgers1D_periodic\" \
    -F trials \
    --param pde_grid.metrics=all \
    --param pde_grid.other_params=test-pde1 \
    --param pde_grid.grid_params=rel-noise \
    --param pde_grid.grid_vals=rel-noise \
    --param pde_grid.grid_decisions=plot2 \
    --param pde_grid.series_params=multikalman \
    --param +pde_grid.plot_prefs=absrel-newloc \
    --param +pde_grid.skinny_specs=duration-noise &> burgers1D_periodic.log &

nohup mitosis pde_grid \
    --debug \
    --eval-param pde_grid.seed=19 \
    --eval-param pde_grid.group=\"ks_periodic\" \
    -F trials \
    --param pde_grid.metrics=all \
    --param pde_grid.other_params=test-pde2 \
    --param pde_grid.grid_params=rel-noise \
    --param pde_grid.grid_vals=rel-noise \
    --param pde_grid.grid_decisions=plot2 \
    --param pde_grid.series_params=multikalman \
    --param +pde_grid.plot_prefs=absrel-newloc \
    --param +pde_grid.skinny_specs=duration-noise &> ks_periodic.log &
