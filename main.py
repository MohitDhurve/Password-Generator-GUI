import random
import string
from tkinter import *
from tkinter import messagebox


# Function to generate the password
def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected")

    # Ensure the password contains at least one character of each selected type
    password = [
        random.choice(string.ascii_uppercase) if use_uppercase else '',
        random.choice(string.ascii_lowercase) if use_lowercase else '',
        random.choice(string.digits) if use_digits else '',
        random.choice(string.punctuation) if use_special else ''
    ]

    # Fill the rest of the password length
    password += [random.choice(characters) for _ in range(length - len(password))]

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    return ''.join(password)


# Function to handle the generation process when the button is clicked
def on_generate():
    try:
        # Get the password length
        length = entry_length.get().strip()
        if not length:
            raise ValueError("Please enter the password length.")

        length = int(length)
        use_uppercase = var_uppercase.get()
        use_lowercase = var_lowercase.get()
        use_digits = var_digits.get()
        use_special = var_special.get()

        if length < 4:
            raise ValueError("Password length must be at least 4.")

        if not (use_uppercase or use_lowercase or use_digits or use_special):
            raise ValueError("Please select at least one character type.")

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        entry_result.delete("1.0", END)
        entry_result.insert(END, password)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", "An unexpected error occurred. Please try again later.")


if __name__ == "__main__":
    root = Tk()
    root.title("Password Generator")
    photo = PhotoImage(file='lock.png')
    root.iconphoto(False, photo)

    welcome_label = Label(root, text="Welcome to Password Generator!", font=('Helvetica', 14, 'bold'))
    welcome_label.pack(pady=10)

    frame = Frame(root)
    frame.pack(padx=10, pady=10)

    Label(frame, text="Enter the length of the password:").grid(row=0, column=0, sticky=W)
    entry_length = Entry(frame)
    entry_length.grid(row=0, column=1)

    var_uppercase = BooleanVar(value=True)
    Checkbutton(frame, text="Include uppercase letters", variable=var_uppercase).grid(row=1, columnspan=2, sticky=W)

    var_lowercase = BooleanVar(value=True)
    Checkbutton(frame, text="Include lowercase letters", variable=var_lowercase).grid(row=2, columnspan=2, sticky=W)

    var_digits = BooleanVar(value=True)
    Checkbutton(frame, text="Include digits", variable=var_digits).grid(row=3, columnspan=2, sticky=W)

    var_special = BooleanVar(value=True)
    Checkbutton(frame, text="Include special characters", variable=var_special).grid(row=4, columnspan=2, sticky=W)

    Button(frame, text="Generate Password", command=on_generate).grid(row=5, columnspan=2, pady=10)

    Label(frame, text="Generated Password:").grid(row=6, column=0, sticky=W)
    entry_result = Text(frame, height=1, wrap=NONE)
    entry_result.grid(row=6, column=1, sticky="ew")

    frame.grid_columnconfigure(1, weight=1)

    root.mainloop()
