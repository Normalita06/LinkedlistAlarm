# APLIKASI DAILY ALARM
# NABILA PUTRI NORMALITA 2209116100

class Node:
    def __init__(self,nama, jam, menit):
        self.nama = nama
        self.jam = jam
        self.menit = menit
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def addFirst(self, nama, jam, menit):
        newalarm = Node(nama,jam,menit)
        if self.head is None:
            self.head = newalarm
            
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newalarm
    def hapus(self):
        if self.head is None:
            print("Linked list kosong")
        else :
            self.head = self.head.next
            
    def cari_alarm(self, nama):
        current = self.head
        while current is not None:
            if current.nama == nama:
                return current
            current = current.next
        return None    
    
    def hapus_alarm(self, nama):
        current = self.head
        if current and current.nama == nama:
            self.head = current.next
            current = None
            print("Alarm berhasil dihapus!")
            return
        prev = None
        while current and current.nama != nama:
            prev = current
            current = current.next
        if current is None:
            print("Alarm tersebut tidak ditemukan!")
            return
        prev.next = current.next
        current = None
        print("Alarm berhasil dihapus!")
  
    def printlist(self):
        if self.head is None:
            print("Linked List Kosong")
        else:
            n = self.head
            print("Alarm yang tersedia")
            print("--------------------")
            while n is not None:
                print("Alarm ",n.nama ,n.jam,":",n.menit)
                n = n.next
                
linkedlist = LinkedList()
def menu():
    while True:
        
        print("""
              Menu Aplikasi Daily Alarm
            -------------------------------
            |   1. Pasang Alarm           |  
            |   2. Alarm Yang Terpasang   |
            |   3. Hapus Alarm            | 
            |   4. Exit                   | 
            ------------------------------
        """)
        pilih = int(input("Masukkan pilihan anda : "))
        if pilih == 1 :
            input1 = input("Masuk nama alarm : ")
            input2 = (input("Masukan Jam :"))
            input3 = (input("Masukan Menit :"))
            linkedlist.addFirst(input1,input2,input3)
            print("Alarm berhasil ditambahkan!")
        elif pilih == 2:
            linkedlist.printlist()
        elif pilih == 3:
            linkedlist.printlist()
            nama1 = input("Masukan nama alarm : ")
            cc = linkedlist.cari_alarm(nama1)
            if cc:
                linkedlist.hapus_alarm(nama1)
            else :
                print("Alarm tidak ditemukan")
        elif pilih == 4:
            break
                
menu()