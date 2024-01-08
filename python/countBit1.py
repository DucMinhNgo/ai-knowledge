input_string = '010101010101'
substring_counts = {}

for i in range(len(input_string)):
  for j in range(i + 1, len(input_string)):
    substring = input_string[i:j + 1]
    if substring not in substring_counts:
      substring_counts[substring] = 0
    substring_counts[substring] += 1

big_obj = {substring: count for substring, count in substring_counts.items() if count > 1}
print(big_obj)