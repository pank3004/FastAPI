import asyncio
from timeit import default_timer as timer

async def run_tasks(task_name, seconds): 
    print(f"{task_name} started at: {timer()}")
    await asyncio.sleep(seconds)  # pause here and come back when this operatin is done
    print(f"{task_name} completed at: {timer()}")


async def main(): 
    start=timer()
    await asyncio.gather(  #asyncio.gather(): Starts all tasks at the same time, Runs them concurrently, Waits until all finish
        run_tasks('Task1', 2),
        run_tasks('Task2', 1),
        run_tasks('Task3', 3)
    )
    print(f"\ntotal time taken: {timer()-start:.2f} s")

asyncio.run(main())


# output: 

# Task1 started at: 93132.9803376
# Task2 started at: 93132.9805381
# Task3 started at: 93132.9806546
# Task2 completed at: 93133.990003
# Task1 completed at: 93134.9889526
# Task3 completed at: 93135.9811456

# total time taken: 3.00 s