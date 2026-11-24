from graphics import Canvas
import time


    
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500

fh = 420
fw = 420
thick = 20

fsx = 40
fsy = 40
fex = 40 + fw
fey = 40 + fh

keyboard = {  'A': [-20,0],
              'S': [0,20],
              'D': [20,0],
              'W': [0,-20],
                }

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    w = welcome(canvas)
    row, col = choose_maze(click(canvas))
    for i in w:
        canvas.delete(i)
    title(canvas)
    frame(canvas)
    maze(canvas, row, col)
    g = exit_sign(canvas)
    c,b = character(canvas)
    appear(canvas, g)
    appear(canvas, c)
    
    while not condition(canvas,c,g):
        play_game(canvas,c,g,b)
    print('You win!')
    canvas.create_text(160, 473,
                           text = "You win! 🥳👑🎉🏆",
                           font = 'Arial', font_size = 17, color ='gold')

def click(canvas):
    canvas.wait_for_click()
    clicks = canvas.get_new_mouse_clicks()
    marker = canvas.create_rectangle(clicks[0][0], clicks[0][1], clicks[0][0]+5, clicks[0][1]+5, "black")
    o1 = canvas.find_overlapping(180,220,320,270)
    o2 = canvas.find_overlapping(180,300, 320,350)
    if len(o1) > 3:
        time.sleep(0.2)
        canvas.delete(marker)
        return 1
    elif len(o2) > 3:
        time.sleep(0.2)
        canvas.delete(marker)
        return 2

def welcome(canvas):
    a = canvas.create_rectangle(100,100, 400,400,"white", "black")
    b = canvas.create_text(132, 125, 
                       text = "Welcome to my mazes!",
                       font = 'Arial', font_size = 23, color ='black')
    c = canvas.create_text(172, 160, 
                       text = "Please choose",
                       font = 'Arial', font_size = 23, color ='black')

    d = canvas.create_rectangle(180,220, 320,270,"light green", "black")
    e = canvas.create_text(244, 235, 
                       text = "1",
                       font = 'Arial', font_size = 23, color ='black')

    f = canvas.create_rectangle(180,300, 320,350,"orange", "black")
    g = canvas.create_text(244, 315, 
                       text = "2",
                       font = 'Arial', font_size = 23, color ='black')  
    return (a,b,c,d,e,f,g)
def play_game(canvas,c,g,b):
    print('Press a key in [a,s,d,w] to move: ')
    while not condition(canvas,c,g):
        keys = []
        while keys == []:
            keys = canvas.get_new_key_presses()
            test1(canvas,keys)
            move(canvas, keys,c,g)
            here(canvas, c, b)
            if keys == ['UNKNOWN_KEY']:
                time.sleep(0.1)
            
            
def move(canvas, keys,c,g):
    for i in keys:
        for r in keyboard.keys():
            if i == r:
                new_x = canvas.get_left_x(c) + keyboard[r][0]
                new_y = canvas.get_top_y(c) + keyboard[r][1]
                canvas.moveto(c, new_x, new_y)
                test2(canvas, keys, c, g, r,  new_x, new_y)
                

def test2(canvas, keys, c, g, r,  new_x, new_y):
    objs1 = canvas.find_overlapping(new_x, new_y, new_x+20, new_y+20)
    objs2 = canvas.find_overlapping(40, 460, 60, 480)
    objs3 = canvas.find_overlapping(80, 460, 100, 480)
    objs4 = canvas.find_overlapping(60, 480, 80, 500)

    if len(objs1)>1 and not condition(canvas,c,g):
        print("You can't go through the wall! :>>")
        a = canvas.create_text(120, 473,
                           text = "You can't go through the wall! :>>",
                           font = 'Arial', font_size = 17, color ='black')
        time.sleep(0.25)
        old_x = new_x - keyboard[r][0]
        old_y = new_y - keyboard[r][1]
        canvas.moveto(c, old_x, old_y)
        time.sleep(0.25)
        canvas.delete(a)

    if objs2 != [] or objs3 != [] or objs4 != [] :
        print("Don't run away! :>>")
        a = canvas.create_text(180, 473,
                           text = "Don't run away! :>>",
                           font = 'Arial', font_size = 17, color ='black')
        time.sleep(0.2)
        old_x = new_x - keyboard[r][0]
        old_y = new_y - keyboard[r][1]
        canvas.moveto(c, old_x, old_y)
        time.sleep(0.25)
        canvas.delete(a)
    
def test1(canvas, keys):
    for i in keys:
            if i!= 'A' and i!= 'W' and i!= 'S' and i!='D' and i != 'UNKNOWN_KEY':
                print('You entered an invalid key. Try again.')
                x = canvas.create_text(105, 470,
                           text = "Invalid key. Try again.",
                           font = 'Arial', font_size = 15, color ='black')
                time.sleep(0.45)
                canvas.delete(x)
