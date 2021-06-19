# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 12:21:58 2021

@author: imamc
"""

jwb = "y"
while jwb=="y" or jwb=="Y":
    print("""
          ===========================
          TOKO BANGUNAN UD. SUBUR
         BIGSALE MATERIAL BANGUNAN
      Diskon 5% Min. Pembelian Rp.500000
          ===========================  
    Daftar Oli dan harga : 
    A. Asbes Gelombang              = Rp.60000
    B. Cat Tembok Dulux 1Galon      = Rp.250000
    C. Cat Tembok Avian 1 Galon     = Rp.350000
    D. Aquaproof 5 Kg               = Rp.50000
    E. Seng 2mm                     = Rp.70000
    F. Spandeks 1mm                 = Rp.92000
    
 ==========================================
    """) 
    
    asbes     =60000
    Dulux     =250000
    Avian     =350000
    Aquaproof =50000
    Seng      =70000
    Spandeks  =92000
    
    print("Masukkan Jumblah pembelian material : ")
    print("==============================")
    
    a=int((asbes)*int(input("A. Asbes Gelombang           = ")))
    b=int((Dulux)*int(input("B. Cat Tembok Dulux 1Galon   = ")))
    c=int((Avian)*int(input("C. Cat Tembok Avian 1 Galon  = ")))
    d=int((Aquaproof)*int(input("D. Aquaproof 5 Kg            = ")))
    e=int((Seng)*int(input("E. Seng 2mm                  = ")))
    f=int((Spandeks)*int(input("E. Spandeks 1mm              = ")))
    
    total=a+b+c+d+e+f
    if int(total)>=500000:
        diskon=int(total*0.05)
        ppn=int(total*0.02)
        totalharga=int(total-diskon+ppn)
    else:
        diskon=(0)
        ppn=int(total*0.01)
        totalharga=int(total+ppn)
    print("")
        
    print("===========================")
    print("Total Rincian Transaksi")
    print("===========================")
    print("Total harga Pembelian material   = Rp.",total)
    print("SELAMAT anda dapat DISKON        = Rp.",diskon)
    print("PPN 2 %                          = Rp.",ppn)
    print("Total harga + Diskon + PPN       = Rp.",totalharga)    
    print("===========================")
    print("Jumblah uang yang harus dibayarkan = Rp.",totalharga)
    print("                                   -------------")
    print("             ===TERIMA KASIH ===")
            
    jwb = input(">>> Apakah Anda Ingin Order Kembali ? y/t : ")
    if jwb== "t" or jwb=="T":
        break