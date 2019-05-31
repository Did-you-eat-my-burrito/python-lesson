# name = inpt("名前を入力してください")
#
# print("hello {}".format(name))
#

# answer = 5 // 3

#for i in range(0,51):
    #print(i)



def fizz_buzz(number):



    for i in range(0, number + 1):

        if i % 3 == 0 and i % 5 == 0:
            print("fizz buzz")


        elif i % 3 == 0:
            print("fizz")

        elif i % 5 == 0:
            print("buzz")



        else:
            print(i)



user_input_number = int(input("数字を入れてください"))

fizz_buzz(user_input_number)







#3の倍数がfizz ５の倍数がbuzz
