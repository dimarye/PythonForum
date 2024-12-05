import uuid

class User:
    def __init__(self, username, email):
        self.id = str(uuid.uuid4())
        self.username = username
        self.email = email

    def __str__(self):
        return f"User[ID: {self.id}, Username: {self.username}, Email: {self.email}]"

class Post:
    def __init__(self, title, content, author):
        self.id = str(uuid.uuid4())
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Post[ID: {self.id}, Title: {self.title}, Author: {self.author.username}]"

class Forum:
    def __init__(self):
        self.users = []
        self.posts = []

    def register_user(self, username, email):
        # Check for unique username and email
        if any(user.username == username for user in self.users):
            print(f"Error: Username '{username}' is already taken.")
            return None
        if any(user.email == email for user in self.users):
            print(f"Error: Email '{email}' is already registered.")
            return None
        user = User(username, email)
        self.users.append(user)
        print(f"User '{username}' registered successfully.")
        return user

    def create_post(self, title, content, author):
        if author not in self.users:
            print("Error: Author is not registered in the forum.")
            return None
        post = Post(title, content, author)
        self.posts.append(post)
        print(f"Post '{title}' created successfully.")
        return post

    def find_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        print(f"Error: User with username '{username}' not found.")
        return None

    def find_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        print(f"Error: User with email '{email}' not found.")
        return None

    def find_posts_by_author(self, author):
        if author not in self.users:
            print("Error: Author is not registered in the forum.")
            return []
        found_posts = [post for post in self.posts if post.author == author]
        if not found_posts:
            print(f"No posts found for author '{author.username}'.")
        return found_posts

# Example usage
forum = Forum()

# Register users
dmitrii = forum.register_user('Dmitrii123', 'dv@gmail.com')
tania = forum.register_user('Tania111', 'td@gmail.com')
forum.register_user('Dmitrii123', 'other_email@gmail.com')  # Should show an error

# Create posts
if dmitrii:
    forum.create_post("My first post", "Post content", dmitrii)
    forum.create_post("Second great post", "Post content", dmitrii)

if tania:
    forum.create_post("Tania's thoughts", "Another post content", tania)

# Find posts by author
if dmitrii:
    dmitrii_posts = forum.find_posts_by_author(dmitrii)
    for post in dmitrii_posts:
        print(post)

# Find user by email
user_email = 'dv@gmail.com'
found_user = forum.find_user_by_email(user_email)
if found_user:
    print(found_user)

# Find user by username
username = 'NonExistentUser'
forum.find_user_by_username(username)
