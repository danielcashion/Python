'''
Initial creation of folder
'''
import urllib

# file location for the master word list.

url = "https://drive.google.com/file/d/0B4niqV00F3msaFZGUEZNTGtBblU/view/LoughranMcDonald_MasterDictionary_2016.csv"
#I hate the fact that this is a static location and will likely break with updates. But it is out of my control.

#download in chunks
file_name = url.split('/')[-1]
u = urllib.request.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()


  
