import turtle as t
n=50
t.speed(0)
t.bgcolor("black")
t.color('green')
for a in range(n):
    t.circle(80)
    t.lt(360/n)

angle=100
t.speed(0)
t.bgcolor("black")
t.color('yellow')
for x in range(200):
    t.fd(x)
    t.lt(angle)
