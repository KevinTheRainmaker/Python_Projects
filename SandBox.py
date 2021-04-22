# import random
# for i in range(5):
#     print(random.randint(0,30))
-----------
word = 'a4b3cdef5gh9'
word_list = list(word)
print(word_list)

x= ['a','b','c','d','e','f','g','h']
new_word_list = [int(p) for p in word_list if p not in x]

print(new_word_list)

answer = 0
for num in new_word_list:
    answer += num

print(answer)