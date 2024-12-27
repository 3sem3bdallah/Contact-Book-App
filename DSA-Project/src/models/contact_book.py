from .contact import Contact

class ContactBook:
    def __init__(self):
        self.head = None  # Head of the linked list

    def add_contact(self, name, phone_number, email):
        new_contact = Contact(name, phone_number, email)
        if not self.head:
            self.head = new_contact
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_contact

    def update_contact(self, name, new_phone_number, new_email):
        current = self.head
        while current:
            if current.name.lower() == name.lower():
                current.phone_number = new_phone_number
                current.email = new_email
                return True
            current = current.next
        return False

    def delete_contact(self, name):
        if not self.head:
            return False

        if self.head.name.lower() == name.lower():
            self.head = self.head.next
            return True

        current = self.head
        while current.next and current.next.name.lower() != name.lower():
            current = current.next

        if current.next:
            current.next = current.next.next
            return True
        return False

    def search_contact(self, keyword):
        current = self.head
        results = []
        while current:
            if keyword.lower() in current.name.lower() or keyword in current.phone_number:
                results.append(f"{current.name} | {current.phone_number} | {current.email}")
            current = current.next
        return results

    def sort_contacts_by_name(self):
        if not self.head or not self.head.next:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.name.lower() > current.next.name.lower():
                    # Swap data
                    current.name, current.next.name = current.next.name, current.name
                    current.phone_number, current.next.phone_number = current.next.phone_number, current.phone_number
                    current.email, current.next.email = current.next.email, current.email
                    swapped = True
                current = current.next

    def display_contacts(self):
        current = self.head
        contacts = []
        while current:
            contacts.append(f"{current.name} | {current.phone_number} | {current.email}")
            current = current.next
        return contacts