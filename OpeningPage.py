import simplegui

header = "Welcome to my game app!"
header2 = "There are plenty of games to choose form in the menu below! Have fun!"

# Handler for mouse click
def click():
    global message
    message = "Good job!"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(header, [50,112], 48, "Red")
    canvas.draw

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 3000, 2000)
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
