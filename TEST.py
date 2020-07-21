def func():
 global guess
 guess = [input('Write your sentence: ')]
 global word
 word = 'test'

 while word != guess:
   guess = [input('Write your sentence: ')]
   word = 'test'

   if word in guess:

       print('TRUE')
       guess.replace('test','TEST')
       print(guess)
       guess.append('Test 2')
       print(guess)

   else:
       print('FALSE')
   break

   #else:
    # print('FALSE')





