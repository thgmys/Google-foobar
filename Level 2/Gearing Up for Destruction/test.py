
pegs = [4,30,50]

#all gears have to be larger than radius==1
gear = pegs[0]/pegs[1]
for i,val in enumerate(pegs[:len(pegs)-1]):
    print(i, val)
    print(pegs[i+1], 'pegs')
    gear = pegs[i+1] - val - gear
    print(gear, 'gear')
    # if gear < 1:
    #     print ([-1,-1])
print('\n')
    # if idx+1!=len(pegs)-1:
    #     gear = pegs[idx+1] - val - gear
    #     print(gear)
    # if gear < 1:
    #     print([-1,-1])

for i in range(len(pegs)-1):
    print(i, pegs[i])
    print(pegs[i+1], 'pegs')
    gear = pegs[i+1] - pegs[i] - gear
    print(gear, 'gear')
    # if gear < 1:
    #     print([-1,-1])