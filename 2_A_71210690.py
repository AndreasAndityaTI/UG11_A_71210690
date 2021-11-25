def ambil_huruf(karakter,urutan= None):
	if urutan == None:
		if len(karakter)%2 == 0:
			hasil = karakter[int(((len(karakter))/2))]
		else:
			hasil = karakter[int(((len(karakter) - 1)/2))]
		return hasil
	else:
		if len(karakter)%2 == 0:
			hasil = karakter[int(((len(karakter))/2) + urutan)]
		else:
			hasil = karakter[int(((len(karakter) - 1)/2) + urutan)]
		return hasil
	
print(ambil_huruf("abcdefg", 1))
print(ambil_huruf("abcdefg", 2))
print(ambil_huruf("abcd"))