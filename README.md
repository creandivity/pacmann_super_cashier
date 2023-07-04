# Project Super Cashier
## 1. Latar Belakang
   Project ini bertujuan untuk membantu customer dalam melakukan transaksi, di mana user bisa menambahkan item, mengubah item (nama, qty, harga), menghapus, serta menampilkan jumlah belanjaan dan menghitungkan discountnya.
   
## 2. Requirement   
   - Procedure add_item : Menambahkan item, dengan parameter nama item (asumsi tidak ada nama kembar dalam 1 transaksi), qty, dan harga satuan.
   - Procedure update_item_name : Mengubah nama item, dengan parameter nama item lama dan nama item baru.
   - Procedure update_item_qty : Mengubah qty item, dengan parameter nama item dan qty baru.
   - Procedure update_item_price : Mengubah harga satuan item, dengan parameter nama item dan harga satuan baru.
   - Procedure delete_item : Menghapus 1 item dari list item, dengan parameter nama item.
   - Procedure reset_transaction : Menghapus semua item yang sudah pernah diinputkan sebelumnya.
   - Procedure check_order : Melakukan pengecekan terhadap order dan menampilkan list order.
   - Procedure total_price() : Menghitung total item yang dibeli dan discount yang diperoleh customer.
  
## 3. Alur Program/Flowchart dan Snippet Function
### Procedure Add Item
#### Snippet
```python
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
```
## 5. Hasil Test Case
