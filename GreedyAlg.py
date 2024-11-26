def select_compatible_intervals(intervals):
    # Sort intervals based on the finishing times (second element of each interval)
    intervals.sort(key=lambda x: x[1])

    selected_intervals = []
    
    # The finish time of the last selected interval (initialize to a very small value)
    last_finish_time = float('-inf')
    
    # Greedily select intervals
    for interval in intervals:
        start, finish = interval
        if start > last_finish_time:
            selected_intervals.append(interval)
            last_finish_time = finish  # Update the last finish time to the current interval's finish time

    return selected_intervals

# Example instance A
A =  [[4, 36], [17, 147], [5, 18], [62, 67], [16, 32], [96, 128], [21, 117], [19, 122], [64, 168], [45, 99], [12, 55], [20, 26], [79, 126], [3, 9], [89, 101], [55, 112], [26, 157], [1, 2], [16, 116], [49, 70], [26, 60], [52, 153], [16, 28], [20, 83], [158, 166], [3, 7], [7, 8], [61, 140], [1, 4], [12, 170], [19, 57], [35, 110], [54, 155], [93, 137], [47, 58], [49, 114], [115, 174], [60, 61], [64, 90], [3, 142], [4, 145], [89, 119], [24, 76], [22, 154], [63, 108], [8, 27], [26, 49], [18, 77], [106, 175], [2, 87], [7, 148], [65, 66], [36, 135], [17, 118], [96, 130], [38, 171], [4, 40], [24, 38], [22, 132], [129, 144]]

# Run the greedy algorithm to select compatible intervals
compatible_intervals = select_compatible_intervals(A)

print("Selected intervals:", compatible_intervals)
