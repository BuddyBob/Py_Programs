def removeDuplicates(head):
   itr = head
   arr = []
   while itr is not None :
      arr.append(itr.data)
      itr = itr.next
   arr2 = list(set(arr))
   print(arr2)
   
   temp = head 
   while(temp.next is not None):
       for i in arr2:
           temp.data = i
           temp=temp.next
      
   
   return head
removeDuplicates(4)