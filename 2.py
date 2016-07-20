#!/usr/bin/python

def eliminate_duplicates_and_print_sorted(file):
    #remove duplicate lines from `file' and print the sorted lines
    #hint: you can use a set and also the "sorted" function
	r = sorted(set(file))
    	for line in r:
       		print line

if __name__ == '__main__':
    eliminate_duplicates_and_print_sorted(open('out1.txt'))
    
