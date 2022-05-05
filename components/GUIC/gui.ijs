NB. editm demo



Text=: topara 0 : 0
Paragraph of text.
)

NB. =========================================================
editmdemo_run=: 3 : 0
wd 'pc editmdemo;pn "Editm Demo"'
wd 'cc ted editm'
wd 'set ted stylesheet *color:#00007f;background-color:#ffefd5'
wd 'set ted text *',Text
wd 'bin zhs'
wd 'cc ok button;cn OK'
wd 'cc close button;cn Close'
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
