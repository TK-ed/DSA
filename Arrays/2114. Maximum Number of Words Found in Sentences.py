class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        c = 0
        l = []
        for i in sentences:
            c = 0
            for j in range(0, len(i)):
                print(i, i[j])
                if i[j] == " ":
                    c+=1
            c+=1
            l.append(c)
        l.sort()
        return l[-1]