import os
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from Dispatcher import Dispatcher
from Client import Client
from Contract import Contract
from decimal import Decimal
from datetime import datetime
from tkinter import PhotoImage

user_window = None
client_created = False
dispatcher_created = False

def check_user_creation():
    global client_created
    global dispatcher_created

    # if the file is not empty
    with open("files/client_firm.txt", "r") as file:
        content = file.read()
        if content.strip():
            client_created = True

    # if the file is not empty
    with open("files/dispatcher.txt", "r") as file:
        content = file.read()
        if content.strip():
            dispatcher_created = True

# constructor Tk()
root = tk.Tk()
root.geometry("750x650")
#root.iconbitmap("img/main.ico")
root.title("Rail Cargo Solutions")
root.resizable(width=False, height=False)
bg_image = PhotoImage(file="img/RailCargoSol.png")
canvas = tk.Canvas(root, width=750, height=650)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

# for choosing registration
registration_type = StringVar()

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def user_window_init(user_type):
    global user_window
    global client_created
    global dispatcher_created

    if user_window is not None:
        user_window.destroy()

    user_window = Toplevel(root)
    user_window.title(f"{user_type}")
    user_window.resizable(width=False, height=False)
    user_window.geometry("750x650")
    user_window.transient(root)  # Set it to be a child of the main window

    # Load the image and keep a reference to it
    bg_img = PhotoImage(file="img/user_window.png")
    bg_label = Label(user_window, image=bg_img)
    bg_label.image = bg_img  # Keep a reference to the image
    bg_label.place(relwidth=1, relheight=1)

    center_window(user_window)

    data_text = Text(user_window, wrap=tk.WORD, height=30, width=50)
    data_text.pack()
    data_text.place(x=300, y=100)

    check_user_creation()


    def view_contract():
        with open("files/contract.txt", "r") as file:
            if file.tell() == 0:
                messagebox.showerror("Empty File", "The file is empty.")
            else:
                contracts = file.read()
                data_text.delete(1.0, tk.END)
                data_text.insert(tk.INSERT, contracts)

    def view_address():
        with open("files/addresses.txt", "r") as file:
            if file.tell() == 0:
                messagebox.showerror("Empty File", "The file is empty.")
            else:
                addresses = file.read()
                data_text.delete(1.0, tk.END)
                data_text.insert(tk.INSERT, addresses)

    def view_firms():
        with open("files/client_firm.txt", "r") as file:
            if file.tell() == 0:
                messagebox.showerror("Empty File", "The file is empty.")
            else:
                clients = file.read()
                data_text.delete(1.0, tk.END)
                data_text.insert(tk.INSERT, clients)

    def max_time():
        with open("files/max_delivery_time.txt", "r") as file:
            contracts = file.read()
            data_text.delete(1.0, tk.END)
            data_text.insert(tk.INSERT, contracts)

    def arrival_st():
        with open("files/pop_arrSt.txt", "r") as file:
            contracts = file.read()
            data_text.delete(1.0, tk.END)
            data_text.insert(tk.INSERT, contracts)

    def avg_time():
        with open("files/avg_time.txt", "r") as file:
            contracts = file.read()
            data_text.delete(1.0, tk.END)
            data_text.insert(tk.INSERT, contracts)

    def clear_all_files():
        file_paths = ["files/client_firm.txt", "files/dispatcher.txt", "files/contract.txt", "files/addresses.txt",
                      "files/max_delivery_time.txt", "files/pop_arrSt.txt", "files/avg_time.txt"]

        for file_path in file_paths:
            try:
                with open(file_path, "w") as file:
                    file.truncate(0)
            except FileNotFoundError:
                pass

        global client_created, dispatcher_created
        client_created = False
        dispatcher_created = False
        messagebox.showinfo("Files Cleared", "All existing files have been cleared.")
        data_text.delete(1.0, tk.END)

    if user_type == "Client":
        new_client_btn = Button(user_window, text="Create new client", command=client_reg, font=("Cooper Black", 12))
        new_contract_btn = Button(user_window, text="New contract", command=create_contract, font=("Cooper Black", 11))
        view_contract_btn = Button(user_window, text="List of contracts", command=view_contract, font=("Cooper Black", 11))
        view_address_btn = Button(user_window, text="List of delivery addresses", command=view_address, font=("Cooper Black", 11))
        view_firms_btn = Button(user_window, text="List of client's firms", command=view_firms, font=("Cooper Black", 11))
        clear_all_btn = Button(user_window, text="Clear all files", command=clear_all_files, font=("Cooper Black", 11))

        new_client_btn.pack()
        new_contract_btn.pack()
        view_contract_btn.pack()
        view_address_btn.pack()
        view_firms_btn.pack()
        clear_all_btn.pack()

        new_client_btn.place(x=50, y=100)
        new_contract_btn.place(x=10, y=160)

        view_contract_btn.place(x=10, y=200)
        view_address_btn.place(x=10, y=240)
        view_firms_btn.place(x=10, y=280)
        clear_all_btn.place(x=300, y=600)

        if not client_created:
            new_contract_btn.config(state=tk.DISABLED)
            view_contract_btn.config(state=tk.DISABLED)
            view_address_btn.config(state=tk.DISABLED)
            view_firms_btn.config(state=tk.DISABLED)
            clear_all_btn.config(state=tk.DISABLED)
        else:
            new_contract_btn.config(state=tk.NORMAL)
            view_contract_btn.config(state=tk.NORMAL)
            view_address_btn.config(state=tk.NORMAL)
            view_firms_btn.config(state=tk.NORMAL)
            clear_all_btn.config(state=tk.NORMAL)

        client_label = tk.Label(user_window, text="You are currently signed as a client:", font=("Cooper Black", 12))
        client_label.pack()
        client_label.place(x=200, y=20)

    elif user_type == "Dispatcher":
        new_dispatcher_btn = Button(user_window, text="Create new dispatcher", command=dispatcher_reg, font=("Cooper Black", 12))
        new_contract_btn = Button(user_window, text="New contract", command=create_contract, font=("Cooper Black", 11))
        view_contract_btn = Button(user_window, text="List of contracts", command=view_contract, font=("Cooper Black", 11))
        view_address_btn = Button(user_window, text="List of addresses", command=view_address, font=("Cooper Black", 11))
        view_firms_btn = Button(user_window, text="List of client's firms", command=view_firms, font=("Cooper Black", 11))
        clear_all_btn = Button(user_window, text="Clear all files", command=clear_all_files, font=("Cooper Black", 11))

        max_btn = Button(user_window, text="Max delivery time",command=max_delivery_time, font=("Cooper Black", 11))
        view_max_btn = Button(user_window, text="View", command=max_time,font=("Cooper Black", 11))
        arr_btn = Button(user_window, text="The most popular station",command=most_popular_destination, font=("Cooper Black", 11))
        view_arr_btn = Button(user_window, text="View", command=arrival_st,font=("Cooper Black", 11))
        avg_btn = Button(user_window, text="Average delivery time", command=calculate_avg_time, font=("Cooper Black", 11))
        view_avg_btn = Button(user_window, text="View", command=avg_time ,font=("Cooper Black", 11))

        new_dispatcher_btn.pack()
        new_contract_btn.pack()
        view_contract_btn.pack()
        view_address_btn.pack()
        view_firms_btn.pack()

        max_btn.pack()
        view_max_btn.pack()
        arr_btn.pack()
        view_arr_btn.pack()
        avg_btn.pack()
        view_avg_btn.pack()
        clear_all_btn.pack()

        new_dispatcher_btn.place(x=50, y=100)
        new_contract_btn.place(x=10, y=160)

        view_contract_btn.place(x=10, y=200)
        view_address_btn.place(x=10, y=240)
        view_firms_btn.place(x=10, y=280)

        max_btn.place(x=5, y=320)
        view_max_btn.place(x=230, y=320)
        arr_btn.place(x=1, y=360)
        view_arr_btn.place(x=230, y=360)
        avg_btn.place(x=5, y=400)
        view_avg_btn.place(x=230, y=400)
        clear_all_btn.place(x=300, y=600)

        if not dispatcher_created:
            new_contract_btn.config(state=tk.DISABLED)
            view_contract_btn.config(state=tk.DISABLED)
            view_address_btn.config(state=tk.DISABLED)
            view_firms_btn.config(state=tk.DISABLED)
            max_btn.config(state=tk.DISABLED)
            view_max_btn.config(state=tk.DISABLED)
            arr_btn.config(state=tk.DISABLED)
            view_arr_btn.config(state=tk.DISABLED)
            avg_btn.config(state=tk.DISABLED)
            view_avg_btn.config(state=tk.DISABLED)
            clear_all_btn.config(state=tk.DISABLED)
        else:
            new_contract_btn.config(state=tk.NORMAL)
            view_contract_btn.config(state=tk.NORMAL)
            view_address_btn.config(state=tk.NORMAL)
            view_firms_btn.config(state=tk.NORMAL)
            max_btn.config(state=tk.NORMAL)
            view_max_btn.config(state=tk.NORMAL)
            arr_btn.config(state=tk.NORMAL)
            view_arr_btn.config(state=tk.NORMAL)
            avg_btn.config(state=tk.NORMAL)
            view_avg_btn.config(state=tk.NORMAL)
            clear_all_btn.config(state=tk.NORMAL)

        dispatcher_label = tk.Label(user_window, text="You are currently signed as a dispatcher:",
                                    font=("Cooper Black", 12))
        dispatcher_label.pack()
        dispatcher_label.place(x=200, y=20)


