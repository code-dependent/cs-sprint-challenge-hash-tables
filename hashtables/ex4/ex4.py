def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    pos_dict = {n:i for i,n in enumerate(a) if n > 0}
    rtn = []
    for n in a:
        if n*-1 in pos_dict:
            rtn.append(n*-1)
    return rtn


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
