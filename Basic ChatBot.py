import tkinter as tk
from tkinter import messagebox

# Placeholder credentials (replace with your actual authentication logic)
valid_username = "Madalitso"
valid_password = "Azubi2023"

faqs = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! What can I help you with?",
    "how are you": "I'm just a bot, but thanks for asking!",
    "What is Azubi Africa?": "Azubi Africa is an online tech school",
    "Who are the partners of Azubi Africa?": "Azubi Africa has partnered with AWS, SAFARICOM",
}

def get_response(query):
    query = query.lower()
    response = "I'm sorry, I don't have an answer for that right now."
    for key in faqs:
        if query in key.lower():
            response = faqs[key]
            break
    return response

def send_message(event=None):
    user_query = entry_field.get()
    if user_query.lower() == 'exit':
        chat_history.insert(tk.END, "You: " + user_query + '\n')
        chat_history.insert(tk.END, "Chatbot: Goodbye!\n")
        entry_field.delete(0, tk.END)
    else:
        chat_history.insert(tk.END, "You: " + user_query + '\n')
        response = get_response(user_query)
        chat_history.insert(tk.END, "Chatbot: " + response + '\n')
        entry_field.delete(0, tk.END)

def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()
    
    if entered_username == valid_username and entered_password == valid_password:
        messagebox.showinfo("Login", "Login successful!")
        login_frame.pack_forget()  # Hide the login frame
        chat_frame.pack()  # Show the chat frame
    else:
        messagebox.showerror("Login Error", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Simple Chatbot")

# Create a frame to hold the login components
login_frame = tk.Frame(root)
login_frame.pack(padx=10, pady=10)

# Create and place widgets for login
tk.Label(login_frame, text="Username:").pack(pady=5)
username_entry = tk.Entry(login_frame)
username_entry.pack(pady=5)

tk.Label(login_frame, text="Password:").pack(pady=5)
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack(pady=5)

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.pack(pady=10)

# Create a frame to hold the chat history
chat_frame = tk.Frame(root)
# chat_frame.pack(padx=10, pady=10)  # Note: Pack this frame when login is successful

# Create a scrollbar for the chat history
scrollbar = tk.Scrollbar(chat_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a text widget for the chat history
chat_history = tk.Text(chat_frame, width=50, height=20, yscrollcommand=scrollbar.set)
chat_history.pack()

# Configure the scrollbar to work with the chat history
scrollbar.config(command=chat_history.yview)

# Create a frame to hold the input field and send button
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10)

# Create an entry field for user input
entry_field = tk.Entry(input_frame, width=40)
entry_field.bind("<Return>", send_message)
entry_field.pack(side=tk.LEFT, padx=5)

# Create a button to send the message
send_button = tk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=5)

# Start the GUI event loop
root.mainloop()
