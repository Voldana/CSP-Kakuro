class Constraint():

    def __init__(self,value,nodes):
        self.is_satisfied = False
        self.value = value
        self.nodes=nodes

    def getSum(self):
        sum=0;
        for node in self.nodes:
            sum+=node.value

        return sum
    def check_satisfaction(self,nodes,value):
        sum=0
        for node in nodes :
            sum+=node.value
        if sum== value:
            return True
        else :
            return False