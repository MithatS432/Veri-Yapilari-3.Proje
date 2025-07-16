# Node yapısı
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Tek yönlü bağlı liste
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def ekle(self, data):
        yeni_dugum = Node(data)
        if not self.head:
            self.head = yeni_dugum
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = yeni_dugum

    def sil(self, veri):
        temp = self.head
        prev = None
        while temp:
            if temp.data == veri:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return
            prev = temp
            temp = temp.next

    def yazdir(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Test
liste = SinglyLinkedList()
liste.ekle(10)
liste.ekle(20)
liste.ekle(30)
liste.yazdir()  # 10 -> 20 -> 30 -> None
liste.sil(20)
liste.yazdir()  # 10 -> 30 -> None
