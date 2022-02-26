"""
ini adalah percobaan project01 untuk penajaman python
coba terus 
"""

print ("hai dunya")
print ("tetep asyik")

ingin_cepat = False
if ingin_cepat:
    print('jalan lurus aja ya!')
else:
    print('Jalan lain')


jumlah_anak = 4

for index_anak in range(1, jumlah_anak+1): #jumlah perulangan = 5 - 1 = 4
    print(f'Halo anak #{index_anak}')


susu = 1
telur = 6
if susu == 1 and telur == 6:
    print ('budi akhirnya membeli susu :', susu, 'dan telur :', telur)
elif susu == 1 and telur < 6:
    print ('budi akhirnya membeli susu :', susu, ' saja')
else :
    print ('budi pulang tanpa belanja apapun')