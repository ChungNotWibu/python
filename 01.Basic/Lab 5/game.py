import random


print('\n== FREAKING MATH CONSOLE ==')
print('Give correct answers to get scores.\n')


score = 0  

while True:  
  

  op = random.randint(0, 3)
  left = None     
  right = None    
  result = None   
  op_char = None  

  if op == 0:  
    left = random.randint(0, 50)
    right = random.randint(0, 50)
    result = left + right
    op_char = '+'
  elif op == 1:  
    left = random.randint(0, 50)
    right = random.randint(0, 50)
    result = left - right
    op_char = '-'
  elif op == 2: 
    left = random.randint(0, 10)
    right = random.randint(0, 10)
    result = left * right
    op_char = '*'
  elif op == 3: 
    right = random.randint(0, 10)
    result = random.randint(0, 10)
    left = right * result 
    op_char = '/'


  correct_ans = random.randint(0, 1)  
  if not correct_ans: 
    result += (random.randint(0, 1)*2-1) * random.randint(1, 5)
  

  print(f'{left} {op_char} {right} = {result}')
  print('1 for True, 0 for False: ', end='')
  choice = input()
  if str(correct_ans) == choice:  
    score += 1
    print(f'Score: {score}\n')
  else:                         
    print(f'Incorrect.\n')
    break


print('== GAME OVER ==')
print(f'Your total score is {score}')