#!/usr/bin/python

def print_urls(file):
    #Each line is of the form: GET /foo/bar/a.jpg
    #remove the GET and print only /foo/bar/a.jpg

    #use a for-loop to iterate through each line of `file'
    #split the line and print second part
	for line in f:
        	print line.split()[1]

f = open('1.txt')
print_urls(f)
f.close()
 


   
