import sys
from io import StringIO
import random

inp =input().split()
N,T = int(inp[0]),int(inp[1])
population=inp[2:]
chromosome_length = N*T

Chromosome={}
population_dict={}
child=[]

for i in population:
    population_dict[i]=False

#For single Timeslot
def course_selection(population):
    parents = []
    #print(population)
    k=random.randint(1,T)
    for i in range(k):
        rnd=random.choice(population)
        #print(rnd)
        if rnd not in parents:
            parents.append(rnd)
    return parents
# Add all single timeslot to chromosome
def course_schedule(population,chromosome):
    for i in range(T):
        chromosome.append(course_selection(population))
    return chromosome

def make_false():
    for i in population_dict:
        population_dict[i]=False
    return population_dict
# population_dict er value check kre jdi included hoy tahole 1 add kre na hole 0 add kre
def check_population():
    temp=''
    for i in population_dict:
        if population_dict[i]==False:
            temp+="0"
        else:
            temp+="1"
    return temp
# Chromosome make kore from the population
def chromosome_maker():
    temp=[]
    course_schedule(population,temp)
    #print("temp",temp)
    #temp e just sobgula course jegula neoa hoise segula thake
    s=''
    for i in temp:
        for j in i:
            population_dict[j]=True
        s+=check_population()
        make_false()
    return s




    
    
    
def fitness(chromosome):
    overlap_penalty=chromosome.count('1')-1*T
    m=[chromosome[i:i + N] for i in range(0, len(chromosome), N)]
    num_count=[sum(int(row[i]) for row in m) for i in range(len(m[0]))]
    num_count=[abs(x - 1) for x in num_count]
    consistency_penalty=sum(num_count)
    fitness_value=overlap_penalty+consistency_penalty
    return -fitness_value




# Chromosome generator just parent 50 generate kore to take the best 10 for crossing
def chromosome_generator():
    for i in range(50):
        temp=chromosome_maker()
        Chromosome[temp]=fitness(temp)
    return sorted(Chromosome.items(), key=lambda x: x[1], reverse=True)

#Parent selection just best 10 select kore
def parent_selection():
    temp=chromosome_generator()
    return temp[:9]

def crossover(p1,p2):
    crossover_point=random.randint(1,chromosome_length-1)
    child1=p1[0][:crossover_point]+p2[0][crossover_point:]
    child2=p2[0][:crossover_point]+p1[0][crossover_point:]
    child1_fitness=fitness(child1)
    child2_fitness=fitness(child2)
    return crossover_point, (child1,child1_fitness),(child2,child2_fitness)

def child_crossover(parent):
    if len(parent) % 2 != 0:
        parent.append(parent[0])
    child = []
    for i in range(0, len(parent), 2):
        _, child1, child2 = crossover(parent[i], parent[i+1])
        child.append(child1)
        child.append(child2)
    return child

def mutation(child):
    for i in range(len(child)):
        temp = list(child[i][0])
        random.shuffle(temp)
        scrambled_chromosome = ''.join(temp)
        child[i] = (scrambled_chromosome, fitness(scrambled_chromosome))
    return child

def calculate_sum(chr):
    sum=0
    for i in range(len(chr)):
        sum+=int(chr[i])
    return sum

def genetic_algorithm():
    parent=parent_selection()
    flag=True
    c=0
    while flag:
        c+=1
        child=child_crossover(parent)
        mutation(child)
        parent=child
        parent=sorted(parent, key=lambda x: x[1], reverse=True)
        parent=parent[:9]
        child.clear()
        if parent[0][1]==0 and calculate_sum(parent[0][0])>0:
            flag=False
            print(f"""{parent[0][0]}
{parent[0][1]}""")
            break
        if c==999:
            flag=False
            for i in range(9):
                if calculate_sum(parent[i][0])>0:
                    print(f"""{parent[0][0]}
{parent[0][1]}""")
            break

genetic_algorithm()

def two_point_crossover(parent):
    crossover_point1=random.randint(1,chromosome_length-1)
    c1=crossover_point1+1
    crossover_point2=random.randint(c1,chromosome_length-1)
    if crossover_point1>crossover_point2:
        crossover_point1,crossover_point2=crossover_point2,crossover_point1
    child1=parent[0][0][:crossover_point1]+parent[1][0][crossover_point1:crossover_point2]+parent[0][0][crossover_point2:]
    child2=parent[1][0][:crossover_point1]+parent[0][0][crossover_point1:crossover_point2]+parent[1][0][crossover_point2:]
    child1_fitness=fitness(child1)
    child2_fitness=fitness(child2)
    return crossover_point1,crossover_point2, (child1,child1_fitness),(child2,child2_fitness)




print("=========================Two Point Crossover================================")

def only_crossover_test():
    parent=parent_selection()
    for i in range(9):
        print(f"""Parent {i+1}: {parent[i][0]} Fitness: {parent[i][1]}""")
    c=0    
    
    a,b,child1,child2=two_point_crossover(parent)
    print("-------------------------------------------------")
    print("crosspoint1",a)
    print("crosspoint2",b)
    print("-------------------------------------------------")
    print("child1",child1)
    print("child2",child2)
    print("-------------------------------------------------")
        
        
        
        
only_crossover_test()
    