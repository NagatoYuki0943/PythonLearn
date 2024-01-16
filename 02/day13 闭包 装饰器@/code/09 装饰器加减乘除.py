
def func_out(func):
	def func_in(*args, **kwargs):
		return func(*args, **kwargs)

	return func_in



@func_out
def add(*args, **kwargs):
	res = 0
	for i in args:
		res += i

	return res


@func_out
def sub(*args, **kwargs):
	res = 0
	for i in args:
		res -= i

	return res


@func_out
def mul(*args, **kwargs):
	res = 1
	for i in args:
		res *= i

	return res


@func_out
def div(*args, **kwargs):
	res = 1
	for i in args:
		res /= i

	return res

print(add(1, 2, 3))     # 6
print(sub(1, 2, 3))     # -6
print(mul(1, 2, 3))     # 6
print(div(1, 2, 3))     # 0.16666666666666666