def solution(pegs):
    if ((not pegs) or (len(pegs)<2) or (len(pegs)>20) or (not isinstance(pegs,list))):
        return [-1,-1]
    radius=0
    # sequence is d1-d2+d3-d4+...+ s*dn
    # s = (n-1) % 2
    for idx,val in enumerate(pegs):
        if val < 1 or val > 10000:
            return[-1,-1]
        if idx+1 < len(pegs):
            if pegs[idx+1]<val:
                return [-1,-1]
            distance = pegs[idx+1] - val # dn+1 - dn
            if idx%2==1: # flip sign
                distance=distance*-1
            # print(distance, ': distance |||', idx, ": index")
            radius += distance
    if radius < 1 or radius/3<1 or radius%1!=0:
        return [-1,-1]
    radius=radius*2
    # print(radius)

    #case if odd number of pegs
    if len(pegs)%2==1:
        ans = [int(radius), 1]
    
    #case if even number of pegs
    else:
        if radius%3==0:
            ans=[int(radius/3),1]
        else:
            ans=[int(radius),3]
            
    #all gears have to be larger than radius==1
    gear = ans[0]/ans[1]
    for i in range(len(pegs)-1):
        # print(pegs[i])
        gear = pegs[i+1] - pegs[i] - gear
        if gear < 1:
            return [-1,-1]
    return ans


solution([4,30,50])
# solution([4,17,50])
# # solution([4,30,50,64,75,84])
# print(solution([]))
# print(solution([-1,10]))
