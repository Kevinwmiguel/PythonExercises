"""
Make a program that has a function called counter (), that receives
three parameters: start, end and step.
Your program has to perform three counts using
the created function:
A) 1 to 10, step 1
B) 10 to 1, step 2
C) A custom count

"""

from time import sleep


def line():
    print('-='*20)


def counter(a, b, c):
    line()
    if a == 1 and b == 10:
        print('Count from 1 to 10 step 1')
        for d in range(a, b+1, c):
            sleep(0.2)
            print(f'{d}', end=' ')
        print()
        line()
        print('Count from 10 to 1 Step 2')
        c = -2
        for d in range(b, -1, c):
            sleep(0.2)
            print(f'{d}', end=' ')
    else:
        line()
        if a >= b and b <= 0 or b >= 0:
            if c == 0:
                c = 1
                for d in range(a, b-1, -c):
                    sleep(0.2)
                    print(f'{d}', end=' ', flush=True)
            elif c < 0:

                for d in range(a, b-1, c):
                    sleep(0.2)
                    print(d, end=' ', flush=True)
            else:
                for d in range(a, b-1, -c):
                    sleep(0.2)
                    print(d, end=' ', flush=True)

        if b >= a and a <= 0 or a >= 0:
            if c == 0:
                c = 1
                sleep(0.2)
                for d in range(a, b-1, c):
                    sleep(0.2)
                    print(d, end=' ', flush=True)
            elif c < 0:
                for d in range(b, a-1, c):
                    sleep(0.2)
                    print(d, end=' ', flush=True)
            else:
                for d in range(a, b+1, c):
                    sleep(0.2)
                    print(d, end=' ', flush=True)


x = 1
y = 10
z = 1
counter(x, y, z)
print()
line()
print("Now it's your turn")
x = int(input('Start: '))
y = int(input('End: '))
z = int(input('Step: '))
counter(x, y, z)

input('Enter to exit')
