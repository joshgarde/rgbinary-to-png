# RGBBinary-to-PNG
#
# Copyright (c) 2015 Joshua Garde
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import sys
import png

# API
def rbp ( read, write, height, width ):
	writer = png.Writer(width, height)
	t = []
	s = []
	counter = 0
	for x in read.read():
		if counter == width * 3:
			s += [tuple(t)]
			del t[:]
			t += [ord(x)]
			counter = 1
		else:
			t += [ord(x)]
			counter += 1
	s += [tuple(t)]
	writer.write(write, s)
	write.close
	read.close

print 'RGBBinary-to-PNG'
print
if len(sys.argv) == 1:
	print 'Usage: python rbp.py (BinaryFile) (OutputFile) (Height) (Width)'
	exit()
else:
	try:
		readf = open(sys.argv[1], 'rb')
		writef = open(sys.argv[2], 'wb')
		height = int(sys.argv[3])
		width = int(sys.argv[4])
	except IOError as err:
		print err.filename + ': ' + err.strerror
	except ValueError as err:
		print 'Unexpected type received. Expected int.'
print 'BinaryFile: ' + sys.argv[1]
print 'OutputFile: ' + sys.argv[2]
print 'Height: ' + str(height)
print 'Width : ' + str(width)
print 'Converting...'
rbp(readf, writef, height, width)
print 'Done.'
