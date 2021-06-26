#This is a small python script for autmatically creating a table of contents for a .md file
#If you are confused as to how to use this, ask me.

def getGitAnchor(name):
    acc = '#'
    i = 0

    while i < len(name):
        if name[i].lower() != name[i].upper():
            acc += name[i].lower()
        elif name[i] == ' ':
            acc += '-'
        i += 1

    return acc

def autoTOC(md, indentSub = 2, indent = '\t'):

    acc = ''

    for line in md.split('\n'):
        stripped = line.lstrip()

        indents = 0
        while indents < len(stripped):
            if stripped[indents] != '#':
                break
            indents += 1

        if indents > 0:
            stripped = stripped[indents+1:]
            indents = max(0,indents-indentSub)
            acc += indent*indents + '* ['+stripped+']('+getGitAnchor(stripped)+')\n'

    return acc

doc = '''Put what you want to make a table of contents of here'''

print(autoTOC(doc))
