# Çift yönlü düğüm yapısı
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Dairesel çift yönlü bağlı liste
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def ekle(self, data):
        yeni = DoublyNode(data)
        if not self.head:
            self.head = yeni
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            tail.next = yeni
            yeni.prev = tail
            yeni.next = self.head
            self.head.prev = yeni

    def ileri_yazdir(self, sayi=10):
        temp = self.head
        sayac = 0
        while temp and sayac < sayi:
            print(temp.data, end=" <-> ")
            temp = temp.next
            sayac += 1
        print("... (döngüsel)")

    def geri_yazdir(self, sayi=10):
        temp = self.head.prev if self.head else None
        sayac = 0
        while temp and sayac < sayi:
            print(temp.data, end=" <-> ")
            temp = temp.prev
            sayac += 1
        print("... (döngüsel)")

# Test
cdll = CircularDoublyLinkedList()
cdll.ekle(1)
cdll.ekle(2)
cdll.ekle(3)
cdll.ileri_yazdir()  # 1 <-> 2 <-> 3 <-> ...
cdll.geri_yazdir()   # 3 <-> 2 <-> 1 <-> ...
