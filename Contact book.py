class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone Number: {self.phone_number}, Email: {self.email}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return True
        return False

    def display_contacts(self):
        for contact in self.contacts:
            print(contact)

# Example usage
contact_book = ContactBook()

contact1 = Contact("RAM", "9732835100", "ram01@example.com")
contact2 = Contact("Sita", "9476450564", "sita02@example.com")

contact_book.add_contact(contact1)
contact_book.add_contact(contact2)

contact_book.display_contacts()

contact_book.delete_contact("Ram")

print("\nAfter deleting Rlice:\n")
contact_book.display_contacts()
