# определим функцию, которая будет делать всю работу
def calculate_ops(ops):
    # в качестве стека будем использовать обычный питоновский список
    stack = []
    # перебираем все элементы ops и вычисляем значение в соответствии с алгоритмом
    operations = ['+', '-', '*', '/', '**']
    calculations = {
        operations[0]: lambda x, y: x + y,
        operations[1]: lambda x, y: x - y,
        operations[2]: lambda x, y: x * y,
        operations[3]: lambda x, y: x // y,
        operations[4]: lambda x, y: x ** y
    }
    for element in ops:
        if element.isdigit():
            stack.append(int(element))
        else:
            if len(stack) < 2:
                return "error"
            x = stack.pop()
            y = stack.pop()
            calculate = calculations[element]
            n = calculate(y, x)
            stack.append(n)

    # после того, как все прочитано, на стеке должно быть ровно одно значение - результат
    # если это так, то возвращаем его, иначе возвращаем ошибку
    if len(stack) == 1:
        return stack[0]
    return "error"

if __name__ == '__main__':
    # считываем строку и делим ее на лексемы
    ops = input().split()

    # вычисляем результат и печатаем его
    result = calculate_ops(ops)
    print(result)