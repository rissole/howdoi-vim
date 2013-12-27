if !has('python')
    finish
endif

function! HowDoI()
    pyfile howdoivim.py
endfunc

command! HowDoI call HowDoI()
