class Solution:
# The idea is that we have in encode <NUM><DELIMITER><actual word> and 
# then knowing the NUM, we can know what is the actual word and 
# once we hit the DELIMITER, we know that right after that the string starts. 

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s 
        return res 


    def decode(self, s: str) -> List[str]:
        result = []  # result will be a list of string 
        i  = 0  # i is the position of where we are in the encoeed string 

        while i < len(s):
            # find the delimiter first 
            j = i 
            while s[j] != "#" : 
                # meaning we are sstill at the character and not hit the delimiter 
                j+=1 
            length = int(s[i:j])
            result.append(s[j+1 : j + 1 + length])
            i = j + 1 + length  # this is the begingin of next string 
        
        return result 





