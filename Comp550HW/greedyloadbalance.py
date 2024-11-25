def greedy_load_balancing(job_loads, num_machines):
    # Initialize machines with 0 load
    machine_loads = [0] * num_machines
    
    # Assign each job to the machine with the smallest load
    for job in job_loads:
        # Find the machine with the minimum load and assign the job
        min_machine = machine_loads.index(min(machine_loads))
        machine_loads[min_machine] += job
    
    # The makespan is the maximum load across all machines
    makespan = max(machine_loads)
    return makespan

# Input values
l = [20, 66, 93, 19, 79, 18, 39, 59, 78, 99, 35, 91, 82, 38, 57, 95, 70, 64, 24, 31, 47, 68, 52, 32, 67, 32, 92, 45, 64, 51, 28, 74, 60, 49, 62, 79, 73, 18, 49, 97, 18, 36, 21, 42, 48, 45, 77, 57, 33, 24, 15, 82, 95, 67, 37, 59, 81, 82, 96, 61, 53, 95, 38, 80, 74, 53, 61, 65, 48, 85, 28, 43, 65, 10, 55, 83, 63, 46, 47, 42, 23, 26, 30, 37, 26, 68, 12, 31, 44, 27, 88, 86, 10, 45, 93, 28, 81, 79, 10, 21]
m = 10

# Compute the makespan
makespan = greedy_load_balancing(l, m)
print(f"The makespan of the resulting assignment is: {makespan}")
