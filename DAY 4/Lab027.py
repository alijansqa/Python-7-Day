# loop

for i in range(0, 20):  # range is a function resulting in -1 output lIKE A LIST
 print(i)

 print("Ali")  # Will print each print below other

 print("Jan")

 for i in range(0, 20):
     print("Ali Jan")

     for i in range(0, 5): # 5-1
         print(i)


         for i in range(1, 10, 2):  # for steps  (start, stop-1, step)
             print(i)

             x = list(range(5))  # returns list in index 
             print(x)