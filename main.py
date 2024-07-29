from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def Save():

    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    

    if len(website) != 0 and len(password) != 0:
        is_ok = messagebox.askokcancel(title= website, message=f"These are the details entered for {website}:\n Email: {email_username}\n Password: {password}\n Is it ok to save?")
        if is_ok:
            f = open("data.txt" , "a")
            f.write(website + ' | ' + email_username + ' | ' + password + "\n")
            f.close()
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
    else:
        messagebox.showwarning(message= "Please don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title('Password Manager')
window.config(padx=30, pady=30 )


canvas = Canvas(height = 200, width = 200)
logo_image = PhotoImage(file= "logo.png")
canvas.create_image(100,100, image = logo_image)
canvas.grid(column=1 ,row=0)

website_label = Label(text="Website: ", fg="#000000", font= ('Helvetica', 15))
website_label.grid(column=0, row=1)

email_username_label = Label(text = "Email/Username: ", fg="#000000", font= ('Helvetica', 15))
email_username_label.grid(column=0, row=2 )

Password_label = Label(text= "Password: ", fg="#000000", font=("Helvetica", 15))
Password_label.grid(column=0, row=3)


website_entry = Entry(width= 35)
website_entry.grid(column=1, row=1, columnspan= 2)
website_entry.focus()


email_username_entry = Entry(width = 35)
email_username_entry.grid(column=1, row=2, columnspan= 2)
email_username_entry.insert(0, "tomtomi@gmail.com")


password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)


add_button = Button(text="Add", width=35, command=Save)
add_button.grid(column=1, row=4, columnspan=2 )

window.mainloop()