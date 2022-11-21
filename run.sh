#/bin/bash
export PATH=${HOME}/bin:${PATH}
source /ws_hyperplan/devel/setup.bash
source /ws_hyperplan/venv/bin/activate
cd /ws_hyperplan/src/hyperplan

# A POSIX variable
OPTIND=1         # Reset in case getopts has been used previously in the shell.

show_help() {
	echo "Usage: ./run.sh -c <CONFIG_FILE> -n <NUM_WORKERS> -r <RUN_ID>"
	echo -e "\t c: Config file to run, MUST be passed in"
	echo -e "\t n: Number of workers, default value 8"
	echo -e "\t r: Run id: default value 0"
	echo -e "\n"
}
num_workers=8
run_id=0
config=""

while getopts "h?c:n::r::" opt; do
  case "$opt" in
    c) config="${OPTARG}"
      ;;
    n)  num_workers=$OPTARG
      ;;
    r)  run_id=$OPTARG
      ;;
    h|\?)
      show_help
      exit 0
      ;;
  esac
done

if [ "$config" = "" ];
then
	show_help
	exit 2
fi

worker=
for i in `seq ${num_workers}`; do
    (nohup ./scripts/hyperplan_cmdline.py --run_id ${run_id} --n_workers ${num_workers} ${worker} "${config}" ) &
    worker='--worker'
done
