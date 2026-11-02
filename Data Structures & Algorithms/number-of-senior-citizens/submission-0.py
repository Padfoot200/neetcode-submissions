class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for x in details:
            print(x[11:13])
            if int(x[11:13])>60:
                print(x[11:13])
                count+=1
        return count