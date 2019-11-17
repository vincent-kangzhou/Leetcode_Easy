class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        import collections
        dic=collections.defaultdict(int)
        
        for word in cpdomains:
            split=word.split()
            count=int(split[0])
            domain=split[1].split('.')
            for j in range(len(domain)):
                subdomain='.'.join(domain[j:])
                dic[subdomain]+=count
                
        return [str(dic[idx])+' '+idx for idx in dic]
        
        
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        import collections
        dic=collections.defaultdict(int)
        
        for word in cpdomains:
            count, domain=word.split()
            count=int(count)
            dic[domain]+=count
            while '.' in domain:
                domain=domain[domain.index('.')+1:]
                dic[domain]+=count
                
        return [str(val)+' '+idx for idx, val in dic.iteritems()]
