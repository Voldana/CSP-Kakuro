from Node import Node
from Constraint import Constraint
const_nodes_count=0
parent_node=0
def MRV(nodes,fixedNodes):
    node=None
    min=9

    for row in nodes :
        for n in row:
            if n!=0 and n.__hash__() not in fixedNodes:
                if len(n.domain)<min:
                    min=len(n.domain)
                    node=n
    return node
def get_maxnode(nodes,fixedNodes):   #Returns node with max degree
    node=None
    max=0
    for row in nodes :
        for n in row:
            if n!=0 and n.__hash__() not in fixedNodes:
                if n.degree>max:
                    max=n.degree
                    node=n
    return node
def is_finished(const_list,fixedNodes):
    sw=False
    if len(fixedNodes)!=const_nodes_count :return False
    for constrain in const_list:
        if constrain.check_satisfaction(constrain.nodes,constrain.value)==False :
            return False
    return True

    
def isValid(cons_list):
    valid=False
    for cons in cons_list:
        sw=0
        cns=cons.getSum()
        for n in cons.nodes:
           if n.value==0:
               sw=1
               break
        if cons.value<cns:
            return False
        elif  cons.value>cns and sw==0 :
            return  False
        else :
            valid= True
    return valid



    return True

def nodeConsistency(constrain_list):
        for constrain in constrain_list:
            if constrain.value < 10:
                for n in constrain.nodes:
                    n.domain=n.domain[:constrain.value]




def forward_checking(consList,fixedNodes,xval):

    for constrain in consList:
        for node in constrain.nodes:
            if node.__hash__() not in fixedNodes:
                val=constrain.value-xval
                if val <10:
                    node.alternative_domain=node.domain[val:]
                    node.domain=node.domain[0:val]
                    if len(node.domain)==0 : return False
    return True


def remove_value_xy(x,y,c):
    removed=False
    cons_both=c
    check=0

    if x.value!=0 or y.value!=0  :
        return removed
    has_empty=0
    for n in cons_both.nodes:
        if len(cons_both.nodes)==2:
            has_empty=0
            break
        if n.value == 0:
            has_empty = 1
            break
    removable=[]
    for v in y.domain :
        check=0
        for u in x.domain : 
            if (cons_both.value)>u+v and has_empty==1:#satisfy
                check=1
                break
            if (cons_both.value) == u + v and has_empty==0:  # satisfy and has_empty== 0
                check = 1
                break
        if check==0 :
            removable.append(v)
            removed=True
            y.alter2.insert(v,v)
    for r in removable:
        y.domain.remove(r)


    return removed


def arc_consistency(nodes_list,fixedNodes,nodeparent):
    conflict = False
    queue=[]
    queue=q_filler(nodeparent.constrain,fixedNodes)
    while len(queue)!=0 and not conflict:
        x=queue.pop()
        for c in x.constrain :
            for n in c.nodes :
                if n.__hash__() not in fixedNodes and x!=n : 
                    if remove_value_xy(x,n,c) : #tartibe algo x,n
                        if len(n.domain)==0 :
                            conflict==True
                            queue.append(n)




    return not conflict,queue


def backtracking(constrain_list,nodes,fixedNodes:list,nodeparent,count):
    if is_finished(constrain_list,fixedNodes): return constrain_list
    if len(fixedNodes)==const_nodes_count: return False
    var_domains,q=arc_consistency(nodes,fixedNodes,nodeparent)
    if var_domains==False :
        reverse_ac3(q)
        return False
    sw=0

    x = MRV(nodes, fixedNodes)
    if x==None :
        x=get_maxnode(nodes,fixedNodes)
    #Exception
    if x==None:
        for r in nodes:
            for n in r :
                if n!=0 and n.__hash__() not in fixedNodes:
                    x=n
                    sw=1
                    break
            if sw==1 : break

    ## ordering
    x.domain.reverse()
    d=x.domain


    for v in d:

        x.value=v
        fixedNodes.append(x.__hash__())
        if nodes[1][1]==2 and nodes[1][2]==4 :
            print("...Horay...")
        res_fc=forward_checking(x.constrain,fixedNodes,x.value)
        if res_fc==False :
            reverse_ac3(q)
            return False
        if isValid(x.constrain):
            result=backtracking(constrain_list,nodes,fixedNodes,x,count+1)
            if result!=False :
                reverse_ac3(q)
                return result
        reverse_fc(constrain_list,fixedNodes)
        fixedNodes.remove(x.__hash__())
        x.value=0
    reverse_ac3(q)
    return False



def printResult(nodes,table):
    i=0
    j=0
    for r in nodes :
        j=0
        for n in r :
            if n!=0:
                table[n.i][n.j]=n.value
            j+=1
        i+=1


    for q in table:
        print(q)

def printTable(constraint):
    if  type(constraint)==bool :
        return print("no soloution")

    for cons in constraint:
        nl=[]
        for n in cons.nodes:
            nl.append(n.value)
        print(str(cons.value) +" = " + str(nl))

def nodesCount(nodes):
    count=0
    for r in nodes:
        for n in r:
            if n!=0 :
                count+=1
    return count





def reverse_ac3(q):
    for n in q :
        for v in q.alter2:
            n.domain.insert(v,v)


def q_filler(constraintlist,fixedNodes):
    q=[]

    for cns in constraintlist :
        for n in cns.nodes:
            if n!=0 and n.__hash__() not in fixedNodes:
                if n not in q:
                    q.append(n)
    return q           


def getDomains(nodes):
    domains=[]
    for r in nodes :
        for f in r:
            if f!=0:
                domains.append(f.domain)
    return domains

def reverse_fc(consList,fixedNodes):
    for constrain in consList:
        for node in constrain.nodes:
            if len(node.alternative_domain)!=0 and node.__hash__() not in fixedNodes:
                node.domain=node.domain+node.alternative_domain
                node.alternative_domain=[] 






if __name__ == '__main__':
    row=int(input())
    col=int(input())
    constrain_list=[]
    nodes=[[0 for o in range(col)] for p in range(row)]
    table=[[0 for o in range(col)] for p in range(row)]
    for i in range(row ):
        temp=input()
        for j in range(col) :
            table[i][j]=int(temp.split()[j])
            if table[i][j]==0: #var
                nodes[i][j]=(Node(i,j,0,table))

    for i in range(row):

        for j in range(col):

                    if table[i][j] != -1 and table[i][j] != 0:
                        n = []
                        try:
                            if table[i][j + 1] == 0 :
                                for k in range(j, col):
                                    if nodes[i][k]!=0:
                                        n.append(nodes[i][k])
                                        nodes[i][k].degree+=1
                            else:
                                for k in range(i, row):
                                    if nodes[k][j]!=0:
                                        n.append(nodes[k][j])
                                        nodes[k][j].degree+=1
                            constrain_list.append(Constraint(table[i][j],n ))
                            for eachnode in n:
                                eachnode.constrain.append(Constraint(table[i][j],n ))
                        except :
                            for k in range(i, row):
                                if nodes[k][j]!=0:#VASE arre nodes
                                    n.append(nodes[k][j])
                                    nodes[k][j].degree+=1
                            constrain_list.append(Constraint(table[i][j], n))
                            for eachnode in n:
                                eachnode.constrain.append(Constraint(table[i][j],n ))


    nodeConsistency(constrain_list)
    const_nodes_count=nodesCount(nodes)
    result_cons=(backtracking(constrain_list,nodes,[],nodes[2][2],0))
    printResult(nodes,table)   