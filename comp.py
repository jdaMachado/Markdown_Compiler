from sys import *


def open_file(filename):
    with open(filename, 'r') as lines:
        return lexer(lines)

def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])


def run():
    data = open_file(argv[1])
    return data


def lexer(lines):
    final = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"> </head><body>'
    special_symbols = ["#", "!", "\n"]
    
    for each_line in lines:

    
#       Title
        if (each_line[0]=='!'):

            titlestring = each_line[1:-1]
            final = replace_str_index(final, 59, "<title>" + titlestring + "</title>")
        
#       Paragraph
        if (each_line[0] not in special_symbols):

            pstring = each_line[:-1]
            final += "<p>" + pstring + "</p>"
              
#       H1
        if (each_line[0]=='#' and each_line[1] != '#'):

            hstring = each_line[1:-1]
            final += '<h1>' + hstring + '</h1>'

#       H2
        if (each_line[0]=='#' and each_line[1] == '#' and each_line[2] != '#'):
            hstring = each_line[2:-1]
            final += '<h2>' + hstring + '</h2>'

#       H3
        if (each_line[0]=='#' and each_line[1] == '#' and each_line[2] == '#'):
            hstring = each_line[3:-1]
            final += '<h3>' + hstring + '</h3>'

#   Final
        
    final += '</body></html>'
    return final

with open('teste.html', 'w') as htmlfile: # Writes the output of run into a document.
    htmlfile.write(run())

print(run())

            