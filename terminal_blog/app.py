import pymongo

# uri = "mongodb://127.0.0.1/27017"
# client = pymongo.MongoClient(uri)
# database = client['fullstack']
# collection = database['students']
#
# # students = [{student['name']: student['mark']} for student in collection.find({}) if student['mark'] == 99.0]
# students = [student['mark'] for student in collection.find({})]
#
# print(students)
from database import Database
from models.post import Post

Database.initialize()

# post = Post(blog_id="123",
#             title="Another great post 2",
#             content="This is some sample content 2",
#             author="Jose")
#
# post.save_to_mongo()


# post = Post.from_mongo('bbfc7993d6654d3a9cc6354cc3dd9828')
# posts =[post for post in Post.from_blog('123')]

# for post in posts:
#     print(post)

# print(posts)

blog = Blog(author="Jose",
            title="Sample title",
            description="Sample discription")

blog.new_post()

blog.save_to_mongo()

Blog.from_mongo()

blog.get_posts() # Post.from_blog(id)