# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 21:27:00 2021

@author: imamc
"""

jwb = "y"
while jwb=="y" or jwb=="Y":
    print("===========================")
    print(" LORENA EXSPEDITION ")
    print("===========================")
    print("a = Surabaya")
    print("b = Bandung")
    print(" ")

    kode =('a','b')
    kota = ('Surabaya','Bandung')
    jarak = (169,452)
    ongkirperkm = (2500,4000)

    pilihan = input(">> Masukkan Kode Tujuan = ")
    index = 0
    while index < len(kode):
        if kode[index] == pilihan:

            print(">>> Pilihan Tujuan   = " + kota[index ])
            print(">>> Jarak            = " + str(jarak[index]) + " km")
            print(">>> Ongkir per Km    = Rp. " + str(ongkirperkm[index]))

            ongkir = jarak[index] * ongkirperkm[index]

            print(">>>> Total           = Rp. " + str(ongkir))
            print(" ")
            print("====================================")
	#index dari index 0 adalah kode a(surabaya), 
	#fungsi index + 1 adalah misal anda memlilih kode b maka akan dibaca index 0+1=1 
    #jadi kode b ada index ke 1, dst
        index = index + 1 
        
# break
    jwb = input(">>> Apakah Anda ingin input lagi ? y/t : ")
    if jwb== "t" or jwb=="T":
        break