l = [1, 2, 3, 4, 5]

for item in l:
    if item > 3:
        break
    print(item)

while True:
    print('Welcome')
    answer = input('Want to continue (yes/no)? ')
    if answer == 'no':
        print('goodbye')
        break
