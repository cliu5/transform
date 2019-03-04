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
    f=open(fname,'r')
    script=f.read()
    commands=f.readlines()
    for i in range(len(commands)):
        if commands[i]=='line':
            points=commands[i+1]
            coordinates=points.split(" ")
            add_edge(points,int(coordinates[0]),int(coordinates[1]),int(coordinates[2]),int(coordinates[3]),int(coordinates[4]),int(coordinates[5]))
        elif commands[i]=='ident':
            ident(transform)
        elif commands[i]=='scale':
            points=commands[i+1]
            coordinates=points.split(" ")
            newMatrix=make_scale(int(coordinates[0]),int(coordinates[1]),int(coordinates[2]))
            matrix_mult(newMatrix,transform)
        elif commands[i]=='translate':
            points=commands[i+1]
            coordinates=points.split(" ")
            newMatrix=make_translate(int(coordinates[0]),int(coordinates[1]),int(coordinates[2]))
            matrix_mult(newMatrix,transform)
        elif commands[i]=='rotate':
            points=commands[i+1]
            coordinates=points.split(" ")
            axis=coordinates[0]
            theta=int(coordinates[1])
            if axis=='x':
                newMatrix=make_rotX(theta)
            elif axis=='y':
                newMatrix=make_rotY(theta)
            elif axis=='z':
                newMatrix=make_rotZ(theta)
            matrix_mult(newMatrix,transform)
        elif commands[i]=='apply':
            matrix_mult(transform,points)
        elif commands[i]=='display':
            for x in range(len(points)):
                for y in range(len(points[0])):
                    points[x][y] = int(points[x][y])
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        elif commands[i]=='save':
            clear_screen(screen)
            points = commands[i+1]
            coordinates = points.split(" ")
            filename = coordinates[0]
            draw_lines(points, screen, color)
            save_extension(screen, filename)
        elif commands[i] == 'quit':
            break
    f.close()



