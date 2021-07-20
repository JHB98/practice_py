# -*- coding: euc-kr -*-
import re


def makePostfix(numbers, operators):
    prec = {'*': 1, '/': 1, '+': 0, '-': 0}
    stack = []
    postfixlist = []
    numIndex = 0
    operIndex = 0
    while True:
        postfixlist.append(numbers[numIndex])
        numIndex += 1
        if numIndex == 4:
            break
        if not stack:
            stack.append(operators[operIndex])
            operIndex += 1
        else:
            while stack:
                ref = stack.pop()
                if(prec[ref] >= prec[operators[operIndex]]):
                    postfixlist.append(ref)
                else:
                    stack.append(ref)
                    break

            stack.append(operators[operIndex])
            operIndex += 1

    while stack:
        postfixlist.append(stack.pop())
    return postfixlist


def tokenize(expr):
    numbers = re.findall("\d+", expr)
    operators = re.findall("[*/+-]", expr)
    return numbers, operators


def calculate(postfixlist):
    stack = []
    for token in postfixlist:
        if token == '*':
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            stack.append(num2*num1)
        elif token == '/':
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            stack.append(int(num2/num1))
        elif token == '+':
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            stack.append(num2+num1)
        elif token == '-':
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            stack.append(num2-num1)
        else:
            stack.append(token)

    return stack.pop()


def main():
    expr = input("Input expression : ")
    numbers, operators = tokenize(expr)
    postfixlist = makePostfix(numbers, operators)
    result = calculate(postfixlist)
    print(result)


if __name__ == '__main__':
    main()
