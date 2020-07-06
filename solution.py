# Write a program determine whether the given number is Armstrong number or not.
# The program should return true or false

def checkArmstrong(num):
        sumi = 0
        temp = num
        while temp > 0:
                digit = temp % 10
                sumi += digit ** 3
                temp //= 10
        if num == sumi:
                return True
        else:

                return False
