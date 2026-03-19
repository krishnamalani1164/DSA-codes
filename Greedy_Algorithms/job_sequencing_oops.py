def job_sequencing(jobs):
    # Sort jobs in descending order of profit
    jobs.sort(key=lambda x: x[2], reverse=True)  # x[2] is profit

    n = len(jobs)
    max_deadline = max(job[1] for job in jobs)  # job[1] is deadline

    # Create time slots, initialized as False (free)
    slots = [False] * (max_deadline + 1)

    job_sequence = [''] * (max_deadline + 1)
    total_profit = 0

    for job in jobs:
        job_id, deadline, profit = job

        # Find a free slot from deadline to 1
        for t in range(min(deadline, max_deadline), 0, -1):
            if not slots[t]:
                slots[t] = True
                job_sequence[t] = job_id
                total_profit += profit
                break

    # Filter out empty slots and return result
    scheduled_jobs = [job_id for job_id in job_sequence if job_id != '']
    return scheduled_jobs, total_profit

# Example usage
jobs = [
    ('a', 2, 100),
    ('b', 1, 19),
    ('c', 2, 27),
    ('d', 1, 25),
    ('e', 3, 15)
]

result, profit = job_sequencing(jobs)
print("Scheduled Jobs:", result)
print("Total Profit:", profit)
