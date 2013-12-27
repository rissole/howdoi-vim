import sys
try:
    import vim
    from howdoi import howdoi

    query = vim.current.line.split()
    result = howdoi.howdoi({'query': query, 'pos': 1, 'num_answers': 1, 'all': False, 'link': False, 'color': False, 'clear_cache': False}).strip().split('\n')
    vim.current.range.append(result)
    vim.command(':d') # delete the original line
    vim.command(':normal '+str(len(result))+'==') # re indent lines
except ImportError as e:
    sys.stderr.write('You need to install howdoi: pip install howdoi')
