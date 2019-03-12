from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing
See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    line = open(fname,'r').read().split('\n')
    for i in range(len(line)):
        if line[i] == 'line':
            i += 1
            coors = line[i].split(' ')
            x0 = int(coors[0])
            y0 = int(coors[1])
            z0 = int(coors[2])
            x1 = int(coors[3])
            y1 = int(coors[4])
            z1 = int(coors[5])
            add_edge(points,x0,y0,z0,x1,y1,z1)
            
        if line[i] == "ident":
            ident(transform)

        if line[i] == "scale":
            i += 1
            coors = line[i].split(' ')
            x = int(coors[0])
            y = int(coors[1])
            z = int(coors[2])
            matrix_mult(make_scale(x,y,z),transform)
        
        if line[i] == "translate":
            i += 1
            coors = line[i].split(' ')
            x = int(coors[0])
            y = int(coors[1])
            z = int(coors[2])
            matrix_mult(make_translate(x,y,z),transform)
            
        if line[i] == "rotate":
            i += 1
            coors = line[i].split(' ')
            theta = int(coors[1])
            if coors[0] == 'x':
                matrix_mult(make_rotX(theta),transform)
            elif coors[0] == 'y':
                matrix_mult(make_rotY(theta),transform)
            elif coors[0] == 'z':
                matrix_mult(make_rotZ(theta),transform)
        
        if line[i] == 'apply':
            matrix_mult(transform,points)
        
        if line[i] == 'display':
            clear_screen(screen)
            draw_lines(points,screen,color)
            display(screen)
        
        if line[i] == 'save':
            i += 1
            filename = line[i]
            clear_screen(screen)
            draw_lines(points,screen,color)
            save_extension(screen,filename)
        
        if line[i] == 'quit':
return
