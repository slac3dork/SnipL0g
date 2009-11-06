#!/usr/bin/python
#
# slac3dork[at]gmail[dot]com

def dec2bin(dec):
	bin = ''
	if dec < 0:
		raise ValueError, 'Must be a positive value'
	elif dec == 0:
		return '0'
	else:
		while dec > 0:
			bin = str(dec % 2) + bin
			dec = dec >> 1
		return bin

def bin2dec(bin):
	dec = 0
	bin_val = 0
	str_len = -1
	len_str = len(bin)
	len_str -= 1
	i = 0
	j = len_str

	while (i <= len_str):
		bin_val = bin[i]
		bin_val = int(bin_val)

		if ((bin_val == 1) or (bin_val == 0)):
			dec = dec + ((2**j)*bin_val)
		else:
			dec = 'not binary'
			break

		i += 1
		j -= 1
	return dec

if __name__ == '__main__':
	print '--------------------------'
	print '[+] Binary Converter   [+]'
	print '[+] Coded by slac3dork [+]'
	print '--------------------------\n\n'
	print 'Testing...\n'
	print 'Decimal to Binary'
	print '20: ', dec2bin(20)
	print '100: ', dec2bin(100)
	print '192: ', dec2bin(192)
	print '168: ', dec2bin(168)
	print '\nBinary to Decimal'
	print '100: ', bin2dec('100')
	print '123: ', bin2dec('123')
	print '1111: ', bin2dec('1111')
