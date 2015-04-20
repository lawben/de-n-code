Decoder Tool
============

A small tool to en-/decode with XOR or Caesar cipher.
---------------------------------------------------

usage: decode.py string {xor,caesar} (-d | -e) [-t TOP] [-b BOTTOM] [-k KEY]
                 
positional arguments:
string              The plain text or cipher string to be used.
{xor,caesar}        Select 'xor' or 'caesar' to use the corresponding method.

optional arguments:  
-h, --help            show this help message and exit  
-d, --decode          Selct to decode a cipher text.  
-e, --encode          Select to encode a plain text.  
-t TOP, --top TOP     Set top of range for decoding. Default: 256  
-b BOTTOM, --bottom BOTTOM
                      Set bottom of range for decoding. Default: 0  
-k KEY, --key KEY     Set key value for encoding.
