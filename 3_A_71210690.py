def hitung_hapus():
	kalimat = input("Masukkan kalimat: ")
	istart = int(input("Index Start :")) + 1
	istop = int(input("Index Stop :")) + 1
	dihapus = istop - istart + 1
	hasil = (dihapus/len(kalimat))*100
	
	if istart > len(kalimat) or istop > len(kalimat):
		return 0.0
	elif hasil < 0:
		return 0.0
	else:
		return hasil
	
print(hitung_hapus())
