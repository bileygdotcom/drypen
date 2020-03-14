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


def draw_menu(stdscr):
    
    #get terminal image
    tifile = open("drydock-logo.ti","r")
    tilist = tifile.readlines()
    tifile.close()
    
    #get config
    conffile = open("drydock-2.cfg","r")
    conflist = conffile.readlines()
    conffile.close()

    #config lists
    F1conf = [conflist[1][1:-1],conflist[2][0:-1],conflist[3][0:-1],conflist[4][0:-1],conflist[5][0:-1],conflist[6][0:-1],conflist[7][0:-1],conflist[8][0:-1],conflist[9][0:-1],conflist[10][0:-1],conflist[11][0:-1]]
    F2conf = [conflist[12][1:-1],conflist[13][0:-1],conflist[14][0:-1],conflist[15][0:-1],conflist[16][0:-1],conflist[17][0:-1],conflist[18][0:-1],conflist[19][0:-1],conflist[20][0:-1],conflist[21][0:-1],conflist[22][0:-1]]
    F3conf = [conflist[23][1:-1],conflist[24][0:-1],conflist[25][0:-1],conflist[26][0:-1],conflist[27][0:-1],conflist[28][0:-1],conflist[29][0:-1],conflist[30][0:-1],conflist[31][0:-1],conflist[32][0:-1],conflist[33][0:-1]]
    F4conf = [conflist[34][1:-1],conflist[35][0:-1],conflist[36][0:-1],conflist[37][0:-1],conflist[38][0:-1],conflist[39][0:-1],conflist[40][0:-1],conflist[41][0:-1],conflist[42][0:-1],conflist[43][0:-1],conflist[44][0:-1]]
    F5conf = [conflist[45][1:-1],conflist[46][0:-1],conflist[47][0:-1],conflist[48][0:-1],conflist[49][0:-1],conflist[50][0:-1],conflist[51][0:-1],conflist[52][0:-1],conflist[53][0:-1],conflist[54][0:-1],conflist[55][0:-1]]
    F6conf = [conflist[56][1:-1],conflist[57][0:-1],conflist[58][0:-1],conflist[59][0:-1],conflist[60][0:-1],conflist[61][0:-1],conflist[62][0:-1],conflist[63][0:-1],conflist[64][0:-1],conflist[65][0:-1],conflist[66][0:-1]]
    F7conf = [conflist[67][1:-1],conflist[68][0:-1],conflist[69][0:-1],conflist[70][0:-1],conflist[71][0:-1],conflist[72][0:-1],conflist[73][0:-1],conflist[74][0:-1],conflist[75][0:-1],conflist[76][0:-1],conflist[77][0:-1]]
    F8conf = [conflist[78][1:-1],conflist[79][0:-1],conflist[80][0:-1],conflist[81][0:-1],conflist[82][0:-1],conflist[83][0:-1],conflist[84][0:-1],conflist[85][0:-1],conflist[86][0:-1],conflist[87][0:-1],conflist[88][0:-1]]
    F9conf = [conflist[89][1:-1],conflist[90][0:-1],conflist[91][0:-1],conflist[92][0:-1],conflist[93][0:-1],conflist[94][0:-1],conflist[95][0:-1],conflist[96][0:-1],conflist[97][0:-1],conflist[98][0:-1],conflist[99][0:-1]]
    F10conf = [conflist[100][1:-1]]
    F11conf = [conflist[101][1:-1]]
    F12conf = [conflist[102][1:-1]]
    Term = [conflist[103][0:-1]]
    Terminal = Term[0]  

    #config matrix
    Fconf = [0,F1conf,F2conf,F3conf,F4conf,F5conf,F6conf,F7conf,F8conf,F9conf,F10conf,F11conf,F12conf]
    
    #k - is the pressed key variable. set it on 0
    k = 0
    cursor_x = 0
    cursor_y = 0

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
    
    
    # F Done
    F1_Done  = [False, False, False, False, False, False]
    F2_Done  = [False, False, False, False, False, False]
    F3_Done  = [False, False, False, False, False, False]
    F4_Done  = [False, False, False, False, False, False]
    F5_Done  = [False, False, False, False, False, False]
    F6_Done  = [False, False, False, False, False, False]
    F7_Done  = [False, False, False, False, False, False]
    F8_Done  = [False, False, False, False, False, False]
    F9_Done  = [False, False, False, False, False, False]
    F10_Done = [False, False, False, False, False, False]
    F11_Done = [False, False, False, False, False, False]
    F12_Done = [False, False, False, False, False, False]
    
    F_Done = [False, F1_Done, F2_Done, F3_Done, F4_Done, F5_Done, F6_Done, F7_Done, F8_Done, F9_Done, F10_Done, F11_Done, F12_Done]
    
    #some preliminary vars
    showWindow = True
    out = "currently no comands"
    err = "no messages yet"
    softpath = '/opt/pilot-server'
    Ftitle = " No selection "
    #frontscreen (first menu) is
    MenuState = 0
    
    #number text
    N_text1 = " 1 "
    N_text2 = " 2 "
    N_text3 = " 3 "
    N_text4 = " 4 "
    N_text5 = " 5 "
    
    #button states
    doneF2_1 = False
    doneF2_2 = False
    doneF2_3 = False
    doneF2_4 = False
    
    #button text
    Ftext_1_1 = "no text yet 1 - 1"
    Ftext_1_2 = "no text yet 1 - 2"
    Ftext_2_1 = "no text yet 2 - 1"
    Ftext_3_1 = "no text yet 3 - 1"
    Ftext_4_1 = "no text yet 4 - 1"
    Ftext_5_1 = "no text yet 5 - 1"

    # Loop where k is the last character pressed
    #while (k != ord('q')):
    while (k != curses.KEY_F12):

        # Initialization
        stdscr.erase()
        height, width = stdscr.getmaxyx()

        # It's all about cursor
        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1
        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)
        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)
        
        #stringaz = "funky people never understood a man with the only rapping soul Pos: {}, {}".format(cursor_x, cursor_y)
        stringaz = ""
        
        ################################################################
        ## DEFINITION OF F-KEYS ########################################
        ################################################################
        
        #path where Pilot-Server is 
        softpath = '/opt/pilot-server'
        if os.path.isdir(softpath):
            direxists = True
        else:
            direxists = False
            
        if k == curses.KEY_F1:
            MenuState = 1
        if k == curses.KEY_F2:
            MenuState = 2
        if k == curses.KEY_F3:
            MenuState = 3
        if k == curses.KEY_F4:
            MenuState = 4
        if k == curses.KEY_F5:
            MenuState = 5
        if k == curses.KEY_F6:
            MenuState = 6
        if k == curses.KEY_F7:
            MenuState = 7
        if k == curses.KEY_F8:
            MenuState = 8
        if k == curses.KEY_F9:
            MenuState = 9
        if k == curses.KEY_F10:
            MenuState = 10
        if k == curses.KEY_F11:
            MenuState = 11
        if k == curses.KEY_F12:
            MenuState = 12
            
        ## END OF DEFINITION OF F-KEYS #################################
        
                
        ################################################################
        ##   MENUSTATE != 0 ############################################
        ################################################################
        
        if MenuState != 0:
            
            MS = MenuState
            stringaz = Fconf[MS][0]
            Ftitle = " "+Fconf[MS][0]+"         "
            showWindow = True

            Ftext_1_1 = Fconf[MS][1]
            Ftext_2_1 = Fconf[MS][3]
            Ftext_3_1 = Fconf[MS][5]
            Ftext_4_1 = Fconf[MS][7]
            Ftext_5_1 = Fconf[MS][9]            
            
            if k == ord('1') or k == ord('2') or k == ord('3') or k == ord('4') or k == ord('5'):
                if k == ord('1'):
                    key = 2
                    grn = 1
                if k == ord('2'):
                    key = 4
                    grn = 2
                if k == ord('3'):
                    key = 6
                    grn = 3
                if k == ord('4'):
                    key = 8
                    grn = 4
                if k == ord('5'):
                    key = 10
                    grn = 5
             
                #Terminal = 'gnome-terminal'
                command = Terminal + ' -- ' + Fconf[MS][key]
                p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                F_Done[MS][grn] = True
                
        ## END OF MENUSTATE != 0  ######################################
        
              
        ################################################################
        # MENUSTATE = 0 ################################################
        ################################################################
        
        # Declaration of about strings
        B = '\U00002588'
        title = "Terminal User interface for Linux"
        subtitle = "Made with Python3 Curses"
        keystr = "bileyg | Sankt-Peterburg"
        
        
        # Centering calculations
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        
        start_x_logo = int((width // 2) - (len(tilist[0]) // 2) - len(tilist[0]) % 2) - 2
        start_y = int((height // 2) - 2)
        
        center_y = int((height// 2))
        center_x = int((width // 2))
        
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
            
            # Rendering subtitle
            
            #stdscr.attron(curses.color_pair(2))
            #stdscr.attron(curses.A_BOLD)
            #stdscr.addstr(start_y+5, start_x_title, title)
            #stdscr.attroff(curses.color_pair(2))
            #stdscr.attroff(curses.A_BOLD)
            # Print rest of text
            
            #stdscr.addstr(start_y + 6, start_x_keystr, keystr)
            #stdscr.move(cursor_y, cursor_x)
            
        # End of F9 ###########################################

        ################################################################
        ## TOPPER ######################################################
        ################################################################
        
        # Topper showing the coordinates
        whstr = "W-H: [{},{}]".format(width, height)
        
        ################################################################
        ## TOPPER BAR ##################################################
        ################################################################
        
        topperstr1 = whstr
        #topperstr1 = ' \U00002297' + '  DRYDOCK v.0.02 '
        #topperstr2 = ' \U00002297' + '  terminal launcher by bileyg'
        topperstr3 = " "
        
        topperstr1 = "Last key pressed: {}".format(k)[:width-1]
        topperstr2 = "Pos: {}, {}".format(cursor_x, cursor_y)
        
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
        
        #normalization of names for menu
        Fconf0names = []
        for i in range(1,13):
            Fconf0 = Fconf[i][0]
            scl = len(Fconf0)
            if scl > 10:
                sss = (Fconf0[0:10])
            elif scl == 10:
                sss = Fconf0
            else:
                ascl = 10 - scl
                sss = Fconf0[0:10] + ' '*ascl
            Fconf0names.append(sss)
        FCN = Fconf0names
            
        if height >= 23 and width >= 79:
            
            #statusbar menu set
            statusbarstr2 = " "+FCN[0]+" | "+FCN[1]+" | "+FCN[2]+" | "+FCN[3]+" | "+FCN[4]+" | "+FCN[5]+" |"
            statusbarstr1 = " "+FCN[6]+" | "+FCN[7]+" | "+FCN[8]+" | "+FCN[9]+" | "+FCN[10]+" | "+FCN[11]+" |"
            
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
        
        
        ################################################################
        ## WINDOW ######################################################
        ################################################################
        
        # The window stuff (inserting preliminary set "stringaz")
        
        if showWindow == True and height >= 22 and width >= 79:
            #center_y = int(height//2)
            #center_x = int(width //2)
            
            if height < 24:
                wHeight = height - 8
                begin_y = 4
            else:
                wHeight = 16
                begin_y = center_y - wHeight//2
                    
            if width <= 80:
                wWidth = width - 8
                begin_x = 4
            else:
                wWidth = 70
                begin_x = center_x - wWidth//2
            
            if height == 24 and width == 80:
                begin_x = 1; begin_y = 4
                wHeight = height - 7; wWidth = width - 2
        
            winn = curses.initscr()        
            winn = curses.newwin(wHeight, wWidth, begin_y, begin_x)
            
            if F_Done[MenuState][1] == False:
                cpair_1 = 6
            else:
                cpair_1 = 8
            winn.attron(curses.color_pair(cpair_1))
            winn.attron(curses.A_BOLD)
            winn.addstr(4,2,N_text1)
            winn.attroff(curses.A_BOLD)
            winn.attroff(curses.color_pair(cpair_1))
            
            if F_Done[MenuState][2] == False:
                cpair_2 = 6
            else:
                cpair_2 = 8            
            winn.attron(curses.color_pair(cpair_2))
            winn.attron(curses.A_BOLD)
            winn.addstr(6,2,N_text2)
            winn.attroff(curses.A_BOLD)
            winn.attroff(curses.color_pair(cpair_2))
            
            if F_Done[MenuState][3] == False:
                cpair_3 = 6
            else:
                cpair_3 = 8            
            winn.attron(curses.color_pair(cpair_3))
            winn.attron(curses.A_BOLD)
            winn.addstr(8,2,N_text3)
            winn.attroff(curses.A_BOLD)
            winn.attroff(curses.color_pair(cpair_3))
            
            if F_Done[MenuState][4] == False:
                cpair_4 = 6
            else:
                cpair_4 = 8
            winn.attron(curses.color_pair(cpair_4))
            winn.attron(curses.A_BOLD)
            winn.addstr(10,2,N_text4)
            winn.attroff(curses.A_BOLD)
            winn.attroff(curses.color_pair(cpair_4))
            
            if F_Done[MenuState][5] == False:
                cpair_5 = 6
            else:
                cpair_5 = 8
            winn.attron(curses.color_pair(cpair_5))
            winn.attron(curses.A_BOLD)
            winn.addstr(12,2,N_text5)
            winn.attroff(curses.A_BOLD)
            winn.attroff(curses.color_pair(cpair_5))
            
            #this could be used for scenario with installation (complex)
            #if direxists == False:
            #    winn.addstr(4,7,Ftext_1_1)
            #else:
            #    winn.addstr(4,7,Ftext_1_2)
            
            #this section shows strings from .config after buttons with digits
            winn.addstr(4,7,Ftext_1_1)
            winn.addstr(6,7,Ftext_2_1)
            winn.addstr(8,7,Ftext_3_1)
            winn.addstr(10,7,Ftext_4_1)
            winn.addstr(12,7,Ftext_5_1)
            
            winn.border()
        
            winn.refresh()
        
            # label window
            ginn = curses.initscr()        
            ginn = curses.newwin(3, 18, begin_y, begin_x)
            ginn.attron(curses.color_pair(5))
            ginn.addstr(1,1,Ftitle)
            ginn.attroff(curses.color_pair(5))
            ginn.border()
            ginn.refresh()
        
            # terminal error windows
            #tw1 = curses.initscr()        
            #tw1 = curses.newwin(4, wWidth-2, height-8, begin_x+1)
            #tw1.attron(curses.color_pair(3))
            #tw1.addstr(1,1," OUTPUT: ")
            #tw1.attroff(curses.color_pair(3))
            #tw1.addstr(1,11,err)
            #tw1.border()
            #tw1.refresh()
        
            # terminal output windows
            #tw2 = curses.initscr()        
            #tw2 = curses.newwin(3, wWidth-2, height-13, begin_x+1)
            #tw2.attron(curses.color_pair(3))
            #tw2.addstr(1,1," OUT: ")
            #tw2.attroff(curses.color_pair(3))
            #tw2.addstr(1,9,out)
            #tw2.attroff(curses.color_pair(3))
            #tw2.border()
            #tw2.refresh()
         
        F_Done[5][3] = False
        F_Done[7][1] = False
        
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
