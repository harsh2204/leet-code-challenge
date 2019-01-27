class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        uniques = set([])
        for email in emails:
            plus = email.find("+")
            dash = email.find("@")
            email = email[:plus].replace(".","")+email[dash:]
            if email not in uniques:
                uniques.add(email)
        return len(uniques)
