"""
MIT License

Copyright (c) 2018 Piotr Bazydło

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import json
import binascii
import base64

if __name__ == "__main__":
	
	#import json
	with open('neverlan.opvault/default/profile.js') as f:
		# s=f.read()[12:-1]
		profile = json.loads(f.read()[12:-1])


	#get data for hashcat input
	out = list()
	#hash - last 32 bytes of masterKey - decode from base64 and save as hex
	out.append(binascii.hexlify(base64.decodestring(profile['masterKey'])[-32::]))
	#salt - decode from base64 and save as hex
	out.append(binascii.hexlify(base64.decodestring(profile['salt'])))
	#iterations
	out.append(str(profile['iterations']))
	#data - rest of the masterKey - decode from base64 and save as hex
	out.append(binascii.hexlify(base64.decodestring(profile['masterKey'])[0:-32]))

	#create output
	out_str = ':'.join(out)

	with open('out.txt','w+') as f:
		f.write(out_str)

	print out_str
