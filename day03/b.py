import os

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    data = f.read().strip().split()

def most_common(l):
    return max("1", "0", key=l.count)

# part 1
gamma = int(''.join(map(most_common, zip(*data))), 2)
epsilon = ~gamma & 0xFFF

print(gamma * epsilon)

# part 2
def get_ls_rating(co2):
    nums = data.copy()
    for i in range(12):
        get_curr_char = lambda x: x[i]
        best = most_common(list(map(get_curr_char, nums)))
        if co2:
            best = "0" if int(best) else "1"

        for j in nums.copy():
            if j[i] != best:
                nums.remove(j)
        
        if len(nums) == 1:
            return int(nums[0], 2)

print(get_ls_rating(False) * get_ls_rating(True))
