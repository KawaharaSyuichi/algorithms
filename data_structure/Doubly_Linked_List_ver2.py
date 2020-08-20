class Cell:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.back = None


class LinkedList:
    def __init__(self):
        self.head = Cell(None)

    def insert(self, value):
        front = self.head
        rear = front.next

        while rear:
            front = rear
            rear = rear.next

        cell = Cell(value)
        cell.next = rear
        front.next = cell
        cell.back = front

    def delete(self, value):
        front = self.head
        rear = front.next

        while rear:
            if rear.value == value:
                break
            front = rear
            rear = rear.next

        if not rear:
            print('No Data')
            return

        front.next = rear.next
        rear.next.back = front

        rear = None

    def show(self):
        temp = self.head.next
        while temp.next != None:
            temp = temp.next

        while temp.back != None:
            print("{} ".format(temp.value), end='')
            temp = temp.back


n = int(input())
Q = LinkedList()

for _ in range(n):
    command, num = input().split()
    if command == 'insert':
        Q.insert(int(num))
    else:
        Q.delete(int(num))

Q.show()
