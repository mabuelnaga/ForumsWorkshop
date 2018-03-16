class MemberStore:

    members = []

    def get_all(self):
        # get all members
        return MemberStore.members

    def add(self, member):
        # append member
        self.members.append(member)

class PostStore:

    posts = []

    def get_all(self):
        # get all members
        return PostStore.posts

    def add(self, post):
        # append member
        self.posts.append(post)