def condition(canvas,c,g):
    return (
        canvas.get_left_x(c) == canvas.get_left_x(g)
        and
        canvas.get_top_y(c) == canvas.get_top_y(g)
            )

def appear(canvas, a):
    time.sleep(0.05)
    canvas.set_hidden(a, True)
    time.sleep(0.05)
    canvas.set_hidden(a, False)  
    time.sleep(0.05)
    canvas.set_hidden(a, True)
    time.sleep(0.05)
    canvas.set_hidden(a, False)

def here(canvas, a, b):
    lx = canvas.get_left_x(a)
    ty = canvas.get_top_y(a)
    if lx != 60 or ty != 460:
        canvas.delete(b)

def character(canvas):
    a = canvas.create_oval(60,460,80,480, "orange", "black")
    b = canvas.create_text(105, 485, 
                           text = "⬉ You're here!",
                           font = 'Arial', font_size = 15, color ='black')   
    return a,b
def exit_sign(canvas):
    a = canvas.create_polygon(460,60,480,70,460,80, color ="red", outline = "black")
    return a

def choose_maze(number):
    row1 = {80:  [[100, 2], [200,2], [340,4]],
            120: [[60,2], [140,8], [360,3]],
            160: [[60,2], [220,5]],
            200: [[100,2], [200,3], [300,5]],
            240: [[80,6], [260,2], [320,4]],
            280: [[140,2], [320,4]],
            320: [[140,4], [340,5]],
            360: [[80,3], [200,3], [360,3]],
            400: [[60,2], [220,4]],
            }

    col1 = {    80:  [[80,2], [180,2], [260,4]], 
                120: [[120,3], [280,3], [380,3]], 
                160: [[60,3], [160,4], [340,4]], 
                200: [[140,2], [240,5], [380,2]], 
                240: [[80,2], [220,7]], 
                280: [[60,2], [180,3], [280,7]], 
                320: [[80,5], [300,6]], 
                360: [[140,2], [380,3]], 
                400: [[140,4], [240,3], [380,2]], 
                }        
    
    row2 = {80:  [[100, 2], [200,2], [320,4]],
            120: [[60,2], [140,9], [360,4]],
            160: [[60,2], [220,4], [400,2]],
            200: [[100,2], [200,3], [280,6]],
            240: [[80,6], [260,3], [340,5]],
            280: [[140,2], [280,3], [360,3]],
            320: [[140,4], [340,5]],
            360: [[80,3], [200,3], [360,3]],
            400: [[60,2], [220,4]],
            }

    col2 = {    80:  [[80,2], [180,2], [260,4]], 
                120: [[120,3], [280,3], [380,3]], 
                160: [[80,2], [160,4], [340,4]], 
                200: [[140,2], [240,5], [380,2]], 
                240: [[80,2], [220,7]], 
                280: [[60,2], [300,5]], 
                320: [[80,5], [320,5]], 
                360: [[140,2], [380,3]], 
                400: [[60,2], [200,2], [380,2]], 
                }
    if number == 1:
        return row1, col1
    if number == 2:
        return row2,col2

def maze(canvas,rows, columns):
    for i in rows.keys():
        for r in range(len(rows[i])):
            draw_a_row(canvas, rows[i][r][0], i, rows[i][r][1] )
            time.sleep(0.03)
    for i in columns.keys():
        for r in range(len(columns[i])):
            draw_a_column(canvas, i, columns[i][r][0], columns[i][r][1] )
            time.sleep(0.04)
def frame(canvas):
    canvas.create_rectangle(fsx           , fsy           , fex         , fsx + thick , 'green')
    time.sleep(0.1)
    canvas.create_rectangle(fsx           , fsy + thick   , fsx + thick ,fey          , 'green')
    time.sleep(0.1)
    canvas.create_rectangle(fex - thick   , fsy + thick*2 , fex         ,fey          , 'green')
    time.sleep(0.1)
    canvas.create_rectangle(fsx + thick*2 , fey - thick   , fex - thick ,fey          , 'green')

def title(canvas):
    canvas.create_text(
    150, 
    13, 
    text = "'A' ⇦   'S' ⇩    'D' ⇨   'W' ⇧",
    font = 'Arial', 
    font_size = 18, 
    color ='black'
)

def draw_a_row(canvas, start_x, start_y, a):
    end_x = start_x + thick*a
    end_y = start_y + thick
    canvas.create_rectangle(
    start_x, start_y,
    end_x, end_y, 
    "light green", "green"
    )


def draw_a_column(canvas, start_x, start_y, a):
    end_x = start_x + thick
    end_y = start_y + thick*a
    canvas.create_rectangle(
    start_x, start_y,
    end_x, end_y, 
    "light green", "green"
    )
if __name__ == '__main__':
    main()