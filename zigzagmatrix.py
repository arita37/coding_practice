def zigzag(n):
    """Return dictionary of elements accessed in the zigzag order"""

    # initialize list of indices for each element
    # sort on sum of the coordinates for diagonals
    # then on the 
    idx_list = [(x, y) for x in xrange(n) for y in xrange(n)]
    idx_order = sorted(idx_list,
                       key = lambda (x,y): (x+y, y if (x+y) % 2 == 0 else -y))

    for x in range(n):
        for y in range(n):
                print "%3d" % idx_order.index((x,y)),
        print
 
zigzag(4)