def create_contract():
    contract_window = Toplevel(root)
    contract_window.title("Create new contract")
    contract_window.resizable(width=False, height=False)
    contract_window.geometry("400x300")
    center_window(contract_window)

    def save_contract():
        contract_id = id_entry.get()
        dep_st = dep_entry.get()
        arr_st = arr_entry.get()
        insurance_sum = insurance_entry.get()
        cargo_type = type_entry.get()
        delivery_time = time_entry.get()
        weight = weight_entry.get()
        date = date_entry.get()
        cost = cost_entry.get()

        if not all([contract_id, dep_st, arr_st, insurance_sum, cargo_type, delivery_time, weight, date, cost]):
            messagebox.showerror("Error", "All fields must be filled.")
            contract_window.destroy()
            return

        try:
            contract_id = int(contract_id)
            insurance_sum = Decimal(insurance_sum)
            delivery_time = datetime.strptime(delivery_time, "%H:%M").time()
            weight = float(weight)
            date = datetime.strptime(date, "%Y-%m-%d").date()
            cost = Decimal(cost)
        except ValueError:
            messagebox.showerror("Error", "Invalid data type for one or more fields.")
            contract_window.destroy()
            return

        contract = Contract(contract_id, dep_st, arr_st, insurance_sum, cargo_type, delivery_time, weight, date, cost)
        save_contract_to_file(contract)

        messagebox.showinfo("Success", "Contract successfully created.")
        contract_window.destroy()
        user_window.deiconify()

    # labels & entries
    id_lb = Label(contract_window, text="Contract ID:")
    id_lb.pack()
    id_lb.place(x=10, y=10)
    id_entry = Entry(contract_window)
    id_entry.pack()
    id_entry.place(x=190, y=10)

    dep_lb = Label(contract_window, text="Departure station:")
    dep_lb.pack()
    dep_lb.place(x=10, y=40)
    dep_entry = Entry(contract_window)
    dep_entry.pack()
    dep_entry.place(x=190, y=40)

    arr_lb = Label(contract_window, text="Arrival station:")
    arr_lb.pack()
    arr_lb.place(x=10, y=70)
    arr_entry = Entry(contract_window)
    arr_entry.pack()
    arr_entry.place(x=190, y=70)

    type_lb = Label(contract_window, text="Cargo type:")
    type_lb.pack()
    type_lb.place(x=10, y=100)
    type_entry = Entry(contract_window)
    type_entry.pack()
    type_entry.place(x=190, y=100)

    insurance_lb = Label(contract_window, text="Insurance sum:")
    insurance_lb.pack()
    insurance_lb.place(x=10, y=130)
    val_lb = Label(contract_window, text="UAH")
    val_lb.pack()
    val_lb.place(x=320, y=130)
    insurance_entry = Entry(contract_window)
    insurance_entry.pack()
    insurance_entry.place(x=190, y=130)

    time_lb = Label(contract_window, text="Delivery time:")
    time_lb.pack()
    time_lb.place(x=10, y=160)
    t_lb = Label(contract_window, text="(D:H)")
    t_lb.pack()
    t_lb.place(x=320, y=160)
    time_entry = Entry(contract_window)
    time_entry.pack()
    time_entry.place(x=190, y=160)

    weight_lb = Label(contract_window, text="Weight:")
    weight_lb.pack()
    weight_lb.place(x=10, y=190)
    w_lb = Label(contract_window, text="KG")
    w_lb.pack()
    w_lb.place(x=320, y=190)
    weight_entry = Entry(contract_window)
    weight_entry.pack()
    weight_entry.place(x=190, y=190)

    date_lb = Label(contract_window, text="Contract date:")
    date_lb.pack()
    date_lb.place(x=10, y=220)
    d_lb = Label(contract_window, text="(Y-M-D)")
    d_lb.pack()
    d_lb.place(x=320, y=220)
    date_entry = Entry(contract_window)
    date_entry.pack()
    date_entry.place(x=190, y=220)

    cost_lb = Label(contract_window, text="Cost:")
    cost_lb.pack()
    cost_lb.place(x=10, y=250)
    val_lb = Label(contract_window, text="UAH")
    val_lb.pack()
    val_lb.place(x=320, y=250)
    cost_entry = Entry(contract_window)
    cost_entry.pack()
    cost_entry.place(x=190, y=250)

    create_contract_btn = Button(contract_window, text="Save contract", command=save_contract)
    create_contract_btn.pack()
    create_contract_btn.place(x=150, y=270)

