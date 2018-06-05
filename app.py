from database import Database
from menu import Menu
from models.blog import Blog
from models.post import Post


Database.initialize()

menu = Menu()

menu.run_menu()

# blog = Blog(author="Jose",
#             title="Another great post",
#             description="Sample description")
#
# blog.new_post()
#
# blog.save_to_mongo()
#
# from_database = Blog.from_mongo(blog.id)
#
#
# print(blog.get_posts())    # Post.from_blog(id)
