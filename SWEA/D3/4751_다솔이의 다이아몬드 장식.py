T = int(input())

for tc in range(1, T + 1):
    
    string=input()
    length=len(string)
    print('.',end='')
    print('.#..'*length)
    print('.',end='')
    print('#.#.'*length)
    print('#',end='')
    for i in string:
        print('.'+i,end='.#')

    print()    
    print('.',end='')
    print('#.#.'*length)
    print('.',end='')
    print('.#..'*length)