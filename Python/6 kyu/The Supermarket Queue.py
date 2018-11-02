def queue_time(customers, n):
    queue = [0] * n
    for i in customers:
        queue[queue.index(min(queue))] += i
    return max(queue)
