#/bin/bash
source ${HOME}/ws_hyperplan/devel/setup.bash
source ${HOME}/ws_hyperplan/venv/bin/activate
cd ${HOME}/ws_hyperplan/src/hyperplan

outdir=${HOME}/Bubox/archive/mark_moll/hyperplan/convergence
num_workers=8
run_id=${1:-0}
worker=

for i in `seq ${num_workers}`; do
    (nohup ./scripts/hyperplan_cmdline.py --run_id ${run_id} --n_workers ${num_workers} --shared_directory ${outdir} --n_iterations 7 --min_budget .33333333333 --max_budget 729 --backend omplapp --opt opt ${worker} examples/Barriers.cfg examples/Home.cfg >> convergence.log) &
    worker='--worker'
done
