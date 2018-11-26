from sys import *

def open_file(filename):
    data = open(filename, "r").read()
    return data

def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])


def run():
    data = open_file(argv[1])
    return lexer(data)


    
def lexer(filecontents):
    filecontents = list(filecontents)
    isItalic = False
    final = '<!DOCTYPE html><html lang="en"><head> </head><body>'
    special_symbols = ["#", "_", "\n", "!"]
    bold_italic = ["*", "_"]
    i = 0


    while(i<len(filecontents)):
        
        #Title
        if ( (filecontents[i-1] == "\n" or i == 0 ) and filecontents[i] == "!"):
            i = i + 1
            titlestring = ""
            while ( i < len(filecontents)):
                if ( filecontents[i]=="!" and filecontents[i-1] != "\\"):
                    break
                titlestring += filecontents[i]
                i += 1
                
            final = replace_str_index(final, 37, "<title>" + titlestring + "</title>")
        
# Paragraphs
    #Paragraph at the start of a document
        if ( i == 0 and filecontents[i] not in special_symbols): 
            pstring0 = ""
            x=0
            while ( i < len(filecontents)):

                if (filecontents[i]=="\n"):
                    break

                
                pstring0 += filecontents[i] 

                if (filecontents[i] in bold_italic ): #Italic
                    if (isItalic):
                        isItalic = False
                        pstring0 = replace_str_index(pstring0, x, "</em>")
                    else:
                        isItalic = True
                        pstring0 = replace_str_index(pstring0, x, "<em>")
                        x = x + 3 
                        

                x += 1
                i += 1
                             
            final += "<p>" + pstring0 + "</p>" 

    # Only applies if there's more than one line
        if ( len(filecontents) >= i+1): 

    #Paragraph after a blank line
            if ( filecontents[i] == "\n" and filecontents[i+1] == "\n"): 
                pstring1 = ""
                i = i+2
                x = 0
                while ( i < len(filecontents)):
                    if (filecontents[i] in special_symbols):
                        break

                    pstring1 += filecontents[i]

                    if (pstring1[x] in bold_italic ): #Italic 
                        if (isItalic):
                            isItalic = False
                            pstring1 = replace_str_index(pstring1, x, "</em>")
                        else:
                            isItalic = True
                            pstring1 = replace_str_index(pstring1, x, "<em>")
                            x=x+3 

                    print(pstring1)

                            
                    x += 1
                    i += 1

                
                final += "<p>" + pstring1 + "</p>" 
        i += 1
                   


    # Only applies if there's more than one line
        #if ( len(filecontents) >= i+1): 

    # #Paragraph after a new line        
    #         if ( filecontents[i] == "\n" and filecontents[i-1] != "\n" and filecontents[i+1] not in special_symbols): 
    #             i = i + 1
    #             pstring2 = ""
    #             while ( i < len(filecontents)):
    #                 if (filecontents[i] in special_symbols):
    #                     break
    #                 pstring2 += filecontents[i]
    #                 i += 1
    #             final += "<p>" + pstring2 + "</p>"
          
              

        # #H1
        # if ( filecontents[i] == "#" and filecontents[i-1] != "#" and filecontents[i+1] != "#"):
        #     x = i + 1
        #     h1string = ""
        #     while ( x < len(filecontents)):
        #         if ( filecontents[x]=="\n"):
        #             break
        #         h1string += filecontents[x]
        #         x += 1
                
        #     final += "<h1>" + h1string + "</h1>"  

        # #H2
        # if ( filecontents[i] == "#" and filecontents[i-1] != "#" and filecontents[i+1] == "#" and filecontents[i+2] != "#"):
        #     x = i + 2
        #     h2string = ""
        #     while ( x < len(filecontents)):
        #         if ( filecontents[x]=="\n"):
        #             break
        #         h2string += filecontents[x]
        #         x += 1
                
        #     final += "<h2>" + h2string + "</h2>"

        # #H3
        # if ( filecontents[i] == "#" and filecontents[i-1] != "#" and filecontents[i+1] == "#" and filecontents[i+2] == "#" and filecontents[i+3] != "#"):
        #     x = i + 3
        #     h3string = ""
        #     while ( x < len(filecontents)):
        #         if ( filecontents[x]=="\n"):
        #             break
        #         h3string += filecontents[x]
        #         x += 1
                
        #     final += "<h3>" + h3string + "</h3>"

        # #Italic
        # if (filecontents[i] in bold_italic and filecontents[i+1] not in bold_italic and filecontents[i-1] not in bold_italic):
        #     x = i + 1
        #     italicstring = ""
        #     while ( x < len(filecontents)):
        #         if (filecontents[x] in bold_italic and filecontents[x-1] != "\\"):
        #             break
        #         italicstring += filecontents[x]
        #         x += 1
                
        #     final += "<em>" + italicstring + "</em>"

        # #Bold
        # if (filecontents[i] in bold_italic and filecontents[i-1] not in bold_italic and filecontents[i+1] in bold_italic and filecontents[i+2] not in bold_italic):
        #     x = i + 2
        #     boldstring = ""
        #     while ( x < len(filecontents)):
        #         if (filecontents[x] in bold_italic and filecontents[x-1] != "\\"):
        #             break
        #         boldstring += filecontents[x]
        #         x += 1
                
        #     final += "<strong>" + boldstring + "</strong>"

#Final
    if ( i >= len(filecontents)):
        final += '</body></html>'
        return final



with open('teste.html', 'w') as htmlfile:
    htmlfile.write(run())
                  