#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  drypen.py
#  
#  Copyright 2020 bileyg <bileyg@bodhi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sys,os
import curses
import subprocess
import resource
from getpass import getpass 

def saveImage(tilist):
    # Saving the file with picture    
    tirec = tilist
    tirec[0] = "__|0         1         2         3         4         5         6         7         8"+"\n"
    tirec[1] = "__#012345678901234567890123456789012345678901234567890123456789012345678901234567890"+"\n"
    tirec[2] = "__|---------------------------------------------------------------------------------"+"\n"
    for j in range(3,22):
        tirec[j] = tilist [j]
    tirec[23]= "20|000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    with open(r"./image/workimage.ti", "w") as file:
        #file.writelines("%s\n" % line for line in tilist)
        file.writelines(line for line in tirec)

def loadImage():
    #get terminal image
    tifile = open("./image/workimage.ti","r")
    tilist = tifile.readlines()
    tifile.close()
    tirec = tilist
    return (tilist)

def draw_menu(stdscr):
    
    #get terminal image
    tifile = open("drypen-logo.ti","r")
    tilist = tifile.readlines()
    tifile.close()
    
    tirec = tilist
    
    #k - is the pressed key variable. set it on 0
    k = 0
    cursor_x = 0
    cursor_y = 2

    # Clear and refresh the screen for a blank canvas
    stdscr.erase()
    stdscr.refresh()
    
    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
    curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(9, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(10, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(11, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    #colors for logo. 
    curses.init_pair(20, curses.COLOR_BLACK,  curses.COLOR_WHITE)
    curses.init_pair(21, curses.COLOR_RED,    curses.COLOR_WHITE)
    curses.init_pair(22, curses.COLOR_GREEN,  curses.COLOR_WHITE)
    curses.init_pair(23, curses.COLOR_YELLOW, curses.COLOR_WHITE)
    curses.init_pair(24, curses.COLOR_BLUE,   curses.COLOR_WHITE)
    curses.init_pair(25, curses.COLOR_MAGENTA,curses.COLOR_WHITE)
    curses.init_pair(26, curses.COLOR_CYAN,   curses.COLOR_WHITE)
    curses.init_pair(27, curses.COLOR_WHITE,  curses.COLOR_BLACK)
    curses.init_pair(28, curses.COLOR_BLACK,  curses.COLOR_WHITE)
    curses.init_pair(29, curses.COLOR_RED,    curses.COLOR_WHITE)
    curses.init_pair(30, curses.COLOR_GREEN,  curses.COLOR_WHITE)
    curses.init_pair(31, curses.COLOR_YELLOW, curses.COLOR_WHITE)
    curses.init_pair(32, curses.COLOR_BLUE,   curses.COLOR_WHITE)
    curses.init_pair(33, curses.COLOR_MAGENTA,curses.COLOR_WHITE)
    curses.init_pair(34, curses.COLOR_CYAN,   curses.COLOR_WHITE)
    curses.init_pair(35, curses.COLOR_WHITE,  curses.COLOR_BLACK)

    #some preliminary vars
    showCommandBar = False
    showWindow = True
    #out = "currently no comands"
    #err = "no messages yet"
    #softpath = '/opt/pilot-server'
    #Ftitle = " No selection "
    #frontscreen (first menu) is
    MenuState = 0
    PixelColors = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    pixelkey = 'Q'
    
    # Declaration of about strings
    B = '\U00002588'
    title = "Terminal User interface for Linux"
    subtitle = "Made with Python3 Curses"
    keystr = "bileyg | Sankt-Peterburg"
    
    # MAIN LOOP where k is the last character pressed
    while (k != curses.KEY_F12):

        # WINDOW Initialization
        stdscr.erase()
        height, width = stdscr.getmaxyx()
        
        # Centering calculations
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        
        start_x_logo = int((width // 2) - (len(tilist[0]) // 2) - len(tilist[0]) % 2) - 2
        start_y = int((height // 2) - 2)
        
        center_y = int((height// 2))
        center_x = int((width // 2))

        # It's all about cursor 
        #movement
        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1
        #limits
        cursor_x = max(center_x-78//2-1, cursor_x)
        cursor_x = min(center_x+78//2-1, cursor_x)
        cursor_y = max(center_y-20//2, cursor_y)
        cursor_y = min(center_y+20//2-2, cursor_y)
        #cursor recalc
        cursor_x_rec = cursor_x - (width-78)//2 + 1
        cursor_y_rec = cursor_y - (height-20)//2
        
        #stringaz = "funky people never understood a man with the only rapping soul Pos: {}, {}".format(cursor_x, cursor_y)
        stringaz = ""        
              
        ################################################################
        # MENUSTATE = 0 ################################################
        ################################################################
        
        if MenuState == 0:
            
            showWindow = False
            #winn.erase()
            
            # Rendering logo
            # from the terminal image strings
        
            PixelMatrix = []
            PixelString = []
            PixelColors = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
            if height >= 23 and width >= 80:
                
                for j in range(3,22):
                    PixelString = tilist[j]
                    for i in range(3,82):
                        Pixel = tilist[j][i]
                        #print('got it')
                        #print(Pixel)
                        PColor = PixelColors.index(Pixel)
                        stdscr.attron(curses.color_pair(20+PColor))
                        if PColor > 7:
                            stdscr.attron(curses.A_BOLD)
                        XX = (center_x - (len(PixelString)-4)//2-3)
                        YY = (center_y - 13)
                        stdscr.addstr(j+YY, i+XX, B)
                        #stdscr.addstr(start_y+j-11, start_x_logo+i, 'B')
                        if PColor > 7:
                            stdscr.attroff(curses.A_BOLD)
                        stdscr.attroff(curses.color_pair(20+PColor))
            
            # Drawing part
            
            if k == curses.KEY_HOME:
                pixelkey = 'Q'
            
            if k == ord('1'):
                pixelkey = '1'
            if k == ord('2'):
                pixelkey = '2'
            if k == ord('3'):
                pixelkey = '3'
            if k == ord('4'):
                pixelkey = '4'
            if k == ord('5'):
                pixelkey = '5'
            if k == ord('6'):
                pixelkey = '6'
            if k == ord('7'):
                pixelkey = '7'
            if k == ord('8'):
                pixelkey = '8'
            if k == ord('9'):
                pixelkey = '9'
            if k == ord('0'):
                pixelkey = '0'
            if k == ord('a'):
                pixelkey = 'A'
            if k == ord('b'):
                pixelkey = 'B'
            if k == ord('c'):
                pixelkey = 'C'
            if k == ord('d'):
                pixelkey = 'D'
            if k == ord('e'):
                pixelkey = 'E'
            if k == ord('f'):
                pixelkey = 'F'
            
            # Put the PixelColor in Tilist to form the picture
            if pixelkey in PixelColors:
                tistring = tilist[int(cursor_y_rec+3)]
                tiarr    = [x for x in tistring]
                tiarr[int(cursor_x_rec+3)] = pixelkey
                tistring = ''.join(tiarr)
                tilist[int(cursor_y_rec+3)] = tistring
            
            # Saving the file with picture    
            if k == curses.KEY_F2:
                saveImage(tilist)
                #tirec[0] = "__|0         1         2         3         4         5         6         7         8"+"\n"
                #tirec[1] = "__#012345678901234567890123456789012345678901234567890123456789012345678901234567890"+"\n"
                #tirec[2] = "__|---------------------------------------------------------------------------------"+"\n"
                #for j in range(3,22):
                #    tirec[j] = tilist [j]
                #tirec[23]= "20|000000000000000000000000000000000000000000000000000000000000000000000000000000000"
                #with open(r"./image/workimage.ti", "w") as file:
                #    #file.writelines("%s\n" % line for line in tilist)
                #    file.writelines(line for line in tirec)
                    
            # Load the picture
            if k == curses.KEY_F3:
                tilist = loadImage()                
                    
            # Clear the picture off
            if k == curses.KEY_F8:
                for j in range(3,22):
                    tilist[j] = "__|" + '0' * 81+"\n" 
                #limits
                cursor_x = center_x-78//2-1
                cursor_y = center_y-20//2

        ################################################################
        ## TOPPER ######################################################
        ################################################################
        
        # Topper showing the coordinates
        whstr = "W-H: [{},{}]".format(width, height)
        
        ################################################################
        ## TOPPER BAR ##################################################
        ################################################################
        
        topperstr1 = whstr
        topperstr1 = ' \U00002297' + '  DRYPEN v.0.01 - terminal drawing tool by bileyg'
        #topperstr2 = ' \U00002297' + '  terminal drawing tool by bileyg'
        topperstr3 = " "
        
        #topperstr1 = "Last key pressed: {}".format(k)[:width-1]
        topperstr2 = " F2 - Save | F3 - Load | F8 - Clear Screen | F12 - Exit | HOME - Drop Color | "
        
        # Render topper1
        stdscr.attron(curses.color_pair(7))
        stdscr.addstr(0, 0, topperstr1)
        stdscr.addstr(0, len(topperstr1), " " * (width - len(topperstr1) - 1))
        stdscr.attroff(curses.color_pair(7))
        
        # Render topper2
        stdscr.attron(curses.color_pair(4))
        stdscr.addstr(1, 0, topperstr2)
        stdscr.addstr(1, len(topperstr2), " " * (width - len(topperstr2) - 1))
        stdscr.attroff(curses.color_pair(4))
        
        ## END OF TOPPER ###############################################
        
        ################################################################
        ## STATUS BAR ##################################################
        ################################################################
        
        sbpair1 = 9
        sbpair2 = 3
        ###############################################################################################
            
        if height >= 23 and width >= 79:
            
            if showCommandBar == True:
                statusbarstr2 = 'statusbarstr2'
                statusbarstr1 = 'statusbarstr1'
                
            else:
                statusbarstr2 = "Colors 1"
                statusbarstr1 = "Colors 2"
                for c in range (0,8):
                    stdscr.attron(curses.color_pair(20 + c))
                    if c > 7:
                            stdscr.attron(curses.A_BOLD)
                    stdscr.addstr(height-2, center_x - 37 + c*9, B + B + B + B + B + B + B + B + B)
                    stdscr.attroff(curses.color_pair(20 + c))
                    if c > 7:
                            stdscr.attroff(curses.A_BOLD)
                    stdscr.attron(curses.color_pair(11))
                    stdscr.attron(curses.A_BOLD)
                    stdscr.addstr(height-2, center_x - 37 + c*9, " " + PixelColors[c] + " ")
                    stdscr.attroff(curses.A_BOLD)
                    stdscr.attroff(curses.color_pair(11))
                for c in range (8,16):
                    stdscr.attron(curses.color_pair(20 + c))
                    if c > 7:
                            stdscr.attron(curses.A_BOLD)
                    stdscr.addstr(height-1, center_x - 37 + (c-8)*9, B + B + B + B + B + B + B + B + B)
                    stdscr.attroff(curses.color_pair(20 + c))
                    if c > 7:
                            stdscr.attroff(curses.A_BOLD)
                    stdscr.attron(curses.color_pair(11))
                    stdscr.attron(curses.A_BOLD)
                    stdscr.addstr(height-1, center_x - 37 + (c-8)*9, " " + PixelColors[c] + " ")
                    stdscr.attroff(curses.A_BOLD)
                    stdscr.attroff(curses.color_pair(11))
            
            # Bar over colors
            statusbarstr3 = "Cursor  Position: {}, {}".format(cursor_x_rec, cursor_y_rec)
            stdscr.attron(curses.color_pair(sbpair2))
            stdscr.addstr(height-3, 0, " " * (width - 1))
            stdscr.addstr(height-3, center_x - 37, statusbarstr3)
            stdscr.attroff(curses.color_pair(sbpair2))

        else:
            statusbarstr2 = "79x23"
            statusbarstr1 = "minimum"
            # Render status bar
            stdscr.attron(curses.color_pair(sbpair1))
            stdscr.addstr(height-1, 0, statusbarstr1)
            stdscr.addstr(height-1, len(statusbarstr1), " " * (width - len(statusbarstr1) - 1))
            stdscr.attroff(curses.color_pair(sbpair1))
            # Render top status bar
            stdscr.attron(curses.color_pair(sbpair2))
            stdscr.addstr(height-2, 0, statusbarstr2)
            stdscr.addstr(height-2, len(statusbarstr2), " " * (width - len(statusbarstr2) - 1))
            stdscr.attroff(curses.color_pair(sbpair2))
        
        ## END OF STATUSBAR ############################################
            
            winn.border()
        
            winn.refresh()
        
        #cursor move works if right before the refresh()
        stdscr.move(cursor_y, cursor_x)
        
        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()
        



def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()
