from collections import defaultdict
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        dct = defaultdict(int)
        uqemail = 0
        for email in emails:
            local, domain = email.split('@')
            try:
                local = local[:local.index('+')]
            except ValueError:
                pass
            local = list(filter(('.').__ne__, local))
            key = str(local)+'@'+str(domain)
            if dct[key] == 0:
                uqemail += 1
                dct[key] += 1
        return uqemail