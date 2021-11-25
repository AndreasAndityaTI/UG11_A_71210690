def ambildanbalik(karakter,indexmulai,indexakhir,syarat):
	if syarat == False:
		hasilbalik = karakter[indexmulai-1:indexakhir]
	else:
		hasilbalik = karakter[indexakhir-1:indexmulai-2:-1]
	return hasilbalik
	
print(ambildanbalik("abcdefg",2,4,True))
print(ambildanbalik("abcdefg",1,5,False))
print(ambildanbalik("qwerty",3,4,True))
print(ambildanbalik("qwerty",2,2,False))