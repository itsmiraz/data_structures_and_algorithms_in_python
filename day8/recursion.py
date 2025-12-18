#  Print an arrow 4 times

# class Solution :

count = 0


def func():
    if count == 4:
        return
    print('Arrow')
    count += 1
    func()


func()
