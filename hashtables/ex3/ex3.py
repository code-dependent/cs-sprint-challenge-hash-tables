def intersection(arrays):
    """
    YOUR CODE HERE
    Plan:
        0. I can create a dict and for each num in the first list add it as a key
           and the value should be 1 (because its been seen in one list)
        1. Loop through the 2D array and for each num that IS in intersection_dict,
           increment intersection_dict[num]
        2. Now we can loop through the intersections_dict and for each value
           that is equal to the length of 2d array, add it to a rtn list and
        3. return rtn_list
    """
    # Your code here
    intersection_dict = {v:1 for v in arrays[0]}
    for i in range(1,len(arrays)):
        for n in arrays[i]:
            if n in intersection_dict:
                intersection_dict[n]+=1

    return [k for k,n in intersection_dict.items() if n == len(arrays)]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
