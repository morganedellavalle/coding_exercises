################## DAY 4 #####################
from collections import Counter

min_code = 256310
max_code = 732736
count = 0

for i in range(min_code, max_code+1):
    i_str = str(i)
    
    if len(i_str) != 6:
        continue
    if i_str[0] > i_str[1] or i_str[1] > i_str[2] or i_str[2] > i_str[3] or i_str[3] > i_str[4] or i_str[4] > i_str[5]:
        continue

    if i_str[0] != i_str[1] and i_str[1] != i_str[2] and i_str[2] != i_str[3] and i_str[3] != i_str[4] and i_str[4] != i_str[5]:
        continue
    else:
        number_occurences = Counter(i_str)
        if 2 not in number_occurences.values():
            continue
    count +=1

print(max_code - min_code)
print(count)