# -*- coding: euc-kr -*-
def main():
    shape = input("Input shape : ")
    line1 = [1, 2, 5, 2, 9]
    line2 = [4, 1, 1, 1, 4, 1, 1, 6, 1]
    line3 = [1, 2, 2, 1, 2, 2, 1, 2, 1, 4, 1, 1]
    line4 = [1, 2, 3, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1]
    line5 = [1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 2, 1, 1, 1]
    line6 = [5, 1, 2, 1, 3, 1, 6, 1]
    line7 = [5, 1, 2, 1, 10, 1]
    line8 = [8, 5]
    lines = [line1, line2, line3, line4, line5, line6, line7, line8]
    checkList = [False, True, False, True, False, False, False, False]
    index = 0
    for line in lines:
        check = checkList[index]
        for num in line:
            for point in range(0, num*4):
                if check:
                    print(shape, end='')
                else:
                    print(' ', end='')
            if check:
                check = False
            else:
                check = True
        index += 1
        print('\n')


if __name__ == '__main__':
    main()
