# -*- coding: utf-8 -*-

"""
Created on Sun Apr 17 09:53:31 2022

@author: fmuror02
"""  

def FraseComprehension():
    
    from urllib.request import urlopen
    url = "https://output.jsbin.com/ludenar"
    url2 = "https://output.jsbin.com/donerab"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    
    page2 = urlopen(url2)
    html2_bytes = page2.read()
    html2 = html2_bytes.decode("utf-8")
    
    print('Python code which analyzes easy frases to see if they are good or bad.')
    print('Frases have to be: Pronoun + verb to be + adjective')
    print('Example: I am bad.')
    
    fo = input('Enter easy frase:')
    
    file1 = open('Memory1.txt','r')
    text1 = file1.read()
    file2 = open('Memory2.txt','r')
    text2 = file2.read()
    
    if fo in text1:
        print('That is good.\m')
    elif fo in text2:
        print('That is bad.\m')
    else:
        pass
        
        
    f = fo.split()
    b = f[1]
    c = f[2]
    if c == 'not':
        d = f[3]
    
        z = 2
        
        if d in html:
            z = z + 0.1
        if d in html2:
            z = z + 0.2
        
        if z == 3.1:
            print("That is good.")
            st = 1
        elif z == 3.2:
            print("That is bad.")
            st = 0
        elif z == 2.1:
            print("That is bad.")
            st = 0
        elif z == 2.2:
            print("That is good.")
            st = 1

        
    
    else:
        if "'" in b:
            z = 2
        else:
            z = 3
        
        if c in html:
            z = z + 0.1
        if c in html2:
            z = z + 0.2

            
        
        if z == 3.1:
            print("That is good.")
            st = 1
        elif z == 3.2:
            print("That is bad.")
            st = 0
        elif z == 2.1:
            print("That is bad.\m")
            st = 0
        elif z == 2.2:
            print("That is good.\m")
            st = 1

  
    if st == 1:
        file = open('Memory1.txt',"a")
        file.write(fo+"   ")
        file.close()
    elif st == 0:
        file = open('Memory2.txt',"a")
        file.write(fo+"   ")
        file.close()
        
            


FraseComprehension()
input()


    
    
    
    
    







