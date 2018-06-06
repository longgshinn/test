# for i in range(2,8,2):
# #     print(i)
# print(*range(2,8,3))
from turtle import *
shape("turtle")
speed(0)
x=10
fillcolor('red')
pencolor('black')
pensize(5)
begin_fill()
for i in range(50):
    for i in range(4):
        forward(x)
        left(90)
    right(30)
    x=x+10
end_fill()
mainloop()