"""
PostBoard Application
---------------------
Features:
1. User Login (with 3 attempts)
2. Create Post (title, description, date)
3. View All Posts
4. Search Posts by Username
5. Exit
"""

import datetime

# Sample users (username: password)
users = {
    "admin": "1234",
    "user1": "pass1",
    "user2": "pass2"
}

# Store posts as list of dictionaries
posts = []

# ------------------- LOGIN FUNCTION -------------------
def login():
    """Login function with 3 attempts"""
    print("=== Login ===")
    for attempt in range(3):
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        if username in users and users[username] == password:
            print("✅ Login successful!")
            return username
        else:
            print("❌ Invalid credentials. Try again.")

    return None  # After 3 wrong attempts


# ------------------- CREATE POST -------------------
def create_post(username):
    """Create a new post"""
    title = input("Enter post title: ").strip()
    description = input("Enter post description: ").strip()
    date = datetime.date.today().strftime("%Y-%m-%d")

    if title and description:
        post = {
            "author": username,
            "title": title,
            "description": description,
            "date": date
        }
        posts.append(post)
        print("✅ Post created successfully!")
    else:
        print("⚠️ Title/Description cannot be blank.")


# ------------------- VIEW POSTS -------------------
def view_posts():
    """Display all posts"""
    print("\n=== All Posts ===")
    if not posts:
        print("No posts available yet.")
    else:
        for post in posts:
            print(f"Author: {post['author']} | Title: {post['title']} | Date: {post['date']}")
            print(f"Description: {post['description']}\n")


# ------------------- SEARCH POSTS -------------------
def search_posts():
    """Search posts by username"""
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


# ------------------- MAIN FUNCTION -------------------
def main():
    username = login()
    if not username:
        print("❌ Login failed. Exiting...")
        return

    while True:
        print("\n--- MENU ---")
        print("1. Create Post")
        print("2. View All Posts")
        print("3. Search Posts by Username")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            create_post(username)
        elif choice == "2":
            view_posts()
        elif choice == "3":
            search_posts()
        elif choice == "4":
            print("👋 Exiting... Thank you for using PostBoard!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")


# ------------------- RUN APP -------------------
if __name__ == "__main__":
    main()
