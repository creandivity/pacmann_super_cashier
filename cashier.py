# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 20:45:27 2023

@author: crean
"""

import pandas as pd

class Transaction:
    def __init__(self):
        self.data_item = list()

    def add_item(self, nama, qty, harga):
        # nama = input('Masukan Nama Item: ')
        # qty = int(input('Masukan Qty: '))
        # harga = int(input('Masukan Harga: '))        
        for i in range(len(self.data_item)):
            if nama == self.data_item[i][0]:
                print('data item sudah ada, \
                      silahkan lakukan proses update jumlah')
        self.data_item.append([nama, qty, harga, qty * harga])
        print('Penambahan data item berhasil')
                
    def update_item_name(self, nama, nama_baru):
        try:
            self.data_item[self.index_item(nama)][0] = nama_baru
        except TypeError:
            print('data item tidak ada')
          
    def update_item_qty(self, nama, qty_baru):
        try:
            self.data_item[self.index_item(nama)][1] = qty_baru
            self.data_item[self.index_item(nama)][3] = qty_baru * self.data_item[self.index_item(nama)][2]
        except TypeError:
            print('data item tidak ada')            

    def update_item_price(self, nama, price_baru):
        try:
            self.data_item[self.index_item(nama)][2] = price_baru
            self.data_item[self.index_item(nama)][3] = price_baru * self.data_item[self.index_item(nama)][1]
        except TypeError:
            print('data item tidak ada')                        
            
    def delete_item(self, nama):
        try:
            self.data_item.pop(self.index_item(nama))
        except TypeError:
            print('data item tidak ditemukan')
            
    def reset_transaction(self):
        self.data_item.clear()
        print('Selesai melakukan reset transaction')            
            
    def index_item(self, nama):
        for i in range(len(self.data_item)):
            if nama == self.data_item[i][0]:
                return i
    
    def check_order(self):
        if(len(self.data_item) == 0):
            print('Tidak Ada Item dalam transaksi ini')
        else:
            print("Item yang dibeli adalah :")
            data = pd.DataFrame(self.data_item)
            data.columns = ['Nama Item', 'Jumlah Item', 'Harga/Item', 'Total Harga']
            print(data.to_markdown())
            
    def total_price(self):
        subtotal = 0
        for i in range(len(self.data_item)):
            subtotal = subtotal + self.data_item[i][3]
        print("Total transaksi : ", subtotal)
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
        
        if discount_pct == 0:
            print("Anda tidak mendapatkan discount untuk transaksi ini")
        else:
            discount_amount = discount_pct * subtotal / 100
            print("Anda mendapatkan discount sebesar ", discount_amount)
        print("Total belanja yang harus dibayarkan adalah ", (subtotal-discount_amount))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        