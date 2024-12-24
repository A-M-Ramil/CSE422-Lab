#==========================================imports=====================================
from collections import defaultdict
import heapq as heap
from itertools import chain


#==========================================Input Handling & Global var declaration =====================================
f=open("Input file.txt")
f=f.readlines()
l=[[str(i) for i in f[_].split()] for _ in range(len(f))]
print(l)
d_branch=defaultdict(list)
d_hval=defaultdict(int)
p_que=[]
parent={}
end_node=""
for i in l:
    d_hval[i[0]]=int(i[1])
    if int(i[1])==0:
            end_node=i[0]
    for j in range(2,len(i[2:])+1,2):
        d_branch[i[0]].append([int(i[j+1]),i[j]])
print("===========================================")
print(d_hval)
print("===========================================")
print(d_branch)

#==========================================Finding the start and end node=============================================
def find_start_end():
    return l[0][0], end_node






#==========================================Path Finding=============================================
def find_path(current):
    path_l=[]
    k=current
    while k!=None:

        path_l.append(k)
        k=parent[k]

    c=-1
    jk=0
    s=path_l[-1]
    for i in path_l:
        for j in d_branch[i]:
            if j[1]==path_l[c+1]:

                jk+=j[0]
                c+=1
    path_real=path_l[::-1]
    for i in path_real[1:]:
        s+=" --> "+i
    print(f"""Path: {s}
Total distance: {jk} km""")




#==========================================Finding the smallest leaf=============================================
def find_small_leaf(node,cost):
    temp_d={}
    for i in d_branch[node]:
        if {i[1]}.issubset(chain.from_iterable(p_que)):

            for j in p_que:

                if j[1]==i[1] and j[0]>(cost+i[0]+d_hval[i[1]]) :
                    p_que[0]=cost+i[0]+d_hval[i[1]]
                    if parent[node]!=j[1]:
                        parent[j[1]]=node

        else:
            heap.heappush(p_que,[cost+i[0]+d_hval[i[1]],i[1]])
            if parent[node]!=i[1]:
                parent[i[1]]=node
            temp_d[i[1]]=i[0]


    chosen=heap.heappop(p_que)
    print(chosen,temp_d)
    return chosen, temp_d[chosen[1]]


#================================================A* Search Algorithm=============================================
def A_search():

    start, end = find_start_end()
    print(f"""Start Node: {start}
Destination: {end}""")
    parent[start]=None
    s=0
    found=False
    current=start
    while not found:

        if current == end:
            found=True
            return find_path(current)
            break

        current_s,s=find_small_leaf(current,s)

        current=current_s[1]



    return "NO PATH FOUND"

#==========================================Main Function=============================================
A_search()