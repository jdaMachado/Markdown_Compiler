from sys import *
import re


def open_file(filename):
    with open(filename, 'r') as lines:
        return lexer(lines)

def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

def bold(text):                                                         #Regex code used from Carlos Quental @https://github.com/carlosquental/marcabaixo/blob/master/marcabaixo.py
    text = re.sub(r'\*{2}(.*)\*{2}', '<strong>\\1</strong>', text)
    text = re.sub(r'_{2}(.*)_{2}', '<strong>\\1</strong>', text)
    return text
    
def italic(text):                                                       #Regex code used from Carlos Quental @https://github.com/carlosquental/marcabaixo/blob/master/marcabaixo.py
    text = re.sub(r'\*(.*)\*', '<em>\\1</em>', text)
    text = re.sub(r'_(.*)_', '<em>\\1</em>', text)
    return text

def close_ul(boolean):
    global openul
    if boolean:
        openul = False
        return '</ul>'
    else:
        return ''

def close_ol(boolean):
    global openol
    if boolean:
        openol = False
        return '</ol>'
    else:
        return ''


def run():
    data = open_file(argv[1])
    return data


def lexer(lines):
    final = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"> </head><body>'
    special_symbols = ["#", "!", "\n", '-']
    openul = False
    openol = False

    
    
    for each_line in lines:

        each_line = bold(each_line)
        each_line = italic(each_line)
        
#       Title
        if (each_line[0]=='!'):

            final += close_ul(openul)
            final += close_ol(openol)

            titlestring = each_line[1:-1] if each_line[-1] =='\n' else each_line[1:]
            final = replace_str_index(final, 59, "<title>" + titlestring + "</title>")
        
#       Paragraph
        if (each_line[0] not in special_symbols) and not (each_line[0].isdigit() and each_line[1] == '.'):

            final += close_ul(openul)
            final += close_ol(openol)

            pstring = each_line[:-1] if each_line[-1] =='\n' else each_line[:]
            final += "<p>" + pstring + "</p>"
              
#       H1
        if (each_line[0]=='#' and each_line[1] != '#'):

            final += close_ul(openul)
            final += close_ol(openol)

            hstring = each_line[1:-1] if each_line[-1] =='\n' else each_line[1:]
            final += '<h1>' + hstring + '</h1>'

#       H2
        if (each_line[0]=='#' and each_line[1] == '#' and each_line[2] != '#'):

            final += close_ul(openul)
            final += close_ol(openol)

            hstring = each_line[2:-1] if each_line[-1] =='\n' else each_line[2:]
            final += '<h2>' + hstring + '</h2>'

#       H3
        if (each_line[0]=='#' and each_line[1] == '#' and each_line[2] == '#'):

            final += close_ul(openul)
            final += close_ol(openol)

            hstring = each_line[3:-1] if each_line[-1] =='\n' else each_line[3:]
            final += '<h3>' + hstring + '</h3>'

#       UL
        if (each_line[0]=='-' and each_line[1] == ' '):
            if not openul:
                final += '<ul>'
                openul = True
            listring = each_line[2:-1] if each_line[-1] =='\n' else each_line[2:]
            final += '<li>' + listring + '</li>'

#       OL
        if (each_line[0].isdigit() and each_line[1] == '.'):
            if not openol:
                final += '<ol>'
                openol = True
            listring = each_line[2:-1] if each_line[-1] =='\n' else each_line[2:]
            final += '<li>' + listring + '</li>'
            

#   Final
        
    final += '</body></html>'
    return final

with open('test.html', 'w') as htmlfile: # Writes the output of run into a document.
    htmlfile.write(run())

print(run())         