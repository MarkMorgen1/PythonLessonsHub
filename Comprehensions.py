# List Comprehension
# Create a list using name for each item in names if the name starts with M.
# new_list = [new_value 'for' list_item 'in' full_list 'if' (list_item meets condition)]
names = ["Mark", "Cindy", "Mara"]
print(names)
m_names = [n for n in names if n.startswith("M")]
print(m_names)

nums = [1, 2, 3, 4]
# new_val = n^2
nums_sqd = [n**2 for n in nums if n >= 3]
print(nums_sqd)
