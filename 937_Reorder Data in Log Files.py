class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        logs_=[i.split(' ',1) for i in logs]
        log_num=[i for i in logs_ if not i[1][0].isalpha()]
        log_alpha=[(i[1],i[0]) for i in logs_ if i[1][0].isalpha()]
        log_alpha.sort()
        log_alpha=[(i[1],i[0]) for i in log_alpha]

        
        logs=log_alpha+log_num
        return [' '.join(i) for i in logs]
        
        
        
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letters=[]
        nums=[]
        for i in logs:
            log_split=i.split(' ',1)
            if log_split[1][0].isalpha():
                letters.append((log_split[1], log_split[0]))
            else:
                nums.append(i)
        letters.sort()
        
        return [i[1]+' '+i[0] for i in letters]+nums
            
            
            
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letters=[]
        nums=[]
        for log in logs:
            idx=log.find(' ')
            if log[idx+1].isalpha():
                letters.append((log[idx+1:], log[:idx]))
            else:
                nums.append(log)
        letters.sort()
        
        return [i[1]+' '+i[0] for i in letters]+nums
        
        
        
        
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def f(log):
            id_,rest=log.split(' ',1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)
        
        return sorted(logs, key=lambda x: f(x))
            
        
        
        
    
