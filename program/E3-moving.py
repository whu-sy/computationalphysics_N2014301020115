import os
import time

l1 = " ### #  # #### #   #   #   #   #   #   #   ###"
l2 = "#    #  # #    ##  #    # #   # #  ##  # #    "
l3 = " #   #### #### # # #     #   ##### # # # #  ##"
l4 = "  #  #  # #    #  ##     #   #   # #  ## #   #"
l5 = "###  #  # #### #   #     #   #   # #   #  ### "

start = input()
os.system('cls')

for i in range(10):
    l1 = " " + l1
    l2 = " " + l2
    l3 = " " + l3
    l4 = " " + l4
    l5 = " " + l5
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    time.sleep(0.2)
    os.system('cls')

end = input()