import numpy as np

N = int(input())

nums = np.arange(1, N + 1).astype(str)

nums[2::3] = "Fizz"
nums[4::5] = "Buzz"
nums[14::15] = "FizzBuzz"

print(*nums)