def save_contract_to_file(contract):
    with open("files/contract.txt", "a") as file:
        file.write(f"\nContract ID: {contract.contract_id}\n")
        file.write(f"Departure station: {contract.dep_st}\n")
        file.write(f"Arrival station: {contract.arr_st}\n")
        file.write(f"Insurance sum: {contract.insurance_sum}\n")
        file.write(f"Cargo type: {contract.cargo_type}\n")
        file.write(f"Delivery time: {contract.delivery_time}\n")
        file.write(f"Weight: {contract.weight}\n")
        file.write(f"Date of conclusion: {contract.date}\n")
        file.write(f"Cost: {contract.cost}\n")

    with open("files/addresses.txt", "a") as arrivalSt_file:
        arrivalSt_file.write(f"Contract ID: {contract.contract_id}\n"
                        f"Arrival Station: {contract.arr_st}\n\n")

def client_reg():
    client_reg_window = tk.Toplevel(root)
    client_reg_window.title("Client registration")
    client_reg_window.resizable(width=False, height=False)
    client_reg_window.geometry("400x300")
    center_window(client_reg_window)

    firm_name_label = tk.Label(client_reg_window, text="Firm name:")
    firm_name_label.pack()
    firm_name_label.place(x=10, y=10)

    firm_name_entry = tk.Entry(client_reg_window)
    firm_name_entry.pack()
    firm_name_entry.place(x=150, y=10)

    address_label = tk.Label(client_reg_window, text="Address:")
    address_label.pack()
    address_label.place(x=10, y=40)

    address_entry = tk.Entry(client_reg_window)
    address_entry.pack()
    address_entry.place(x=150, y=40)

    phone_number_label = tk.Label(client_reg_window, text="Phone number:")
    phone_number_label.pack()
    phone_number_label.place(x=10, y=70)

    phone_number_entry = tk.Entry(client_reg_window)
    phone_number_entry.pack()
    phone_number_entry.place(x=150, y=70)

    pib_label = tk.Label(client_reg_window, text="PIB:")
    pib_label.pack()
    pib_label.place(x=10, y=100)

    pib_entry = tk.Entry(client_reg_window)
    pib_entry.pack()
    pib_entry.place(x=150, y=100)

    def save_client_reg():
        firm_name = firm_name_entry.get()
        address = address_entry.get()
        phone_number = phone_number_entry.get()
        pib = pib_entry.get()

        if not (firm_name and address and phone_number and pib):
            messagebox.showerror("Error", "All fields must be filled")
            return

        try:
            if not isinstance(firm_name, str) or not isinstance(address, str):
                raise ValueError("Firm name and address must be strings")

            if not phone_number.isdigit() or len(phone_number) != 10:
                raise ValueError("Phone number must be a 10-digit numeric value")

            client = Client(firm_name, address, phone_number, pib)

            with open("files/client_firm.txt", "a") as file:
                file.write("Firm name: {}\n".format(firm_name))
                file.write("Address: {}\n".format(address))
                file.write("Phone number: {}\n".format(phone_number))
                file.write("PIB: {}\n".format(pib))
                file.write("\n")

            messagebox.showinfo("Success", "Client successfully created.")
        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid data: {str(ve)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    sv_btn = tk.Button(client_reg_window, text="Write to file", command=save_client_reg)
    sv_btn.pack()
    sv_btn.place(relx=0.5, rely=0.8, anchor='s')

def dispatcher_reg():
    dispatcher_reg_window = tk.Toplevel(root)
    dispatcher_reg_window.title("Dispatcher registration")
    dispatcher_reg_window.resizable(width=False, height=False)
    dispatcher_reg_window.geometry("400x300")
    center_window(dispatcher_reg_window)

    firm_name_label = tk.Label(dispatcher_reg_window, text="Firm name:")
    firm_name_label.pack()
    firm_name_label.place(x=10, y=10)

    firm_name_entry = tk.Entry(dispatcher_reg_window)
    firm_name_entry.pack()
    firm_name_entry.place(x=150, y=10)

    address_label = tk.Label(dispatcher_reg_window, text="Address:")
    address_label.pack()
    address_label.place(x=10, y=40)

    address_entry = tk.Entry(dispatcher_reg_window)
    address_entry.pack()
    address_entry.place(x=150, y=40)

    phone_number_label = tk.Label(dispatcher_reg_window, text="Phone number:")
    phone_number_label.pack()
    phone_number_label.place(x=10, y=70)

    phone_number_entry = tk.Entry(dispatcher_reg_window)
    phone_number_entry.pack()
    phone_number_entry.place(x=150, y=70)

    pib_label = tk.Label(dispatcher_reg_window, text="PIB:")
    pib_label.pack()
    pib_label.place(x=10, y=100)

    pib_entry = tk.Entry(dispatcher_reg_window)
    pib_entry.pack()
    pib_entry.place(x=150, y=100)

    experience_label = tk.Label(dispatcher_reg_window, text="Work experience:")
    experience_label.pack()
    experience_label.place(x=10, y=130)

    experience_entry = tk.Entry(dispatcher_reg_window)
    experience_entry.pack()
    experience_entry.place(x=150, y=130)

    def save_dispatcher_reg():
        firm_name = firm_name_entry.get()
        address = address_entry.get()
        phone_number = phone_number_entry.get()
        pib = pib_entry.get()
        experience = experience_entry.get()

        if not (firm_name and address and phone_number and pib and experience):
            messagebox.showerror("Error", "All fields must be filled")
            return

        try:
            if not isinstance(firm_name, str) or not isinstance(address, str):
                raise ValueError("Firm name and address must be strings")

            if not phone_number.isdigit() or len(phone_number) != 10:
                raise ValueError("Phone number must be a 10-digit numeric value")

            experience = float(experience)  # Convert to float
            if not isinstance(experience, float):
                raise ValueError("Work experience must be a float")

            dispatcher = Dispatcher(firm_name, address, phone_number, pib, experience)

            with open("files/dispatcher.txt", "a") as file:
                file.write("Firm name: {}\n".format(firm_name))
                file.write("Address: {}\n".format(address))
                file.write("Phone number: {}\n".format(phone_number))
                file.write("PIB: {}\n".format(pib))
                file.write("Work experience: {}\n".format(experience))
                file.write("\n")

            messagebox.showinfo("Success", "Dispatcher successfully created.")
            dispatcher_reg_window.destroy()
        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid data: {str(ve)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    save_btn = tk.Button(dispatcher_reg_window, text="Write to file", command=save_dispatcher_reg)
    save_btn.pack()
    save_btn.place(relx=0.5, rely=0.8, anchor='s')


def max_delivery_time():
    max_delivery = 0
    id = None

    with open("files/contract.txt", "r") as file:
        lines = file.readlines()
        contract_info = {}
        current_id = None

        for line in lines:
            if line.startswith("Contract ID:"):
                if current_id:
                    delivery_time = int(contract_info.get("Delivery time", 0))
                    if delivery_time > max_delivery:
                        max_delivery = delivery_time
                        id = current_id

                current_id = line.strip().replace("Contract ID: ", "")
                contract_info = {}

            if ":" in line:
                key, value = map(str.strip, line.split(":", 1))
                contract_info[key] = value

        if current_id:
            delivery_time = int(contract_info.get("Delivery time", 0))
            if delivery_time > max_delivery:
                max_delivery = delivery_time
                id = current_id

    if id:
        with open("files/max_delivery_time.txt", "w") as output_file:
            output_file.write(f"Contract ID: {id}\n")
            output_file.write(f"Max delivery time: {max_delivery} hours\n")

        messagebox.showinfo("Success", "Max delivery time saved in file")
    else:
        messagebox.showerror("No contracts", "No contracts found in file.")


def most_popular_destination():
    destination_counts = {}
    most_popular_destination = None
    max_count = 0

    with open("files/contract.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            if line.startswith("Arrival station:"):
                destination = line.strip().replace("Arrival station: ", "")
                destination_counts[destination] = destination_counts.get(destination, 0) + 1

                if destination_counts[destination] > max_count:
                    max_count = destination_counts[destination]
                    most_popular_destination = destination

    if most_popular_destination:
        with open("files/pop_arrSt.txt", "w") as output_file:
            output_file.write(f"Most popular arrival station: {most_popular_destination}\n")
            output_file.write(f"Number of contracts: {max_count}\n")

        messagebox.showinfo("Success", "Most popular destination saved in file")
    else:
        messagebox.showerror("No contracts", "No contracts with destination found in the file.")

def calculate_avg_time():
    total_delivery_time = 0
    contract_count = 0

    with open("files/contract.txt", "r") as file:
        lines = file.readlines()
        contract_info = {}
        id = None

        for line in lines:
            if line.startswith("Contract ID:"):
                if id:
                    delivery_time = int(contract_info.get("Delivery time", 0))
                    total_delivery_time += delivery_time
                    contract_count += 1

                id = line.strip().replace("Contract ID: ", "")
                contract_info = {}

            if ":" in line:
                key, value = map(str.strip, line.split(":", 1))
                contract_info[key] = value
        if id:
            delivery_time = int(contract_info.get("Delivery time", 0))
            total_delivery_time += delivery_time
            contract_count += 1

    if contract_count > 0:
        average_delivery_time = total_delivery_time / contract_count
        messagebox.showinfo("Average delivery time", f"Average delivery time: {average_delivery_time} hours")

        with open("files/avg_time.txt", "w") as output_file:
            output_file.write(f"Average delivery time: {average_delivery_time} hours")

    else:
        messagebox.showerror("No contracts", "No contracts found in the file.")


def register_client():
    user_window_init("Client")

def register_dispatcher():
    user_window_init("Dispatcher")

def reg_type(*args):
    selected_role = registration_type.get()
    if selected_role == "Client":
        register_btn.config(command=register_client)
    elif selected_role == "Dispatcher":
        register_btn.config(command=register_dispatcher)

l_main = Label(text="Choose the role to register as:", font=("Cooper Black", 15))
l_main.pack()
l_main.place(relx=0.5, rely=0.3, anchor="center")

registration_menu = OptionMenu(root, registration_type, "Client", "Dispatcher")
registration_menu.pack()
registration_menu.place(relx=0.5, rely=0.4, anchor="center")

registration_type.trace_add("write", reg_type)

register_btn = tk.Button(root, text="Choose", font=("Cooper Black", 15))
register_btn.pack()
register_btn.place(relx=0.5, rely=0.5, anchor="center")

center_window(root)
root.mainloop()