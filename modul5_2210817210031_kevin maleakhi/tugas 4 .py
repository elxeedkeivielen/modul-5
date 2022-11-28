def reverse(x,reverse = 0):
    reverse = 0
    while (x != 0):
        reverse *= 10
        reverse += x % 10
        x //= 10
    return reverse 
x,y = input().split()
x=reverse(int(x))
y=reverse(int(y))
z= x + y
print(reverse(z))
