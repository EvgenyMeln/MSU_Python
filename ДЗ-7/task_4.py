import numpy as np

start = float(input())
end = float(input())
N = int(input())

nums = np.linspace(start, end, N)

nums[::7] = nums[::7]/3
nums[4::7] = nums[4::7]*2

formatted_nums = [f"{x:.2f}" for x in nums]

for number in formatted_nums:
    print(number)
