# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 10:38:36 2021

@author: imamc
"""

jwb = "y"
while jwb=="y" or jwb=="Y":
    print("""
          ===========================
            BENGKEL UD. MATAHARI
             BIGSALE OIL MOTOR
      Diskon 5% Min. Pembelian Rp.200000
          ===========================  
    Daftar Oli dan harga : 
    A. Duration SW20         = Rp.53000/liter
    B. Castrol Magnatec      = Rp.50000/liter
    C. Federal Supreme XX    = Rp.54000/liter
    D. Yamalube              = Rp.45000/liter
    E. Shell                 = Rp.46000/liter
 ==========================================
    """) 
    duration=53000
    castrol=50000
    federal=54000
    yamalube=45000 
    shell=46000
    
    print("Masukkan Jumblah pembelian oli : ")
    print("==============================")
    
    a=int((duration)*int(input("A. Duration SW20      = ")))
    b=int((castrol)*int(input("B. Castrol Magnatec   = ")))
    c=int((federal)*int(input("C. Federal Supreme XX = ")))
    d=int((yamalube)*int(input("D. Yamalube           = ")))
    e=int((shell)*int(input("E. Shell              = ")))
    
    total=a+b+c+d+e
    if int(total)>=200000:
        diskon=int(total*0.05)
        ppn=int(total*0.01)
        totalharga=int(total-diskon+ppn)
    else:
        diskon=(0)
        ppn=int(total*0.01)
        totalharga=int(total+ppn)
    print("")
        
    print("===========================")
    print("Total Rincian Transaksi")
    print("===========================")
    print("Total harga Pembelian oli    = Rp.",total)
    print("SELAMAT anda dapat DISKON    = Rp.",diskon)
    print("PPN 1 %                      = Rp.",ppn)
    print("Total harga + Diskon + PPN   = Rp.",totalharga)    
    print("===========================")
    print("Jumblah uang yang harus dibayarkan = Rp.",totalharga)
    print("                                   -------------")
    print("             ===TERIMA KASIH ===")
            
    jwb = input(">>> Apakah Anda Ingin Order Kembali ? y/t : ")
    if jwb== "t" or jwb=="T":
        break