import time
from timeit import default_timer as timer

def run_tasks(task_name, seconds): 
    print(f"{task_name} started at {timer()}")
    time.sleep(seconds)
    print(f"{task_name} completed at {timer()}")

start=timer()
run_tasks('task1', 2)
run_tasks('task2', 1)
run_tasks('task3', 3)

print(f"\ntotal time to complete: {timer()-start:.2f}")

# output: task1 started at 92964.2354736
# task1 completed at 92966.2363846
# task2 started at 92966.2365998
# task2 completed at 92967.2367422
# task3 started at 92967.2372065
# task3 completed at 92970.2410507

# total time to complete: 6.01

