mystory = "He doesn't like to eat \"cheese\""
''' \ is used to escape the quotation formula
     in this way " is not to be considered as 
      part of it.
      For this comment we use \' instead of \"
      as otherwise it would confuse the first part (mystory)'''

print(mystory)


#Same thing here, but different way
print('\n')
mystory = 'He doesn\'t like to eat "cheese"'
print(mystory)


# Here we create a multistring by using \n
print('\n')
mystory = 'He doesn\'t like to eat "cheese"\nBut he does like eggs'
print(mystory)

# Here we use double \ to escape \ escape
print('\n')
filepath = "martina\pythonforprogrammers\\news"
print(filepath)
