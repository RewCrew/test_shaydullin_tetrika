def task(array:str):
    result = array.find('0')
    return result
# входной массив - строка чисел

def task1(array:list):
    result = array.index(0)
    return result
# входной массив - список чисел

print(task("111111111110000000000000000"))
print(task1([1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0]))