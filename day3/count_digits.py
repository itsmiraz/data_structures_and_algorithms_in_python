
n = 587323232309823092378970323421980721347908321470432701932419073124097341207934217091234790
count = 0
while n > 0:
    count += 1
    n = n//10

print('c', count)
# Time Complexity of this part will be => O(log5(n)) where n is the constant
# Space Complexity => O(1)
