class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        split=[i.split('@') for i in emails]
        domain=[i[1] for i in split]
        
        local=[i[0].split('+')[0].replace('.','') for i in split]
        
        address=[local[i]+'@'+domain[i] for i in range(len(domain))]
        
        return len(set(address))
        
        
        
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        eset=set()
        for email  in emails:
            simper=self.simplifyemail(email)
            eset.add(simper)
        return len(eset)
    
    
    def simplifyemail(self, email):
        local, domain=email.split('@')
        plus_i=local.find('+')
        if plus_i!=-1:
            local=local[:plus_i]
        local=local.replace('.','')
        return local+'@'+domain
        
        
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res=set()
        for email in emails:
            local, domain=email.split('@')
            local=local.split('+')[0].replace('.','')
            res.add(local+'@'+domain)
            
        return len(res)
