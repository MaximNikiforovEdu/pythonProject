def shunting_yard(string):
    stack = []
    res = ''
    priority = {"+":0, "-":0, "*":1, "/":1, "**":2}
    if string[-1] in priority:
        return "error"
    for s in string:
        if s.isdigit():
            res += s + ' '
        elif s == "(":
            stack.append(s)
        elif s == ")":
            if stack == []:
                return "error"
            x = stack.pop()
            while x != "(":
                res += x + ' '
                if stack == []:
                    return "error"
                x = stack.pop()
        elif s in priority:
            if stack == [] or stack[-1] == "(" or s == '**' or priority[stack[-1]] < priority[s]:
                stack.append(s)
            else:
                while stack and priority[stack[-1]] >= priority[s]:
                    x = stack.pop()
                    res += x + ' '
                stack.append(s)
        else:
            return "error"
    while stack:
        x = stack.pop()
        if x == "(":
            return "error"
        res += x + ' '
    return res


if __name__ == '__main__':
    string = input().split()
    print(shunting_yard(string))