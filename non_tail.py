def factorial_non_tail(n):
	if n==0:
		return 1
	return n*factorial_non_tail(n-1)

print(factorial_non_tail(0))
print(factorial_non_tail(1))
print(factorial_non_tail(2))
print(factorial_non_tail(5))
print(factorial_non_tail(8))
print(factorial_non_tail(10))
print(factorial_non_tail(1000))