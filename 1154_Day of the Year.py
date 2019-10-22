class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        import datetime
        
        day_month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
        date_time=datetime.datetime.strptime(date,'%Y-%m-%d')
        
        year=date_time.year
        if (year%4==0 and year%100!=0) or year%400==0:
            day_month[2]=29
        return sum(day_month[:date_time.month])+date_time.day
        
        
class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        date_time=date.split('-')
        day_month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
        if (int(date_time[0])%4==0 and int(date_time[0])%100!=0) or int(date_time[0])%400==0:
            day_month[2]=29
        return sum(day_month[:int(date_time[1])])+int(date_time[2])
