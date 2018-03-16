class MemberStore:

    members = []
    last_id = 1

    def get_all(self):
        # get all members
        return MemberStore.members

    def add(self, member):
        # append member
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_by_id(self, id):
        result = None
        all_members = self.get_all()
        for member in all_members:
            if member.id == id:
                result = member
                break
        return result

    def get_by_name(self, name):
        result = []
        all_members = self.get_all()
        for member in all_members:
            if member.name == name:
                result.append(member)
        return result

    def entity_exists(self, member):
        result = True
        if self.get_by_id(member.id) is None:
            result = False
        return result

    def delete(self, id):
        member = self.get_by_id(id)
        MemberStore.members.remove(member)

    def update(self, member):
        all_members = self.get_all()
        for index, current_member in enumerate(all_members):
            if current_member.id == member.id:
                all_members[index] = member



#####################################
class PostStore:

    posts = []

    def get_all(self):
        # get all members
        return PostStore.posts

    def add(self, post):
        # append member
        self.posts.append(post)
