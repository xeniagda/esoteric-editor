NB. editm demo



Text=: topara 0 : 0
Send some cool messages in this editor!
)

NB. =========================================================
editmdemo_run=: 3 : 0
wd 'pc editmdemo;pn "Editm Demo"'
wd 'cc ted editm'
wd 'menupop File'
wd '  menu save "Save"'
wd '  menu open "Open"'
wd '  menu saveas "Save As.."'
wd 'menupopz'
wd 'menupop Edit'
wd '  menu find "Find"'
wd '  menu replace "Replace"'
wd '  menu undo "Undo"'
wd '  menu redo "Redo"'
wd 'menupopz'
wd 'set ted stylesheet *color:#00007f;background-color:#ffefd5;font-family:monospace'
wd 'set ted text *',Text
wd 'pmove 100 10 700 500'
wd 'pshow'
NB. call these after the pshow:
wd 'set ted select 1580 1763'
wd 'set ted scroll 15'
)

NB. print editm to default printer:
NB. wd 'cmd ted print'

NB. set line wrap off:
NB. wd 'set ted wrap 0'

NB. set readonly:
NB. wd 'set ted readonly 1'

NB. =========================================================
editmdemo_close=: 3 : 0
wd 'pclose'
showevents_jqtide_ 0
)

editmdemo_close_button=: editmdemo_close

NB. =========================================================
showevents_jqtide_ 2
editmdemo_run''
