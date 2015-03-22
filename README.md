# RGBBinary-to-PNG

This python script is used to convert raw RGB data to a viewable PNG image using a manually assigned height and width. This can be be used, for example, to decode image data from a DFM or Delphi form. Please note that some RGB binaries, such as the ones used by Delphi forms, contain sync pixels. This application does not account for those pixels nor uses them to set the height and width. If your binary does contain sync pixels, please account for this in your width arguement.

## Usage

```
python rbp.py (INPUT) (OUTPUT) (HEIGHT) (WIDTH)
```

## License

Copyright (c) 2015 Joshua Garde

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

## API

This script contains an API to create PNG files from binary files (DUH)

###To use:
```
import rbp

rbp( [INPUTFILE] [OUTPUTFILE] [HEIGHT] [WIDTH] )
```

## Thanks

A thanks to Johann C. Rocholl, David Jones, and Nicko van Someren for their work on pypng, the library used to create the PNG files. This application is just a simple wrapper to their amazing work. Thanks guys!
