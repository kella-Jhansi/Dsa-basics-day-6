class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def iae(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode

    def deletevalue(self, key):
        current = self.head
        if not current:
            print("Empty Linked List")
            return
        
        # If the head node is to be deleted
        if current.data == key:
            self.head = current.next
            print(f"Deleted node from beginning: {key}")
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            print(f"{key} not found in the linked list")
            return

        prev.next = current.next
        print(f"{key} deleted from the linked list")

    def display(self):
        current = self.head
        if not current:
            print("Linked list is empty")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()

while True:
    print("\nLinkedList - Insert at End / Delete / Display")
    print("1. Insert")
    print("2. Display")
    print("3. Delete")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        data = int(input("Enter a value to insert: "))
        ll.iae(data)

    elif choice == '2':
        ll.display()

    elif choice == '3':
        key = int(input("Enter the value you want to delete: "))
        ll.deletevalue(key)

    elif choice == '4':
        print("Exiting the operation...")
        break

    else:
        print("Enter only 1, 2, 3, or 4")
