fib=[0,1]
for i in range(5):
    fib.append(fib[-2]+fib[-1])
print(fib)