class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        c = 0
        for i in items:
            for j in range(0, len(i)):
                print(i[j])
                if ruleKey == 'name':
                    if ruleValue == i[2]:
                        c+=1
                        break
                elif ruleKey == 'color':
                    if ruleValue == i[1]:
                        c+=1
                        break
                elif ruleKey == 'type':
                    if ruleValue == i[0]:
                        c+=1
                        break
                else: 
                    continue 
        return c 