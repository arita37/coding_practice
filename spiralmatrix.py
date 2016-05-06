def spiral(n):
    """Print out spiral matrix starting from the top left corner clockwise"""

    dx = 1          # start moving right
    dy = 0          
    x, y = 0, 0     # Starting location top left
    
    array = [[None] * n for i in xrange(n)]   # initialize array as None's

    # total number of steps = size of matrix
    for i in xrange(n ** 2):
        array[x][y] = i
        x_next = x + dx
        y_next = y + dy

        # if not at a corner (0,0), (n,0), (0,n), (n,n)
        # and the next step is None, then continue spiraling
        if 0 <= x_next < n and 0 <= y_next < n and array[x_next][y_next] == None:
            x = x_next
            y = y_next

        # if at a corner or if the next element has already been populated
        # change directions
        else:
            dx, dy = -dy, dx
            x += dx
            y += dy

    for y in xrange(n):
        for x in xrange(n):
            print "%3d" % array[x][y],
        print
 
spiral(6)
