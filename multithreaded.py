################################################################################
# Thread pool pattern opportunity
#
# Purpose: The below code simulates a situation where we have "bursts" made up
# of some number of jobs that need to be done, where the precise number
# of jobs varies between 0-20 for each burst, and all the jobs in one burst
# must be completed before moving on to the next.  Completing a job is done
# by calling the do_job method.  The jobs can be run concurrently without any
# regard to race conditions.
#
# In the below code, we use multithreading to improve the performance of
# executing bursts of jobs.  There is an opportunity to use a thread pool
# instead.
#
#
# Author: Kevin Browne
# Contact: brownek@mcmaster.ca
#
################################################################################

import threading
from queue import Queue
from random import random
from time import sleep
import timeit

# DO NOT MODIFY do_job: Simulates doing some job with sleep(), adds 1 to
# queue for keeping track of the number of do_job calls
def do_job(output_queue,id):
    sleep(0.0001)
    output_queue.put(1)

# DO NOT MODIFY the function name or add any arguments
def execute():

    # DO NOT MODIFY THESE TWO STATEMENTS
    BURSTS = 1000
    queue = Queue()

    # DO NOT MODIFY THE LOOP RANGE: run through the 1000 bursts of activity
    for i in range(0, BURSTS):

        # DO NOT MODIFY THIS STATEMENT: Generate a random number of jobs to be
        # done concurrently by calling do_job, this batch of jobs must all be
        # completed before moving on to the next batch (i.e. next BURSTS loop
        # iteration).
        job_total = int(round((random() * 20), 0))

        # You will need to modify the below code to use a thread pool. You
        # will have to make other modifications in other places in this file,
        # such as importing the relevant module, and deciding where in this
        # file it makes sense to instantiate the thread pool executor itself.

        jobs = []
        for j in range(0, job_total):
            thread = threading.Thread(target=do_job,args=(queue,j))
            jobs.append(thread)
            thread.start()

        for j in jobs:
            j.join()

    # DO NOT MODIFY THIS STATEMENT: output number of do_job calls
    print(queue.qsize())

# DO NOT MODIFY THESE TWO STATEMENTS: run a test of how long it takes to
# execute the method
test = timeit.timeit(execute, number=1)
print("Test result: " + str(test) + "s")
