class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Inserted {data} at the back of the linked list.")

    def delete_node(self, key):
        current = self.head
        previous = None

        if current is None:
            print("The linked list is empty.")
            return

        if current.data == key:
            self.head = current.next
            print(f"Deleted {key} from the linked list.")
            return

        while current and current.data != key:
            previous = current
            current = current.next

        if current is None:
            print(f"Value {key} not found in the linked list.")
            return

        previous.next = current.next
        print(f"Deleted {key} from the linked list.")

    def delete_node_begin(self):
        if self.head is None:
            print("The linked list is empty.")
            return
        deleted_data = self.head.data
        self.head = self.head.next
        print(f"Deleted {deleted_data} from the beginning of the linked list.")

    def delete_node_end(self):
        if self.head is None:
            print("The linked list is empty.")
            return
        current = self.head
        previous = None

        while current.next:
            previous = current
            current = current.next

        if previous is None:
            self.head = None
        else:
            previous.next = None
        print(f"Deleted {current.data} from the end of the linked list.")

    def display(self):
        if self.head is None:
            print("The linked list is empty.")
            return
        current = self.head
        print("Linked list contents:", end=" ")
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()


def main():
    li = LinkedList()

    while True:
        print("\nMenu:")
        print("1. Append a number")
        print("2. Delete a number by value")
        print("3. Delete from beginning")
        print("4. Delete from end")
        print("5. Display linked list")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            num = int(input("Enter number to append: "))
            li.append(num)
        elif choice == "2":
            num = int(input("Enter number to delete by value: "))
            li.delete_node(num)
        elif choice == "3":
            li.delete_node_begin()
        elif choice == "4":
            li.delete_node_end()
        elif choice == "5":
            li.display()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
