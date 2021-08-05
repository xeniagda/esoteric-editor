# Tcl GUI
# Code: GUIC
# Esoteric editor
# By Razetime
package require Tk

#Menus
menu .mbar
. configure -menu .mbar

menu .mbar.fl -tearoff 0
.mbar add cascade -menu .mbar.fl -label File \
    -underline 0
.mbar.fl add command -label "Open File"
.mbar.fl add command -label "Open Folder"
.mbar.fl add command -label "Save"
.mbar.fl add command -label "Save As"
.mbar.fl add command -label "Exit" -command { exit }

menu .mbar.ed -tearoff 0
.mbar add cascade -menu .mbar.ed -label Edit \
    -underline 0
.mbar.ed add command -label "Undo"
.mbar.ed add command -label "Redo"
.mbar.ed add command -label "Cut"
.mbar.ed add command -label "Copy"
.mbar.ed add command -label "Paste"
.mbar.ed add command -label "Find"
.mbar.ed add command -label "Replace"

.mbar add command -label "Help"

grid [text .myText -background white -foreground black -borderwidth 1 -padx 10 -pady 10 -font {"Courier New" -18 bold}]


wm minsize . 600 600
wm title . "Esoteric Editor"
wm geometry . 300x200+100+100
