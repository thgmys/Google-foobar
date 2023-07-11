def solution(x, y):
    # start with 1,1
    # for every bomb left iteration return(m+f, f)
    # for every bomb right iteration return(m, f+m)
    mach_bomb = int(x)
    facula_bomb = int(y)
    count = 0
    while mach_bomb != facula_bomb:
        if mach_bomb > facula_bomb:
            cycles = (mach_bomb - facula_bomb) // facula_bomb + (
                (mach_bomb - facula_bomb) % facula_bomb > 0
            )
            count += cycles
            mach_bomb, facula_bomb = mach_bomb - cycles * facula_bomb, facula_bomb
        elif facula_bomb > mach_bomb:
            cycles = (facula_bomb - mach_bomb) // mach_bomb + (
                (facula_bomb - mach_bomb) % mach_bomb > 0
            )
            count += cycles
            mach_bomb, facula_bomb = mach_bomb, facula_bomb - cycles * mach_bomb
    return str(count) if (mach_bomb, facula_bomb) == (1, 1) else "impossible"


print(solution("4", "7"))
print(solution("2", "4"))
