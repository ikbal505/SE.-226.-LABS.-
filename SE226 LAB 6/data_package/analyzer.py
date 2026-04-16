def calculate_mean(num_list):
    if len(num_list) == 0:
        return None
    return round(sum(num_list) / len(num_list), 2)

def find_maximum(num_list):
    if len(num_list) == 0:
        return None
    return max(num_list)

def find_minimum(num_list):
    if len(num_list) == 0:
        return None
    return min(num_list)