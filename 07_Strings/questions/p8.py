# CamelCase to snake_case

my_string = "HelloWorldHowAreYou"
result = ""
for ch in my_string:
    if ch.isupper():
        result += "_" + ch.lower()
    else:
        result += ch
if result[0] == "_":
    result = result[1:]
print(result)
