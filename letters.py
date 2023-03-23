# do not do this
# letters = ''
# for c in document:
#     if c .isalpha() :
#         letters += c
        
        
# temp = []
# for c in letters:
#     if c.isalpha():
#         temp.append(c)
#     letters = ''.join(temp)

    
letters = ''.join([c for c in document if c.isalpha()])
letters = ''.join(c for c in document if c.isalpha())