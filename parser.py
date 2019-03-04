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
	 move: create a translation matrix,
	    then multiply the transform matrix by the translation matrix -
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing
See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname,'r')
    script = f.read()
    commands = script.split('\n')
    for i in range(len(commands)):
        if commands[i] == 'line':
            coordinates=commands[i+1].split(" ")
            x0 = int(coordinates[0])
            y0 = int(coordinates[1])
            z0 = int(coordinates[2])
            x1 = int(coordinates[3])
            y1 = int(coordinates[4])
            z1 = int(coordinates[5])
            add_edge(points, x0, y0, z0, x1, y1, z1)
        elif commands[i] == 'ident':
            ident(transform)
        elif commands[i] == 'scale':
            coordinates=commands[i+1].split(" ")
            sx = int(coordinates[0])
            sy = int(coordinates[1])
            sz = int(coordinates[2])
            smatrix = make_scale(sx, sy, sz)
       	    matrix_mult( smatrix, transform )
        elif commands[i] == 'move':
            coordinates=commands[i+1].split(" ")
            tx = int(coordinates[0])
            ty = int(coordinates[1])
            tz = int(coordinates[2])
            tmatrix = make_translate(tx, ty, tz)
       	    matrix_mult(tmatrix,transform )
        elif commands[i] == 'rotate':
            coordinates=commands[i+1].split(" ")
            axis = coordinates[0]
            theta = int(coordinates[1])
            if axis == 'x':
                rmatrix = make_rotX(theta)
            elif axis == 'y':
                rmatrix = make_rotY(theta)
            elif axis == 'z':
                rmatrix = make_rotZ(theta)
       	    matrix_mult( rmatrix, transform )
        elif commands[i] == 'apply':
            matrix_mult(transform, points)
        elif commands[i] == 'display':
            for x in range(len(points)):
		for y in range(4):
		    points[x][y] = int(points[x][y])
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        elif commands[i] == 'save':
            coordinates=commands[i+1].split(" ")
            filename = coordinates[0]
            draw_lines(points, screen, color)
            save_extension(screen, filename)
        elif commands[i] == 'quit':
            break
    f.close()
