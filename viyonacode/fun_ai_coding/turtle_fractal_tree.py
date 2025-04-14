import turtle


def draw_tree(t, branch_len, angle, shorten_factor, min_branch_len):
    if branch_len > min_branch_len:
        t.forward(branch_len)
        new_len = branch_len * shorten_factor

        t.left(angle)
        draw_tree(t, new_len, angle, shorten_factor, min_branch_len)

        t.right(2 * angle)
        draw_tree(t, new_len, angle, shorten_factor, min_branch_len)

        t.left(angle)
        t.backward(branch_len)


# Setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("skyblue")
screen.tracer(0, 0)  # Use this instead of False
print("came here")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.left(90)
t.penup()
t.goto(0, -250)
t.pendown()

draw_tree(t, 100, 25, 0.7, 15)
screen.update()
turtle.done()
