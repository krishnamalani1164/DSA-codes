def max_activities(start, end):
    activities = sorted(zip(start, end), key=lambda x: x[1])
    count = 1
    last_end = activities[0][1]

    for i in range(1, len(activities)):
        if activities[i][0] >= last_end:
            count += 1
            last_end = activities[i][1]
    return count

# Example usage
start = [1, 2, 0, 5, 8, 5, 3, 6]
end   = [3, 5, 6, 9, 9, 7, 5, 10]
print("Maximum number of activities:", max_activities(start, end))
