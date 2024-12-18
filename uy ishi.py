# 1
# def sum_of_digits(num):
#     return sum(int(digit) for digit in str(abs(num)))
#
# print(sum_of_digits(108))

# ------------------------------------
# 2
# def seconds_to_time(seconds):
#     days = seconds // 86400
#     seconds %= 86400
#     hours = seconds // 3600
#     seconds %= 3600
#     minutes = seconds // 60
#     seconds %= 60
#     return f"{days} kun, {hours} soat, {minutes} minut, {seconds} sekund"
#
# print(seconds_to_time(91000))

# ---------------------------------------------------
# 3
# def capitalize_words(names):
#     return [name.capitalize() for name in names]
#
# names = ['alfred', 'tabitha', 'william', 'arla']
# print(capitalize_words(names))

# ---------------------------------------------
# 4
# def high_scores(scores):
#     return [score for score in scores if score > 75]
#
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# print(high_scores(scores))

# --------------------------------------------------------------
# 5
# def palindromes(words):
#     return [word for word in words if word.lower() == word[::-1].lower()]
#
# words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# print(palindromes(words))

# -------------------------------------------------------------------------------
# 6
# def replace_e_with_3(text):
#     result = ""
#     i = 0
#     while i < len(text):
#         if text[i] == 'e':
#             result += '3'
#         else:
#             result += text[i]
#         i += 1
#     return result
#
# user_input = input("Matn kiriting: ")
# print(replace_e_with_3(user_input))

# ----------------------------------------------------------------------
# 7
# def remove_spaces(text):
#     result = ""
#     i = 0
#     while i < len(text):
#         if text[i] != ' ':
#             result += text[i]
#         i += 1
#     return result
#
# user_input = input("Matn kiriting: ")
# print(remove_spaces(user_input))

# ------------------------------------------------------------------------
# 8
# numbers = [i for i in range(10)]
# doubled = [num * 2 for num in numbers]
# print(doubled)

# -------------------------------------------------------------------------------------
# 9
# import random
#
# random_numbers = [random.randint(1, 100) for _ in range(10)]
# print(random_numbers)