def PascalTriangle(n):
   row = [1]
   y = [0]
   for x in range(n):
      print(row)

      print(' ')

      row=[left+right for left,right in zip(row+y, y+row)]

   return n

rows = 27
PascalTriangle(rows)