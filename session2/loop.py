# # for i in [2, 45, 2, 62, 3]:
# #  print(i)
# from turtle import *
# shape('turtle')
# # for i in ["yellow", "black", "pink", "blue"]:
# #     color(i)
# #     forward(150)
# #     left (90)
# # mainloop()

# # n = int(input( "How many sides does the polygon have?" ))
# # for side in range (n):
# #     forward (150) 
# #     left (90)
# # mainloop()
# # n = int(input())
# # for i in range (3, n+1):
# #     for j in range (i):
# #         forward (150)
# #         left (360/i)
# # mainloop()

# total = 0
# for i in ['a','b','c']:
#     total +=i
# print(total)
account_username = "mindx"
account_password = "mindx123"

running = True
while running:
    username = input('username: ')
    password = input('password: ')

    if username == account_username and password == account_password:
            print('Dung quay lai voi nyc')
            running = False
    else:
        print('sai acc roi T.T')