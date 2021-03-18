turn = 1
opts = [["empty"]*4]*4
while True: 
  print('               Board')
  for i in opts:print(i)
  slot = int(input('Enter a column [1-4]: '))
  count = 0
  while count <= 4:
    if opts[count][slot] == "empty":
      if turn == 1:
        opts[count][slot] = "blue"
        print(opts[count][slot])
        break
      else:
        opts[count][slot] = "red"
        break

  turn *= -1































# x = [ ['empty', 'empty', 'empty', 'red'],
#  ['empty', 'empty', 'red', 'red'],
#  ['empty', 'red', 'red', 'empty'],
#  ['red', 'red', 'empty', 'empty'],
# ]

# l = []
# l2 = []
# num = 1
# for lists in x:
#   if lists[-num] == 'red':
#     l.append(True)
#   else:
#     l.append(False)
#   num+=1
# print(l)

# num = 0
# for lists in x:
#   if lists[num] == 'red':
#     l2.append(True)
#   else:
#     l2.append(False)
#   num+=1
# print(l2)