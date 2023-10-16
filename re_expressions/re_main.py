import re

string_input = 'Он --- серо-буро-малиновая редиска!! >>>:->  А не кот. www.kot.ru'
# r'[АВЕКМНОРСТУХ]'

print(len(re.split(r'\W+', string_input)))
print(re.split(r'\W+', string_input))
