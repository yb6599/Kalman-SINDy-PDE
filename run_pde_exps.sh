nohup mitosis gen_experiments.gridsearch \
    -e seed=19 \
    -g diffuse1D_periodic \
    -F trials \
    --param metrics=all \
    --param other_params=test-pde1 \
    --param grid_params=rel_noise \
    --param grid_vals=rel_noise \
    --param grid_decisions=plot2 \
    --param series_params=kalman-auto3 \
    --param +plot_prefs=test-absrel3 \
    --param +skinny_specs=duration-noise &> diffuse1D_periodic.log &

nohup mitosis gen_experiments.gridsearch \
    -e seed=19 \
    -g burgers1D_periodic \
    -F trials \
    --param metrics=all \
    --param other_params=test-pde1 \
    --param grid_params=rel_noise \
    --param grid_vals=rel_noise \
    --param grid_decisions=plot2 \
    --param series_params=kalman-auto3 \
    --param +plot_prefs=test-absrel3 \
    --param +skinny_specs=duration-noise &> burgers1D_periodic.log &

nohup mitosis gen_experiments.gridsearch \
    -e seed=19 \
    -g ks_periodic \
    -F trials \
    --param metrics=all \
    --param other_params=test-pde2 \
    --param grid_params=rel_noise \
    --param grid_vals=rel_noise \
    --param grid_decisions=plot2 \
    --param series_params=kalman-auto3 \
    --param +plot_prefs=test-absrel3 \
    --param +skinny_specs=duration-noise &> ks_periodic.log &
