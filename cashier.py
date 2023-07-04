# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 20:45:27 2023

@author: crean
"""

import pandas as pd

class Transaction:
    def __init__(self):
        self.data_item = list()

    # Function add item untuk menambahkan item baru ke dalam list
    def add_item(self, nama, qty, harga):
        # nama = input('Masukan Nama Item: ')
        # qty = int(input('Masukan Qty: '))
        # harga = int(input('Masukan Harga: '))         
        for i in range(len(self.data_item)):
            #Lakukan pengecekan. Jika sebelumnya sudah ada, maka print error message
            if nama == self.data_item[i][0]:
                print('data item sudah ada, \
                      silahkan lakukan proses update jumlah')
        # Jika belum ada item tsb di list, maka append ke dalam list
        # di kolom terakhir, untuk menyimpan subtotal, dari perkalian qty * harga per unit
        self.data_item.append([nama, qty, harga, qty * harga])
        print('Penambahan data item berhasil')

    # function index_item untuk mencari index list berdasarkan nama item        
    def index_item(self, nama):
        for i in range(len(self.data_item)):
            if nama == self.data_item[i][0]:
                return i        
                
    # function update_item_name untuk mengupdate nama item di dalam list yang sudah ada
    def update_item_name(self, nama, nama_baru):
        try:
            # dengan memakai index_item untuk mencari isi dari list yg sama dengan nama
            self.data_item[self.index_item(nama)][0] = nama_baru
        except TypeError:
            print('data item tidak ada')
          
    # function update_item_qty untuk mengupdate qty di dalam list yang sudah ada berdasarkan nama item
    def update_item_qty(self, nama, qty_baru):
        try:
            # dengan memakai index_item untuk mencari isi dari list yg sama dengan nama
            # selain mengupdate qty, maka menghitung ulang kembali subtotal
            self.data_item[self.index_item(nama)][1] = qty_baru
            self.data_item[self.index_item(nama)][3] = qty_baru * self.data_item[self.index_item(nama)][2]
        except TypeError:
            print('data item tidak ada')            

    # function update_item_price untuk mengupdate qty di dalam list yang sudah ada berdasarkan nama item
    def update_item_price(self, nama, price_baru):
        try:
            # dengan memakai index_item untuk mencari isi dari list yg sama dengan nama
            # selain mengupdate harga satuan, maka menghitung ulang kembali subtotal
            self.data_item[self.index_item(nama)][2] = price_baru
            self.data_item[self.index_item(nama)][3] = price_baru * self.data_item[self.index_item(nama)][1]
        except TypeError:
            print('data item tidak ada')                        
            
    # function delete_item untuk menghapus item berdasarkan nama item
    def delete_item(self, nama):
        try:
            self.data_item.pop(self.index_item(nama))
        except TypeError:
            print('data item tidak ditemukan')
            
    # function reset_transaction untuk menghapus semua isi list
    def reset_transaction(self):
        self.data_item.clear()
        print('Selesai melakukan reset transaction')                    
    
    # function check order untuk menampilkan isi orderan
    def check_order(self):
        if(len(self.data_item) == 0):
            print('Tidak Ada Item dalam transaksi ini')
        else:
            empty_name = 0;
            for i in range(len(self.data_item)):
                if (self.data_item[i][0]==""):
                    empty_name = empty_name + 1
            if (empty_name == 0):
                print("Item yang dibeli adalah :")
                data = pd.DataFrame(self.data_item)
                data.columns = ['Nama Item', 'Jumlah Item', 'Harga/Item', 'Total Harga']
                print(data.to_markdown())
            else:
                print("Terdapat kesalahan item yang tidak memiliki nama")
            
    # function total_price untuk menghitung total belanjaan dan discount
    def total_price(self):
        subtotal = 0
        # untuk semua item di dalam list, subtotal ditambahkan dengan subtotal per item
        for i in range(len(self.data_item)):
            subtotal = subtotal + self.data_item[i][3]
        print("Total transaksi : ", subtotal)
        # hitung discount percent berdasarkan belanjaan total
        discount_pct = 0;
        discount_amount = 0;
        if subtotal > 500000:
            discount_pct = 10            
        elif subtotal > 300000:
            discount_pct = 8
        elif subtotal > 200000:
            discount_pct = 5
        else:
            discount_pct = 0
        
        #print total discount yang diperoleh
        if discount_pct == 0:
            print("Anda tidak mendapatkan discount untuk transaksi ini")
        else:
            discount_amount = discount_pct * subtotal / 100
            print("Anda mendapatkan discount sebesar ", discount_amount)
        print("Total belanja yang harus dibayarkan adalah ", (subtotal-discount_amount))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        