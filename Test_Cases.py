
def square(x):
    return x*x

assert(sorted([1,7,4] == [1,4,7]) #True
assert(square(3) == 9) #True, Nothing happens
assert(square(3) == 8) #False, Runtime Error (AssertError)
####################################################################
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = dsquared**0.5
    return result

assert distance(1, 2, 1, 2) == 0
assert distance(1,2, 4,6) == 5
assert distance(0,0, 1,1) = 2*(0.5)^2