class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return (moves.count('U')==moves.count('D')) and (moves.count('L')==moves.count('R'))
        
        
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        dirs={'U':1,'D':-1, 'L':-1j,'R':1j}
        
        return sum(dirs[i] for i in moves)==0
        
        
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        import collections
        count=collections.Counter(moves)
        
        return count['U']==count['D'] and count['L']==count['R']
