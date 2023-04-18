en = {"aeioulnstr": 1,
      "dg": 2,
      "bcmp": 3,
      "fhvwy": 4,
      "k": 5,
      "jx": 8,
      "qz": 10}
ru = {"авеинорст": 1,
      "дклмпу": 2,
      "бгёья": 3,
      "йы": 4,
      "жзхцч": 5,
      "шэю": 8,
      "фщъ": 10}

en_set = set()
ru_set = set()

# for el in en.keys():
#     for i in el:
#         en_set.add(i)

en_set = [i for el in en.keys() for i in el]  # alternative with generator
ru_set = [i for el in ru.keys() for i in el]  # alternative with generator

print(en_set)
print(ru_set)

word = input("Enter a word: ")
if word[0] in en_set:
    dict = en
else:
    dict = ru

# count = 0
# for key, score in dict.items():
#     for letter in word:
#         if letter.lower() in key:
#             count += score

result = [score for key, score in dict.items()  # alternative with generator
          for letter in word if letter.lower() in key]
count = sum(result)

print("Total score:", count)
