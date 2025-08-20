import datetime

# Sample users (username: password)
users = {"admin": "1234", "user1": "pass1"}
# Store posts as list of dictionaries
posts = []

def login():
    print("=== Login ===")
    for i in range(3):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in users and users[username] == password:
            print("Login successful!")
            return username
        else:
            print("Invalid credentials. Try again.")
    return None

def create_post(username):
    title = input("Enter post title: ").strip()
    description = input("Enter post description: ").strip()
    date = datetime.date.today().strftime("%Y-%m-%d")
    if title and description:
        post = {"author": username, "title": title, "description": description, "date": date}
        posts.append(post)
        print("Post created successfully!")
    else:
        print("Title/Description cannot be blank.")

def view_posts():
    print("\n=== All Posts ===")
    for post in posts:
        print(f"Author: {post['author']} | Title: {post['title']} | Date: {post['date']}")
        print(f"Description: {post['description']}\n")

def search_posts():
    user = input("Enter username to search posts: ").strip()
    print(f"\n=== Posts by {user} ===")
    found = False
    for post in posts:
        if post["author"] == user:
            found = True
            print(f"Title: {post['title']} | Date: {post['date']}")
            print(f"Description: {post['description']}\n")
    if not found:
        print("No posts found for this user.")

def main():
    username = login()
    if not username:
        print("Login failed. Exiting...")
        return
    while True:
        print("\n1. Create Post")
        print("2. View All Posts")
        print("3. Search Posts by Username")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            create_post(username)
        elif choice == "2":
            view_posts()
        elif choice == "3":
            search_posts()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
