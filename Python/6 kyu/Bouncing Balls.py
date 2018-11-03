def bouncingBall(h, bounce, window):
    if h > 0 and 0 < bounce < 1 and window < h:
        h_bounce = h
        counter = 1
        while h_bounce > window:
            h_bounce *= bounce
            counter += 2 * (h_bounce > window)
        return counter
    return -1
