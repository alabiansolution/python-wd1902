score = int(input("Enter score: "))

if score >= 0 and score < 35:
    print("Your score is ",score, "and this is Fail")
elif score >= 35 and score < 45:
    print("Your score is ", score, "and this is Pass")
elif score >= 45 and score < 50:
    print("Your score is ", score, "and this is Fair")
elif score >= 50 and score < 60:
    print("Your score is ", score, "and this is Good")
elif score >= 60 and score < 70:
    print("Your score is ", score, "and this is vary Good")
elif score >= 70 and score <= 100:
    print("Your score is ", score, "and this Excellent")
else:
    print("Invalid score")
