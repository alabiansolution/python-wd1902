num = int(input("Enter num: "))


if num >= 0 and num <= 34:      #if score is >= 0 and score < 35:
   print ("Your score is:",  num,  "Result Fail (F)")

   
elif num >= 35 and num <= 44:
   print ("Your score is:",  num,  "Result: Pass(E)")

elif num  >= 45 and num <= 49:
       print ("Your score is:", num,  "Result: Fair(D)")

elif num  >= 50 and num <= 59:
           print ("Your score is:",  num,  "Result: Good(C)")

elif num  >= 60 and num <= 69:
           print ("Your score is:" , num,  "Result: Very Good(B)")

elif num  >= 70 and num <= 100:
               print ("Your score is:",  num,  "Result: Excellence(A)")
               
else:
        print ("Result not found...Report to Exams & Records. Thank you")

   
    