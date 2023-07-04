# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 20:57:30 2023

@author: crean
"""

from cashier import Transaction

#Case 1 : menambahkan add item
trnsct123 = Transaction()
print("Case 1 : menambahkan item baru")
trnsct123.add_item("Ayam Goreng", 2, 20000)
trnsct123.add_item("Pasta Gigi", 3, 15000)
trnsct123.check_order()
print("")

#Mengupdate item name
#trnsct123.update_item_name("Mobil", "Mobil Toyota")
#trnsct123.check_order()

#Mengupdate item qty
#trnsct123.update_item_qty("Ayam Goreng", 4)
#trnsct123.check_order()

#Mengupdate item price
#trnsct123.update_item_price("Ayam Goreng", 40000)
#trnsct123.check_order()

#Case 2 : Menghapus pasta gigi
print("Case 2 : Menghapus item pasta gigi")
trnsct123.delete_item("Pasta Gigi")
trnsct123.check_order()
print("")

#Case 3 : Reset Transaction
print("Case 3 : Reset Transaction")
trnsct123.reset_transaction()
print("")

#Case 4
print("Case 4 : Mencoba total price")
trnsct123.add_item("Ayam Goreng", 2, 20000)
trnsct123.add_item("Pasta Gigi", 3, 15000)
trnsct123.add_item("Mainan Mobil", 1, 200000)
trnsct123.add_item("Mi Instan", 5, 3000)
trnsct123.check_order()
trnsct123.total_price()
print("")


