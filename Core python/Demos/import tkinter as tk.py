import tkinter as tk

# Create window
root = tk.Tk()
root.title("GUI Animation")
root.geometry("600x400")

# Create canvas
canvas = tk.Canvas(root, width=600, height=400, bg="black")
canvas.pack()

# Create ball
ball = canvas.create_oval(50, 180, 90, 220, fill="cyan")

dx = 4  # movement speed

def animate():
    global dx
    canvas.move(ball, dx, 0)
    pos = canvas.coords(ball)

    # Bounce from walls
    if pos[2] >= 600 or pos[0] <= 0:
        dx = -dx

    root.after(20, animate)  # repeat animation

animate()
root.mainloop()
