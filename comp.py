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
    isBold = False
    final = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"> </head><body>'
    special_symbols = ["#", "\n", "!"]
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
                
            final = replace_str_index(final, 59, "<title>" + titlestring + "</title>")
        
# Paragraphs

        #Paragraph at the start of a document
        if ( i == 0 and filecontents[i] not in special_symbols): 
            pstring0 = ""
            em_counter=0
            strong_counter=0
            while ( i < len(filecontents)):

                if (filecontents[i]=="\n"):
                    break

                
                pstring0 += filecontents[i] 
                

                # Checks for Bold markdown
                if (filecontents[i] in bold_italic and filecontents[i+1] in bold_italic): 
                    if (isBold):
                        isBold = False
                        pstring0 = replace_str_index(pstring0, strong_counter, "</strong>")
        
                    else:
                        isBold = True
                        pstring0 = replace_str_index(pstring0, strong_counter, "<strong>")
                        strong_counter += 7 #Needs to compensate for the replacement of one character {*} with eight characters {<strong>}.
                        em_counter += 13 #Needs to compensate for the replacement of one character {*} with 13 characters {</strong><em>}

                        
                if (filecontents[i] in bold_italic and filecontents[i-1] in bold_italic):
                    pstring0 = pstring0.replace('*', '')
                    pstring0 = pstring0.replace('_', '')


                # Checks for Italic markdown
                if (filecontents[i] in bold_italic and filecontents[i+1] not in bold_italic and filecontents[i-1] not in bold_italic): 
                    if (isItalic):
                        isItalic = False
                        pstring0 = replace_str_index(pstring0, em_counter, "</em>")
        
                    else:
                        isItalic = True
                        pstring0 = replace_str_index(pstring0, em_counter, "<em>")
                        em_counter +=  3 #Needs to compensate for the replacement of one character {*} with four characters {<em>}.
                        strong_counter += 13 #Needs to compensate for the replacement of one character {*} with 13 characters {</em><strong>}.

                strong_counter += 1         
                em_counter += 1
                i += 1
                             
            final += "<p>" + pstring0 + "</p>" 


        # Tests for out of index range
        if ( len(filecontents) >= i): 

            #Paragraph after a blank line
            if ( filecontents[i] == "\n" and filecontents[i+1] == "\n"): 
                pstring1 = ""
                i = i + 2
                strong_counter = 0 
                em_counter = 0
                while ( i < len(filecontents)):
                    if (filecontents[i] in special_symbols):
                        break

                    pstring1 += filecontents[i]
                    
                     # Checks for Bold markdown
                    if (filecontents[i] in bold_italic and filecontents[i+1] in bold_italic): 
                        if (isBold):
                            isBold = False
                            pstring1 = replace_str_index(pstring1, strong_counter, "</strong>")
            
                        else:
                            isBold = True
                            pstring1 = replace_str_index(pstring1, strong_counter, "<strong>")
                            strong_counter += 7 #Needs to compensate for the replacement of one character {*} with eight characters {<strong>}.
                            em_counter += 13 #Needs to compensate for the replacement of one character {*} with 13 characters {</strong><em>}

                            
                    if (filecontents[i] in bold_italic and filecontents[i-1] in bold_italic):
                        pstring1 = pstring1.replace('*', '')
                        pstring1 = pstring1.replace('_', '')


                    # Checks for Italic markdown
                    if (filecontents[i] in bold_italic and filecontents[i+1] not in bold_italic and filecontents[i-1] not in bold_italic): 
                        if (isItalic):
                            isItalic = False
                            pstring1 = replace_str_index(pstring1, em_counter, "</em>")
            
                        else:
                            isItalic = True
                            pstring1 = replace_str_index(pstring1, em_counter, "<em>")
                            em_counter +=  3 #Needs to compensate for the replacement of one character {*} with four characters {<em>}.
                            strong_counter += 13 #Needs to compensate for the replacement of one character {*} with 13 characters {</em><strong>}.

                    strong_counter += 1         
                    em_counter += 1
                    i += 1

                if ( len(pstring1)>0):
                    final += "<p>" + pstring1 + "</p>" 

            #Paragraph after a new line        
            if ( filecontents[i] == "\n" and filecontents[i-1] != "\n" and filecontents[i+1] not in special_symbols): 
                i = i + 1
                em_counter = 0
                strong_counter = 0
                pstring2 = ""
                while ( i < len(filecontents)):
                    if (filecontents[i] in special_symbols):
                        break

                    pstring2 += filecontents[i]

                    # Checks for Bold markdown
                    if (filecontents[i] in bold_italic and filecontents[i+1] in bold_italic): 
                        if (isBold):
                            isBold = False
                            pstring2 = replace_str_index(pstring2, strong_counter, "</strong>")
            
                        else:
                            isBold = True
                            pstring2 = replace_str_index(pstring2, strong_counter, "<strong>")
                            strong_counter += 7 #Needs to compensate for the replacement of one character {*} with eight characters {<strong>}.
                            em_counter += 13 #Needs to compensate for the replacement of one character {*} with 13 characters {</strong><em>}

                            
                    if (filecontents[i] in bold_italic and filecontents[i-1] in bold_italic):
                        pstring2 = pstring1.replace('*', '')
                        pstring2 = pstring1.replace('_', '')


                    # Checks for Italic markdown
                    if (filecontents[i] in bold_italic and filecontents[i+1] not in bold_italic and filecontents[i-1] not in bold_italic): 
                        if (isItalic):
                            isItalic = False
                            pstring2 = replace_str_index(pstring2, em_counter, "</em>")
            
                        else:
                            isItalic = True
                            pstring2 = replace_str_index(pstring2, em_counter, "<em>")
                            em_counter +=  3 #Needs to compensate for the replacement of one character {*} with four characters {<em>}.
                            strong_counter += 13 #Needs to compensate for the replacement of one character {*} with 13 characters {</em><strong>}.

                    strong_counter += 1         
                    em_counter += 1
                    i += 1

                final += "<p>" + pstring2 + "</p>"
          
              
        #H1
        if ( filecontents[i] == "#" and filecontents[i-1] != "#" and filecontents[i+1] != "#"):
            i = i + 1
            em_counter = 0
            strong_counter = 0
            h1string = ""
            while ( i < len(filecontents)):
                if ( filecontents[i]=="\n"):
                    break

                h1string += filecontents[i]

                # Checks for Bold markdown
                if (filecontents[i] in bold_italic and filecontents[i+1] in bold_italic): 
                    if (isBold):
                        isBold = False
                        h1string = replace_str_index(h1string, strong_counter, "</strong>")
        
                    else:
                        isBold = True
                        h1string = replace_str_index(h1string, strong_counter, "<strong>")
                        strong_counter += 7 #Needs to compensate for the replacement of one character {*} with eight characters {<strong>}.
                        em_counter += 13 #Needs to compensate for the replacement of one character {*} with 13 characters {</strong><em>}

                        
                if (filecontents[i] in bold_italic and filecontents[i-1] in bold_italic):
                    h1string = h1string.replace('*', '')
                    h1string = h1string.replace('_', '')


                # Checks for Italic markdown
                if (filecontents[i] in bold_italic and filecontents[i+1] not in bold_italic and filecontents[i-1] not in bold_italic): 
                    if (isItalic):
                        isItalic = False
                        h1string = replace_str_index(h1string, em_counter, "</em>")
        
                    else:
                        isItalic = True
                        h1string = replace_str_index(h1string, em_counter, "<em>")
                        em_counter +=  3 #Needs to compensate for the replacement of one character {*} with four characters {<em>}.
                        strong_counter += 13 #Needs to compensate for the replacement of one character {*} with 13 characters {</em><strong>}.

                strong_counter += 1         
                em_counter += 1
                i += 1
                   
            final += "<h1>" + h1string + "</h1>"
        
        # Tests for out of index range
        if len(filecontents) >= i+1:
            #H2
            if ( filecontents[i] == "#" and filecontents[i-1] != "#" and filecontents[i+1] == "#" and filecontents[i+2] != "#"):
                i = i + 2
                em_counter = 0
                strong_counter = 0
                h2string = ""
                while ( i < len(filecontents)):
                    if ( filecontents[i]=="\n"):
                        break

                    h2string += filecontents[i]

                    # Checks for Bold markdown
                    if (filecontents[i] in bold_italic and filecontents[i+1] in bold_italic): 
                        if (isBold):
                            isBold = False
                            h2string = replace_str_index(h2string, strong_counter, "</strong>")
            
                        else:
                            isBold = True
                            h2string = replace_str_index(h2string, strong_counter, "<strong>")
                            strong_counter += 7 #Needs to compensate for the replacement of one character {*} with eight characters {<strong>}.
                            em_counter += 13 #Needs to compensate for the replacement of one character {*} with 13 characters {</strong><em>}

                            
                    if (filecontents[i] in bold_italic and filecontents[i-1] in bold_italic):
                        h2string = h2string.replace('*', '')
                        h2string = h2string.replace('_', '')


                    # Checks for Italic markdown
                    if (filecontents[i] in bold_italic and filecontents[i+1] not in bold_italic and filecontents[i-1] not in bold_italic): 
                        if (isItalic):
                            isItalic = False
                            h2string = replace_str_index(h2string, em_counter, "</em>")
            
                        else:
                            isItalic = True
                            h2string = replace_str_index(h2string, em_counter, "<em>")
                            em_counter +=  3 #Needs to compensate for the replacement of one character {*} with four characters {<em>}.
                            strong_counter += 13 #Needs to compensate for the replacement of one character {*} with 13 characters {</em><strong>}.

                    strong_counter += 1         
                    em_counter += 1
                    i += 1
                    
                final += "<h2>" + h2string + "</h2>"
        
        # Tests for out of index range
        if len(filecontents) >= i+2:
            #H3
            if ( filecontents[i] == "#" and filecontents[i-1] != "#" and filecontents[i+1] == "#" and filecontents[i+2] == "#" and filecontents[i+3] != "#"):
                i = i + 3
                em_counter = 0
                strong_counter = 0
                h3string = ""
                while ( i < len(filecontents)):
                    if ( filecontents[i]=="\n"):
                        break

                    h3string += filecontents[i]

                    # Checks for Bold markdown
                    if (filecontents[i] in bold_italic and filecontents[i+1] in bold_italic): 
                        if (isBold):
                            isBold = False
                            h3string = replace_str_index(h3string, strong_counter, "</strong>")
            
                        else:
                            isBold = True
                            h3string = replace_str_index(h3string, strong_counter, "<strong>")
                            strong_counter += 7 #Needs to compensate for the replacement of one character {*} with eight characters {<strong>}.
                            em_counter += 13 #Needs to compensate for the replacement of one character {*} with 13 characters {</strong><em>}

                            
                    if (filecontents[i] in bold_italic and filecontents[i-1] in bold_italic):
                        h3string = h3string.replace('*', '')
                        h3string = h3string.replace('_', '')


                    # Checks for Italic markdown
                    if (filecontents[i] in bold_italic and filecontents[i+1] not in bold_italic and filecontents[i-1] not in bold_italic): 
                        if (isItalic):
                            isItalic = False
                            h3string = replace_str_index(h3string, em_counter, "</em>")
            
                        else:
                            isItalic = True
                            h3string = replace_str_index(h3string, em_counter, "<em>")
                            em_counter +=  3 #Needs to compensate for the replacement of one character {*} with four characters {<em>}.
                            strong_counter += 13 #Needs to compensate for the replacement of one character {*} with 13 characters {</em><strong>}.

                    strong_counter += 1         
                    em_counter += 1
                    i += 1
                    
                final += "<h3>" + h3string + "</h3>"

        i += 1 # While-loop counter.

    #Final
    if ( i >= len(filecontents)):
        final += '</body></html>'
        return final

with open('teste.html', 'w') as htmlfile: # Writes the output of run into a document.
    htmlfile.write(run())              