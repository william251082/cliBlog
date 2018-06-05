from database import Database
from models.post import Post


Database.initialize()

blog = Blog(author="Jose",
            title="Another great post",
            description="Sample description"
            )

blog.new_post()
blog.save_to_mongo()
Blog.from_mongo()
blog.get_posts()

# post = Post("Post1 title", "Post1 content", "Post1 author")
# post2 = Post("Post2 title", "Post2 content", "Post2 author")
# post2.content = "Some different content"

# print(post.content)
# print(post2.content)