
def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # got i in range(length) add weights[i] to a HT
    #
    d = {v:i for i, v in enumerate(weights)}
    for i,v in enumerate(weights):

        if (limit - v) in d:
            return [i,d[limit - v] ] if i > d[limit - v] else [d[limit - v], i ]

    return None
print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))