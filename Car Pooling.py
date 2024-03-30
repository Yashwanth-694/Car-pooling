def carpooling(trips,capacity):
    stop_lst=[]
    for item in trips:
        stop_lst.append(item[1])
        stop_lst.append(item[2])
    max_stop_no=max(stop_lst)+1
    pass_cnt=[0]*max_stop_no
    for item in trips:
        pass_cnt[item[1]]=item[0]
        pass_cnt[item[2]]=-item[0]
    tot=0
    for p_cnt in pass_cnt:
        tot+=p_cnt
        if tot>capacity:
            return False
    return True
trips=[[2,1,5],[3,5,7]]
capacity=5
ans=carpooling(trips,capacity)
print(ans)
        
        
