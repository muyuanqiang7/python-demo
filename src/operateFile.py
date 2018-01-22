#!/usr/local/bin/python3
# encoding:utf-8


# open a file
import pickle
import pprint
from urllib import request

f = open("./foo.txt", "r+")

# f.write("write Python is the best programming language\n")
print(f.readline())
# close file

f.close()

data1 = {'a': [1, 2.0, 3, 4 + 6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('./data.pkl', 'rb')

# Pickle dictionary using protocol 0.
# pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
# pickle.dump(selfref_list, output, -1)

pprint.pprint(pickle.load(output))

output.close()

response = request.urlopen("http://www.baidu.com")
baidu = open("./baidu.html", "a+")
# baidu.write(response.read().decode('utf-8'))
baidu.writelines(response.read().decode('utf-8'))
baidu.close()
