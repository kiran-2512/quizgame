print('Hello, welcome to quiz')

ans = input('Are u ready to play (yes/no): ')
score = 0
total_questions= 5
#Here i'm declaring a three variables which is ans,score,and total_questions,if answer is yes it will continue or else it will terminate

if ans.lower() == "yes":
    #lower fuctionality : if user enters any uppercase letters it will replace the upper case to lower case
    ans=input(' 1. Which operator is used to multiply numbers? ')
    if ans == "*":
        score+=1
        print('Correct')
    else:
        print('Incorrect')


    ans=input(' 2. what is 20 % 10 ? ')
    if ans  == "0":
        score+=1
        print('Correct')
    else:
        print('Incorrect')


    ans=input(' 3.Which operator is used to show that two number are equal ? ')
    if ans  == "==":
        score+=1
        print('Correct')
    else:
        print('Incorrect')

    ans=input('4.Which statement is used to stop a loop? ')
    if ans.lower() == "break":
        score+=1
        print('Correct')
    else:
        print('Incorrect')

    ans=input('5. Which method can be used to return a string in upper case letters? ')
    if ans.lower() == "upper()":
        score+=1
        print('Correct')
    else:
        print('Incorrect')

print('Thank you for participating, you got ',score,"Question correct.")
mark = (score/total_questions) * 100
#displaying the marks in percentage.
print("mark: ",mark)

