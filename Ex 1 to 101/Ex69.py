# ----- Header -----
def header():
    print('=' * 15)
    print('Register a person')
    print('=' * 15)

# ----- Var -----
c = ywomen = old = man = 0
while True:
    sex = ''
    r = ''
    header()
# ---- Input -----
    age = int(input('age: '))
    while sex not in 'MF':
        sex = str(input('Sex: [M/F]: ')).upper().strip()
# ----- Conditional -----
    if sex == 'M':
        man = man + 1
    if age > 18:
        old = old + 1
    if sex == 'F' and age < 19:
        ywomen = ywomen + 1
    print('=' * 15)
# ----- Option to tell if the loop will happen again -----
    while r not in 'YN':
        r = str(input('Do you want to continue?: [Y/N]')).upper().strip()
    if r == 'N':
        break
# ----- Output -----
print(f'Total of people over 18 years: {old}')
print(f'Total we have {man} man registered')
print(f'We have {ywomen} women under 19 years')

input('Enter to exit')
