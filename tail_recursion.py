def tail_recursion(n,result):
	if n==0:
		return result
	return tail_recursion(n-1,n*result)

print(tail_recursion(0,1))
print(tail_recursion(1,1))
print(tail_recursion(2,1))
print(tail_recursion(5,1))
print(tail_recursion(8,1))
print(tail_recursion(10,1))
print(tail_recursion(1000,1))