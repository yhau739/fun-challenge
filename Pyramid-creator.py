#Pyramid creator
#Illustration:
#       0
#      000
#     00000
#    0000000
#   000000000
#  00000000000
# 0000000000000

class Pyramid():
    def pyramid_creator(pyramid_width):
        for i in range(0,pyramid_width):
            for l in range(0,pyramid_width-i):
                print(" ",end="")
            for j in range(0,i * 2 + 1):
                print("0",end="")
            print("")

    width = int(input("Enter the width of the pyramid: "))
    pyramid_creator(width)

Pyramid()

