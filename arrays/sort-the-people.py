class Solution:
    def sortPeople(self, names, heights):
        result=[]
        for i in range(len(heights)):
            result.append([heights[i], names[i]])
        result.sort(reverse=True)                  #sort descending order 
       
        r=[]
        for i in range(len(result)):
            r.append(result[i][1])          # 1 represents accessing the name part 

        return r