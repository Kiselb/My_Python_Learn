def my_function(a, b):
    return a + b

with open('result.txt', 'a', encoding='utf-8') as file:
    file.write(str(my_function(100, 700)))
    print("File saved")
