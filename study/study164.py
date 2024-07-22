import turtle

def draw_star(size):
    angle = 144
    for _ in range(5):
        turtle.forward(size)
        turtle.right(angle)

def main():
    screen = turtle.Screen()  
    screen.bgcolor("black")  
    
    turtle.penup()
    turtle.goto(-50, 0)  
    turtle.pendown()
    turtle.color("yellow") 
    
    draw_star(100) 

    turtle.done()  

if __name__ == "__main__":
    main()
