
import requests
def print_urls(file):

     for line in f:
        print line.split()[1]


f = open('1.txt')
print_urls(f) 

 

def eliminate_duplicates_and_sort(file):
    r = sorted(set(file))
    for line in r:
        print line

if __name__ == '__main__':
    eliminate_duplicates_and_sort(open('out1.txt'))
    

def save_image(url, filename):
    print url
    r = requests.get(url)
    f = open(filename, 'w')
    f.write(r.content)
    f.close()


def main():

    filename = 0
    url_base = 'http://code.google.com'
    
    for url in open('out2.txt'):
        save_image(url_base + url.strip() , "images/" + str(filename) + ".jpg")
        print 'saved file %d' % filename
        filename += 1

main()


print """<html>
         <head><title>Images</title></head>
         <body>
      """

for i in range(0,40):
    print '<img src="%s">' % (str(i) + ".jpg")


print """</body></<html>"""
