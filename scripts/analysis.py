#!/usr/bin/env python
######################################################################
# Software License Agreement (BSD License)
#
#  Copyright (c) 2020, Rice University
#  All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions
#  are met:
#
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above
#     copyright notice, this list of conditions and the following
#     disclaimer in the documentation and/or other materials provided
#     with the distribution.
#   * Neither the name of Rice University nor the names of its
#     contributors may be used to endorse or promote products derived
#     from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
#  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
#  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
#  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
#  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
#  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
#  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#  POSSIBILITY OF SUCH DAMAGE.
######################################################################

# Author: Mark Moll

import sys
import matplotlib.pyplot as plt
import hpbandster.core.result as hpres
import hpbandster.visualization as hpvis
from os import path

def analyze(dir):
    # load the example run from the log files
    result = hpres.logged_results_to_HBS_result(dir)
    # get all executed runs
    all_runs = result.get_all_runs()
    # get the 'dict' that translates config ids to the actual configurations
    id2conf = result.get_id2config_mapping()
    # Here is how you get he incumbent (best configuration)
    inc_id = result.get_incumbent_id()
    # let's grab the run on the highest budget
    inc_runs = result.get_runs_by_id(inc_id)
    inc_run = inc_runs[-1]
    # We have access to all information: the config, the loss observed during
    #optimization, and all the additional information
    inc_loss = inc_run.loss
    inc_config = id2conf[inc_id]['config']
    
    #print(inc_run.info.keys())
    #inc_test_loss = inc_run.info['test accuracy']
    
    print('Best found configuration with loss =', {inc_loss}, ':')
    print(inc_config)
    #print('It achieved accuracies of %f (validation) and %f (test).'%(1-inc_loss, inc_test_loss))
    
    
    # Let's plot the observed losses grouped by budget,
    hpvis.losses_over_time(all_runs)
    plt.yscale("log")
    plt.savefig(path.join(dir, 'loss_over_time.png'))
    # the number of concurent runs,
    hpvis.concurrent_runs_over_time(all_runs)
    plt.title('Number of Concurrent Runs Over Time')
    plt.savefig(path.join(dir, 'concurrent_runs_over_time.png'))
    # and the number of finished runs.
    hpvis.finished_runs_over_time(all_runs)
    plt.title('Number of Finished Runs Over Time')
    plt.savefig(path.join(dir, 'finished_runs_over_time.png'))
    # This one visualizes the spearman rank correlation coefficients of the losses
    # between different budgets.
    hpvis.correlation_across_budgets(result)
    plt.savefig(path.join(dir, 'correlation_across_budgets.png'))
    # For model based optimizers, one might wonder how much the model actually helped.
    # The next plot compares the performance of configs picked by the model vs. random ones
    hpvis.performance_histogram_model_vs_random(all_runs, id2conf)
    plt.savefig(path.join(dir, 'performance_his_model_vs_random.png'))

if __name__ == "__main__":
    if len(sys.argv)==1:
        print('Usage: {} <results_dir1> [<results_dir2> ...]\n'.format(sys.argv[0]))
        exit(-1)
    for dir in sys.argv[1:]:
        analyze(dir)
