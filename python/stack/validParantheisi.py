
def isValid(s) :
     st = []
     mapping = {')' : '(', '}' : '{',']' : '['}
     for ch in s :
         if ch in ['(','{','['] :
             st.append(ch)
         else:
             if not st or st[-1] != mapping[ch]:
                 return False
             st.pop()
     return not st

s = "(}"
print(isValid(s))

