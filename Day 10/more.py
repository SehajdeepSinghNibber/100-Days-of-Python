def function_1(text):
    return text+text
def function_2(text):
    doubled=function_1(text)
    return doubled.title()

output=function_2("hello")
print(output)