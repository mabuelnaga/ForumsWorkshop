from models import Member, Post
from stores import MemberStore, PostStore

member1 = Member('Adam', 1)
member2 = Member('Talia', 5)

post1 = Post('Hello there!', 'My name is Mohamed')
post2 = Post('Python', 'Python is cool!')

#Member Store
member_store = MemberStore()

member_store.add(member1)
member_store.add(member2)

print member_store.get_all()

post_store = PostStore()

post_store.add(post1)
post_store.add(post2)

print post_store.get_all()
