def max_profit(jobs):
    # jobs: list of tuples (deadline, profit)
    
    # Sort jobs by profit descending
    jobs.sort(key=lambda x: x[1], reverse=True)

    profit = jobs[0][1]
    safe_deadline = 2

    for i in range(1, len(jobs)):
        if jobs[i][0] >= safe_deadline:
            profit += jobs[i][1]
            safe_deadline += 1

    print("Max profit from jobs:", profit)


# Example usage
jobs = [
    (2, 100),
    (1, 19),
    (2, 27),
    (1, 25),
    (3, 15)
]

max_profit(jobs)