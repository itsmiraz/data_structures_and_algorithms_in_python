

# Head recursion

# class Solution:
def func(x, n):

    if n == 0:
        return
    print(x)
    func(x, n-1)


# func(15, 4)

def func2(n):
    if n == 0:
        return
    func2(n-1)
    print(n)


func2(4)
