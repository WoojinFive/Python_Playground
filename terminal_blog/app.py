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

from models.post import Post

post = Post("Post1 title", "Post1 content", "Post1 author")

post2 = Post("Post2 title", "Post2 content", "Post2 author")

print(post.content)

print(post2.content)
