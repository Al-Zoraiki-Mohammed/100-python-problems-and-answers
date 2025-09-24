
"""Task66"""

def get_distinct(array):
    return list(set(array))


def get_dist(array):
    """Alternative solution without using sets"""
    dist_array = []
    for element in array:
       if element not in dist_array:
           dist_array.append(element)
    return dist_array


if __name__ == "__main__":
    array = [1,1,2,2,3,3,4,4,5,5]
    dist_array = get_distinct(array)
    dist_arr = get_dist(array)

    print(array, dist_array, dist_arr)
