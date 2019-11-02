class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dx, dy=[0,1,0,-1],[1,0,-1,0]
        x=y=di=res=0
        
        obstacleSet=set(map(tuple, obstacles))
        
        for cmd in commands:
            if cmd==-2:
                di=(di+4-1)%4
            elif cmd==-1:
                di=(di+1)%4
            else:
                for k in range(cmd):
                    if ((x+dx[di]),(y+dy[di])) not in obstacleSet:
                        x+=dx[di]
                        y+=dy[di]
                        
                    res=max(res, x*x+y*y)     
        return res
                     
                     
                     
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        position_offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        obstacles = set(map(tuple, obstacles))
        x, y, direction, max_distance = 0, 0, 0, 0
        for command in commands:
            if command == -2: direction = (direction - 1) % 4
            elif command == -1: direction = (direction + 1) % 4
            else:
                x_off, y_off = position_offset[direction]
                while command:
                    if (x + x_off, y + y_off) not in obstacles:
                        x += x_off
                        y += y_off
                    command -= 1
                max_distance = max(max_distance, x**2 + y**2)
        print(x, y)
        return max_distance
