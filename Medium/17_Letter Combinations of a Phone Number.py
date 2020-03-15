class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters=[]
        digit_to_letter = { 2:["a","b","c"], 
                            3:["d","e","f"], 
                            4:["g","h","i"],
                            5:["j","k","l"],
                            6:["m","n","o"],
                            7:["p","q","r","s"],
                            8:["t","u","v"],
                            9:["w","x","y","z"]}
        for digit in digits:
            if int(digit)>1:
                next_letters=[]
                if len(letters)>0:
                    for c_letters in letters:
                        for letter in digit_to_letter[int(digit)]:
                            next_letters+=[c_letters+letter]
                else:
                    for letter in digit_to_letter[int(digit)]:
                        next_letters+=[letter]
                letters=next_letters
            else:
                return []
        return letters