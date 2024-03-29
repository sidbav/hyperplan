# HyperPlan: Motion Planning Hyperparameter Optimization

HyperPlan is a tool for automatic selection of a motion planning algorithm and
its parameters that optimize some performance metric over a given set of
problems.

It uses [HpBandSter](https://github.com/automl/HpBandSter) as the underlying
optimization package.

## Installation

Run the following commands:

    sudo apt-get install python3.8-dev python3.8-venv
    python3.8 -m venv venv
    source venv/bin/activate
    pip install --isolated -r requirements.txt

### OMPL.app benchmarking

Build a recent version of [OMPL.app](http://ompl.kavrakilab.org)
somewhere. Make sure that `ompl_benchmark` is somewhere in the $PATH.

### MoveIt benchmarking

TODO

### Robowflex benchmarking

1. [Install ROS Melodic](http://wiki.ros.org/melodic/Installation/Ubuntu) and these build tools:

         sudo apt-get install python-wstool python-catkin-tools

2. Check out the code:

         export CATKIN_WS=~/ws_hyperplan
         mkdir -p $CATKIN_WS/src
         cd $CATKIN_WS/src
         wstool init .
         git clone git@github.com:KavrakiLab/hyperplan.git
         wstool merge $CATKIN_WS/src/hyperplan/hyperplan.rosinstall
         wstool update

3. Configure and build the code:

         cd $CATKIN_WS
         catkin config --extend /opt/ros/$ROS_DISTRO \
           --cmake-args -DCMAKE_BUILD_TYPE=Release -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
         rosdep install -y --from-paths src --ignore-src --rosdistro $ROS_DISTRO
         catkin build

4. Source the workspace.

         source $CATKIN_WS/devel/setup.bash

## Running the optimization

Below are some examples on how to run the command line tool to optimize for
different objectives using different backends.

### OMPL.app benchmarking

Find a planner configuration that optimizes speed of geometric planning:

    ./examples/speed.sh

Find a planner configuration that optimizes speed of kinodynamic planning:

    ./examples/speed_kinodynamic.sh

Find a planner configuration that optimizes convergence rate of asymptotically
(near-)optimal geometric planning:

    ./examples/convergence.sh

Type `./scripts/hyperplan.py --help` to see all options. See the shared
directory for the result files. See the scripts `./scripts/analysis.py` and
`./scripts/hyperplanvis.{py,R}` for examples of how to perform some basic
analysis of the results.

### MoveIt

TODO

### Robowflex benchmarking

Find planner configuration that optimizes speed of geometric planning for the
Fetch arm and torso using 10 scenes and corresponding motion planning queries:

    ./examples/robowflex_speed.sh

Note the format in the `examples/fetch` directory:

- There is an equal number of scene and motion planning request YAML files. The
  scenes are all the files that match the glob pattern `*scene*.yaml`, while
  the requests are the files that `*request*.yaml`. The aggregate performance
  across all the planning problems is optimized.
- The `ompl_planning.yaml` file is a minimal template of the
  `ompl_planning.yaml` file that is normally found in the
  `<robot>_moveit_config` package for a robot. The only things you'd have to
  change for a different robot are the planning group and the projection.

# Docker
## Build Docker
run the following command:

```
docker build -t hyperplan .
```

## Run Docker
Run the following command 
To run the docker container run the following command:
```
./start_docker.sh
```

Before running any of the benchmarks, make sure to create a `.env` file, follow the `EXAMPLE.env` file as a guide.


## Run Benchmarks 
run the following command:
```
cd src/hyperplan
./run.sh -c <PATH_TO_CONFIG_FILE> -n <NUM_WORKERS> -r <RUN_ID>
```

To access log:
```
tail -f nohup.out
```

The results will be saved in the directory where the hyperplan-fetch file is stored.

## Kill Python Processes:
```
ps aux
pgrep python3
kill -9 `pgrep python3`
```
## Run Test:
```
cd src/hyperplan
./run_test.sh -c <PATH_TO_CONFIG_FILE> -r <RUN_ID>
```

To access test log:
```
tail -f test_nohup.out
```

## Run Analysis:
```
export PATH=${HOME}/bin:${PATH}
source /ws_hyperplan/devel/setup.bash
source /ws_hyperplan/venv/bin/activate

cd /hyperplan/scripts
python3 analysis.py /ws_hyperplan/src/hyperplan/hyperplan-fetch/results/box_pick/execution_time/0
```
## R analysis:
```
sudo apt install r-base
R
install.packages("ggplot2")
Rscript ./scripts/hyperplan_vis.R ./hyperplan-fetch/results/box_pick/iteration/5
```