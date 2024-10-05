# An example module

# One function
def odd_numbers(n=10):
    for i in range(1,n+1):
        if i % 2 == 1:
            print(i)

# Another function          
def even_numbers(n):
    for i in range(1,n+1):
        if i % 2 == 0:
            print(i)
