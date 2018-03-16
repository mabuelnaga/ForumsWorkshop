class Member:
    def __init__(self, name, age):
        self.id = 0
        self.name = name
        self.age = age

    def __str__(self):
        return "Name: {}, Age: {}".format(self.name, self.age)


class Post:
    def __init__(self, subject, content):
        self.id = 0
        self.subject = subject
        self.content = content

    def __str__(self):
        return "Subject: {}, Content: {}".format(self.subject,\
         self.content)
