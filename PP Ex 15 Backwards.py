# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

#   My name is Michele
# Then I would see the string:
#   Michele is name My

string1 = "Porky is the name of a famous pig."
word_list = string1.split()
print(word_list)
# num_words = len(word_list)
# for i in range((num_words - 1), -1, -1):
#     # print(i)
#     print(word_list[i], end=" ")

# Reverse the list using slicing ---> [::-1]
reversed_list = word_list[::-1]  # but this creates another list
print(reversed_list)  # ['fun', 'is', 'Python']

for word in reversed(
    word_list
):  # use the 'reversed' function to avoid creating another list
    print(word, end=" ")
