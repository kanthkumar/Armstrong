# Write a program determine whether the given number is Armstrong number or not.
# The program should return true or false

def checkArmstrong(num):
        sumit = 0
        temp = num
        while temp > 0:
                digit = temp % 10
                sumit += digit ** len(str(num))
                temp //= 10
#IrfaShaik Writing this
        return num == sumit
