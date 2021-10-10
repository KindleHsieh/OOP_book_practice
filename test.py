class ContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

c1 = Contact("John A", "JJA.net")
c2 = Contact("John B", "JJB.net")
c3 = Contact("Jean A", "JeC.net")
print(
# [contact.name for contact in Contact.all_contacts.search('John')]
[contact.name for contact in Contact.all_contacts if 'John' in contact.name]
)

a = 1
print(
    dir(a)
)