import random

player = int(input())  
Min = 1
Max = 0
Branch_factor = 2
Max_Depth = 5
alpha = float("-inf")
beta = float("inf")
scorpion_win=0
sub_zero_win=0

def switchMinOrMax(player):
    if player == 0:
        return 1
    else:
        return 0

def build_Tree(player, depth=0):
    if depth == Max_Depth:
        return random.choice([1, -1])
    
    if player == Max:
        return build_Max_Tree(depth)
    else:
        return build_Min_Tree(depth)

def build_Max_Tree(depth):
    root = Max_Node()
    for i in range(Branch_factor):
        child = build_Tree(Min, depth + 1)
        root.add_child(child)
    return root

def build_Min_Tree(depth):
    root = Min_Node()
    for i in range(Branch_factor):
        child = build_Tree(Max, depth + 1)
        root.add_child(child)
    return root

class Max_Node:
    def __init__(self):
        self.children = []
        self.value = 0
    
    def add_child(self, child):
        self.children.append(child)
    
class Min_Node:
    def __init__(self):
        self.children = []
        self.value = 0
    
    def add_child(self, child):
        self.children.append(child)

def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    if isinstance(node, int):
        return node

    if maximizing_player:
        return Scorpion_play(node, depth, alpha, beta)
    else:
        return Sub_zero_play(node, depth, alpha, beta)

def Scorpion_play(node, depth, alpha, beta):
    max_eval = float('-inf')
    for child in node.children:
        eval = alpha_beta_pruning(child, depth + 1, alpha, beta, False)
        max_eval = max(max_eval, eval)
        if beta <= alpha:
            break  
        
    if max_eval != float('-inf'):
        return max_eval
    else:
        return 0  

def Sub_zero_play(node, depth, alpha, beta):
    min_eval = float('inf')
    for child in node.children:
        eval = alpha_beta_pruning(child, depth + 1, alpha, beta, True)
        min_eval = min(min_eval, eval)
        if beta <= alpha:
            break
    if min_eval != float('inf'):
        return min_eval
    else:
        return 0 

def play_game(starting_player):
    if starting_player == 0:
        root = build_Tree(Max, 0)
    else:
        root = build_Tree(Min, 0)
    if starting_player == 0:
        optimal_value = alpha_beta_pruning(root, 0, float('-inf'), float('inf'), True)
    else:
        optimal_value = alpha_beta_pruning(root, 0, float('-inf'), float('inf'), False)
    return optimal_value
# Output making
p=True
c=[]
while p:
    
    
    if player == 0:
        
        result = play_game(player)
        if result == 1:
            scorpion_win += 1
            c.append("Scorpion")
            
        else:
            sub_zero_win += 1
            c.append("Sub-Zero")
        player = switchMinOrMax(player)
        
    else:
        
        result = play_game(player)
        if result == 1:
            scorpion_win += 1
            c.append("Scorpion")
        else:
            sub_zero_win += 1
            c.append("Sub-Zero")
        player = switchMinOrMax(player)
        
    if scorpion_win == 3:
        print("Game Winner: Scorpion")
        print(f"Total Rounds: {len(c)}")
        for i in range(len(c)):
            print(f"Winner of Round {i+1}: {c[i]}")

        
        
        p=False
    elif sub_zero_win == 3:
        print("Game Winner: Sub-Zero")
        print(f"Total Rounds: {len(c)}")
        for i in range(len(c)):
            print(f"Winner of Round {i+1}: {c[i]}")
        p=False
        
        
print("================================================================================================================Part 2============================================================================")
Max_Depth_little = 2

def build_Tree_little(player, depth=0, leaf_nodes=[]):
    if depth == Max_Depth_little:
        return leaf_nodes.pop(0)
    
    if player == Max:
        return build_Max_Tree_little(depth,leaf_nodes)
    else:
        return build_Min_Tree_little(depth,leaf_nodes)



def build_Max_Tree_little(depth,leaf_nodes):
    root = Max_Node()
    for i in range(Branch_factor):
        child = build_Tree_little(Min, depth + 1,leaf_nodes)
        root.add_child(child)
    return root

def build_Min_Tree_little(depth,leaf_nodes):
    root = Min_Node()
    for i in range(Branch_factor):
        child = build_Tree_little(Max, depth + 1,leaf_nodes)
        root.add_child(child)
    return root


def play_game_2(leaf,leaf_nodes2,c):

    root = build_Tree_little(Max, 0,leaf)
    optimal_value = alpha_beta_pruning(root, 0, float('-inf'), float('inf'), True)
    
    
    dark_magic=[i-c for i in leaf_nodes2]
    
    dark_magic_l=[i-c for i in leaf_nodes2[:4]]
    
    dark_magic_r=[i-c for i in leaf_nodes2[4:]]
    
    p=[]
    p.append((optimal_value, "root"))
    p.append((max(dark_magic),"dark magic"))
    p.append((max(dark_magic_l),"left"))
    p.append((max(dark_magic_r),"right"))
    
    mx=max(p)
    
    if mx[0]==optimal_value:
        print(f"The minimax value is {optimal_value}. Pacman does not use dark magic.")
        a=best_dark_magic(dark_magic_l,dark_magic_r)
        if a!=None:
            print(f"But if uses dark magic then the Advantageous direction will {a}.")
        else:
            print("There is no advantageous direction simply use both direction.")
        
        
    elif mx[1]=="dark magic":
        print(f"The new minimax value is {mx[0]}. Pacman uses dark magic both directions.")
        
      
    else:
        print(f"The new minimax value is {mx[0]}. Pacman goes {mx[1]} and uses dark magic.")
        
    
        
    
    
def best_dark_magic(a,b):
    if max(a)>max(b):
        return "left"
    elif max(a)<max(b):
        return "right"
    return None
     
    
lf_1 = [3,6,2,3,7,1,2,0]

leaf_nodes2= lf_1.copy()
c=int(input())
play_game_2(lf_1,leaf_nodes2,c)