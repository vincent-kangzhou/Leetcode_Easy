class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        dic={employee.id: (employee.importance, employee.subordinates) for employee in employees}
        
        res=dic[id][0]
        
        subordinate=dic[id][1]
        
        while subordinate:
            id=subordinate.pop(0)
            res+=dic[id][0]
            subordinate+=dic[id][1]
        return res
        
        
        
        
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        dic={employee.id: (employee.importance, employee.subordinates) for employee in employees}
        
        def dfs(id):
            return dic[id][0]+sum(dfs(i) for i in dic[id][1])
        return dfs(id)
        
        
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        dic={employee.id: (employee.importance, employee.subordinates) for employee in employees}
        res=dic[id][0]
        
        for i in dic[id][1]:
            res+=self.getImportance(employees, id)
        return res
        
