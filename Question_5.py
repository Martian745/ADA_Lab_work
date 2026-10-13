
def fractional_knapsack(weights, values, capacity):
    items = sorted(
        zip(weights, values),
        key=lambda x: x[1] / x[0],
        reverse=True
    )

    total_profit = 0.0

    for weight, value in items:
        if capacity == 0:
            break

        if weight <= capacity:
            total_profit += value
            capacity -= weight
        else:
            total_profit += value * (capacity / weight)
            capacity = 0

    return total_profit


# Main program
weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))
capacity = int(input("Enter knapsack capacity: "))

profit = fractional_knapsack(weights, values, capacity)
print("Maximum profit:", profit)

#Job Scheduling Function

from typing import NamedTuple, List

class Job(NamedTuple):
    job_id: int
    deadline: int
    profit: int


def job_scheduling(jobs: List[Job]) -> List[int]:
    jobs = sorted(jobs, key=lambda job: job.profit, reverse=True)

    max_deadline = max((job.deadline for job in jobs), default=0)
    slots = [None] * (max_deadline + 1)

    for job in jobs:
        for t in range(min(job.deadline, max_deadline), 0, -1):
            if slots[t] is None:
                slots[t] = job.job_id
                break

    return [job_id for job_id in slots[1:] if job_id is not None]


# Main program
n = int(input("Enter number of jobs: "))
jobs = []

for i in range(n):
    job_id = int(input("Enter job ID: "))
    deadline = int(input("Enter deadline: "))
    profit = int(input("Enter profit: "))
    jobs.append(Job(job_id, deadline, profit))

sequence = job_scheduling(jobs)
print("Optimal job sequence:", sequence)

profit_map = {job.job_id: job.profit for job in jobs}
total_profit = sum(profit_map[job_id] for job_id in sequence)
print("Maximum profit:", total_profit)
