счет = input()
команда1, команда2 = map(int, счет.split(":"))
if команда1 > команда2:
    print(1)
elif команда2 > команда1:
    print(2)
else:
    print(0)
