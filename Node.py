from Constraint import Constraint
class Node():


    def __init__(self,i,j,value,table):
        self.degree=0
        self.i=i
        self.j=j
        self.value=value
        #self.const=self.setConstraint(i,j,table)
        #self.nodes.append(self)
        self.domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.alternative_domain=[]
        self.alter2=[]
        self.constrain = []
    def setConstraint(self,i,j,table):
        n=[]
        for k in range(self.col):
            n.append(table[i][k])
        row_constraint=Constraint(table[i][0],n)
        return
    
