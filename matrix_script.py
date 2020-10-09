import re

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

text_as_columns = []
for i in range(m):
    text_as_columns.append("".join([matrix_item[i] for matrix_item in matrix]))

whole_text = "".join(text_as_columns)
pattern = re.compile(r"([A-Za-z0-9])[^A-Za-z0-9]+([A-Za-z0-9])")
result = pattern.sub(r"\1 \2", whole_text)
print(result)
