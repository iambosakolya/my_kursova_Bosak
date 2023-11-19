import os
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from Dispatcher import Dispatcher
from Client import Client
from Station import Station
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

    with open("files/client_firm.txt", "r") as file:
        content = file.read()
        if content.strip():
            client_created = True

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

def home_window():
    user_window.destroy()
    root.deiconify()

def user_init(user_type):
    global user_window
    global client_created
    global dispatcher_created
    if user_window is not None:
        user_window.destroy()

    user_window = Toplevel(root)
    user_window.title(f"{user_type}")
    user_window.resizable(width=False, height=False)
    user_window.geometry("750x650")
    user_window.transient(root)
    bg_img = PhotoImage(file="img/user_window.png")
    bg_label = Label(user_window, image=bg_img)
    bg_label.image = bg_img
    bg_label.place(relwidth=1, relheight=1)
    center_window(user_window)

    data_text = Text(user_window, wrap=tk.WORD, height=30, width=50)
    data_text.pack()
    data_text.place(x=300, y=100)
    check_user_creation()

    def view_contract():
        with open("files/contract.txt", "r") as file:
            contracts = file.read()
            if not contracts:
                messagebox.showerror("Empty File", "The file is empty.")
            else:
                data_text.delete(1.0, tk.END)
                data_text.insert(tk.INSERT, contracts)
    def view_address():
        with open("files/addresses.txt", "r") as file:
            addresses = file.read()
            if not addresses:
                messagebox.showerror("Empty File", "The file is empty.")
            else:
                data_text.delete(1.0, tk.END)
                data_text.insert(tk.INSERT, addresses)
    def view_firms():
        with open("files/client_firm.txt", "r") as file:
            clients = file.read()
            if not clients:
                messagebox.showerror("Empty File", "The file is empty.")
            else:
                data_text.delete(1.0, tk.END)
                data_text.insert(tk.INSERT, clients)
    def max_time():
        with open("files/max_delivery_time.txt", "r") as file:
            contracts = file.read()
            if not contracts:
                messagebox.showerror("Empty File", "The file is empty.")
            else:
                data_text.delete(1.0, tk.END)
                data_text.insert(tk.INSERT, contracts)
    def arrival_st():
        with open("files/pop_arrSt.txt", "r") as file:
            contracts = file.read()
            if not contracts:
                messagebox.showerror("Empty File", "The file is empty.")
            else:
                data_text.delete(1.0, tk.END)
                data_text.insert(tk.INSERT, contracts)
    def avg_time():
        with open("files/avg_time.txt", "r") as file:
            contracts = file.read()
            if not contracts:
                messagebox.showerror("Empty File", "The file is empty.")
            else:
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

    back_to_main_btn = Button(user_window, text="Go back", command=home_window,
                              font=("Cooper Black", 11))
    back_to_main_btn.pack()
    back_to_main_btn.place(x=660, y=600)

    if user_type == "Client":
        new_client_btn = Button(user_window, text="Create new client", command=client_reg, font=("Cooper Black", 12))
        new_contract_btn = Button(user_window, text="New contract", command=create_contract, font=("Cooper Black", 11))
        view_contract_btn = Button(user_window, text="List of contracts", command=view_contract, font=("Cooper Black", 11))
        view_address_btn = Button(user_window, text="List of delivery addresses", command=view_address, font=("Cooper Black", 11))
        view_firms_btn = Button(user_window, text="List of client's firms", command=view_firms, font=("Cooper Black", 11))
        clear_all_btn = Button(user_window, text="Clear all files", command=clear_all_files, font=("Cooper Black", 11))
        update_contract_btn = Button(user_window, text="Update Contract", command=update_contract, font=("Cooper Black", 11))

        new_client_btn.pack()
        new_contract_btn.pack()
        view_contract_btn.pack()
        view_address_btn.pack()
        view_firms_btn.pack()
        clear_all_btn.pack()
        update_contract_btn.pack()

        new_client_btn.place(x=50, y=100)
        new_contract_btn.place(x=10, y=170)
        view_contract_btn.place(x=10, y=240)
        view_address_btn.place(x=10, y=310)
        view_firms_btn.place(x=10, y=380)
        clear_all_btn.place(x=200, y=600)
        update_contract_btn.place(x=150, y=170)


        if not client_created:
            new_contract_btn.config(state=tk.DISABLED)
            view_contract_btn.config(state=tk.DISABLED)
            view_address_btn.config(state=tk.DISABLED)
            view_firms_btn.config(state=tk.DISABLED)
        else:
            new_contract_btn.config(state=tk.NORMAL)
            view_contract_btn.config(state=tk.NORMAL)
            view_address_btn.config(state=tk.NORMAL)
            view_firms_btn.config(state=tk.NORMAL)

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
        update_contract_btn = Button(user_window, text="Update Contract", command=update_contract, font=("Cooper Black", 11))

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
        update_contract_btn.pack()

        new_dispatcher_btn.place(x=50, y=100)
        new_contract_btn.place(x=10, y=160)
        view_contract_btn.place(x=10, y=215)
        view_address_btn.place(x=10, y=255)
        view_firms_btn.place(x=10, y=295)
        max_btn.place(x=5, y=335)
        view_max_btn.place(x=230, y=335)
        arr_btn.place(x=1, y=375)
        view_arr_btn.place(x=230, y=375)
        avg_btn.place(x=5, y=415)
        view_avg_btn.place(x=230, y=415)
        clear_all_btn.place(x=300, y=615)
        update_contract_btn.place(x=150, y=160)

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

        dispatcher_label = tk.Label(user_window, text="You are currently signed as a dispatcher:",
                                    font=("Cooper Black", 12))
        dispatcher_label.pack()
        dispatcher_label.place(x=200, y=20)

def create_contract():
    contract_window = Toplevel(root)
    contract_window.title("Create new contract")
    contract_window.resizable(width=False, height=False)
    contract_window.geometry("400x350")
    center_window(contract_window)
    back_image = PhotoImage(file="img/user.png")
    back_label = tk.Label(contract_window, image=back_image)
    back_label.place(relwidth=1, relheight=1)
    back_label.image = back_image

    def save_contract():
        contract_id = id_entry.get()
        if id_exists(contract_id):
            messagebox.showerror("Error", "Contract with this ID already exists.")
            return
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
            delivery_time = int(delivery_time)
            weight = float(weight)
            date = datetime.strptime(date, "%Y-%m-%d").date()
            cost = Decimal(cost)
        except ValueError:
            messagebox.showerror("Error", "Invalid data type for one or more fields.")
            contract_window.destroy()
            return

        contract = Contract(contract_id, dep_st, arr_st, insurance_sum, cargo_type, delivery_time, weight, date, cost)
        save(contract)

        messagebox.showinfo("Success", "Contract successfully created.")
        contract_window.destroy()
        user_window.deiconify()

    def id_exists(contract_id):
        with open("files/contract.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("Contract ID:") and contract_id in line:
                    return True
        return False

    # labels & entries
    id_lb = Label(contract_window, text="Contract ID:",font=("Cooper Black", 10))
    id_lb.pack()
    id_lb.place(x=10, y=10)
    id_entry = Entry(contract_window)
    id_entry.pack()
    id_entry.place(x=190, y=10)

    dep_lb = Label(contract_window, text="Departure station:",font=("Cooper Black", 10))
    dep_lb.pack()
    dep_lb.place(x=10, y=40)
    dep_entry = Entry(contract_window)
    dep_entry.pack()
    dep_entry.place(x=190, y=40)

    arr_lb = Label(contract_window, text="Arrival station:",font=("Cooper Black", 10))
    arr_lb.pack()
    arr_lb.place(x=10, y=70)
    arr_entry = Entry(contract_window)
    arr_entry.pack()
    arr_entry.place(x=190, y=70)

    type_lb = Label(contract_window, text="Cargo type:",font=("Cooper Black", 10))
    type_lb.pack()
    type_lb.place(x=10, y=100)
    type_entry = Entry(contract_window)
    type_entry.pack()
    type_entry.place(x=190, y=100)

    insurance_lb = Label(contract_window, text="Insurance sum:",font=("Cooper Black", 10))
    insurance_lb.pack()
    insurance_lb.place(x=10, y=130)
    val_lb = Label(contract_window, text="UAH",font=("Cooper Black", 10))
    val_lb.pack()
    val_lb.place(x=320, y=130)
    insurance_entry = Entry(contract_window)
    insurance_entry.pack()
    insurance_entry.place(x=190, y=130)

    time_lb = Label(contract_window, text="Delivery time:",font=("Cooper Black", 10))
    time_lb.pack()
    time_lb.place(x=10, y=160)
    t_lb = Label(contract_window, text="day(s)",font=("Cooper Black", 10))
    t_lb.pack()
    t_lb.place(x=320, y=160)
    time_entry = Entry(contract_window)
    time_entry.pack()
    time_entry.place(x=190, y=160)

    weight_lb = Label(contract_window, text="Weight:",font=("Cooper Black", 10))
    weight_lb.pack()
    weight_lb.place(x=10, y=190)
    w_lb = Label(contract_window, text="KG",font=("Cooper Black", 10))
    w_lb.pack()
    w_lb.place(x=320, y=190)
    weight_entry = Entry(contract_window)
    weight_entry.pack()
    weight_entry.place(x=190, y=190)

    date_lb = Label(contract_window, text="Contract date:",font=("Cooper Black", 10))
    date_lb.pack()
    date_lb.place(x=10, y=220)
    d_lb = Label(contract_window, text="(Y-M-D)",font=("Cooper Black", 10))
    d_lb.pack()
    d_lb.place(x=320, y=220)
    date_entry = Entry(contract_window)
    date_entry.pack()
    date_entry.place(x=190, y=220)

    cost_lb = Label(contract_window, text="Cost:",font=("Cooper Black", 10))
    cost_lb.pack()
    cost_lb.place(x=10, y=250)
    val_lb = Label(contract_window, text="UAH",font=("Cooper Black", 10))
    val_lb.pack()
    val_lb.place(x=320, y=250)
    cost_entry = Entry(contract_window)
    cost_entry.pack()
    cost_entry.place(x=190, y=250)

    cr_btn = Button(contract_window, text="Save contract",
                                 font=("Cooper Black", 11),
                                 command=save_contract)
    cr_btn.pack()
    cr_btn.place(x=130, y=290)

def save(contract):
    with open("files/contract.txt", "a") as file:
        file.write(f"Contract ID: {contract.contract_id}\n")
        file.write(f"Departure station: {contract.dep_st}\n")
        file.write(f"Arrival station: {contract.arr_st}\n")
        file.write(f"Insurance sum: {contract.insurance_sum} UAH\n")
        file.write(f"Cargo type: {contract.cargo_type}\n")
        file.write(f"Delivery time(in days): {contract.delivery_time}\n")
        file.write(f"Weight: {contract.weight} KG\n")
        file.write(f"Date of conclusion: {contract.date}\n")
        file.write(f"Cost: {contract.cost} UAH\n")
        file.write("\n")

    with open("files/addresses.txt", "a") as arrivalSt_file:
        arrivalSt_file.write(f"Contract ID: {contract.contract_id}\n")
        arrivalSt_file.write(f"Arrival Station: {contract.arr_st}\n")
        arrivalSt_file.write("\n")

def update_contract():
    def del_contract():
        selected_index = contracts_listbox.curselection()
        if selected_index:
            contract_id = contracts_listbox.get(selected_index[0])
            delete_files(contract_id)
            contracts_listbox.delete(selected_index)
            messagebox.showinfo("Success", f"Contract with ID {contract_id} is deleted.")
        else:
            messagebox.showinfo("Info", "Please select a contract to update.")
    def delete_files(contract_id):
        try:
            files = os.listdir("files")

            for file_name in files:
                file_path = os.path.join("files", file_name)

                with open(file_path, "r") as file:
                    lines = file.readlines()

                new_lines = []
                is_contract_block = False

                for line in lines:
                    if line.startswith("Contract ID:") and contract_id in line:
                        is_contract_block = True
                    elif line.startswith("Contract ID:") and not contract_id in line:
                        is_contract_block = False

                    if not is_contract_block:
                        new_lines.append(line)

                with open(file_path, "w") as file:
                    file.writelines(new_lines)

        except FileNotFoundError:
            messagebox.showerror("Error", f"File {file_name} not found.")
    def update_selected_contract():
        selected_index = contracts_listbox.curselection()
        if selected_index:
            contract_id = contracts_listbox.get(selected_index[0])
            update_contract_window = Toplevel(update_window)
            update_contract_window.title(f"Update {contract_id}")
            update_contract_window.geometry("400x350")
            center_window(update_contract_window)

            back_image = PhotoImage(file="img/user.png")
            back_label = tk.Label(update_contract_window, image=back_image)
            back_label.place(relwidth=1, relheight=1)
            back_label.image = back_image

            existing_data = get_contract_data(contract_id)

            dep_lb = Label(update_contract_window, text="Departure station:", font=("Cooper Black", 10))
            dep_lb.pack()
            dep_lb.place(x=10, y=40)
            dep_entry = Entry(update_contract_window)
            dep_entry.pack()
            dep_entry.place(x=190, y=40)

            arr_lb = Label(update_contract_window, text="Arrival station:", font=("Cooper Black", 10))
            arr_lb.pack()
            arr_lb.place(x=10, y=70)
            arr_entry = Entry(update_contract_window)
            arr_entry.pack()
            arr_entry.place(x=190, y=70)

            type_lb = Label(update_contract_window, text="Cargo type:", font=("Cooper Black", 10))
            type_lb.pack()
            type_lb.place(x=10, y=100)
            type_entry = Entry(update_contract_window)
            type_entry.pack()
            type_entry.place(x=190, y=100)

            insurance_lb = Label(update_contract_window, text="Insurance sum:", font=("Cooper Black", 10))
            insurance_lb.pack()
            insurance_lb.place(x=10, y=130)
            val_lb = Label(update_contract_window, text="UAH", font=("Cooper Black", 10))
            val_lb.pack()
            val_lb.place(x=320, y=130)
            insurance_entry = Entry(update_contract_window)
            insurance_entry.pack()
            insurance_entry.place(x=190, y=130)

            time_lb = Label(update_contract_window, text="Delivery time:", font=("Cooper Black", 10))
            time_lb.pack()
            time_lb.place(x=10, y=160)
            t_lb = Label(update_contract_window, text="day(s)", font=("Cooper Black", 10))
            t_lb.pack()
            t_lb.place(x=320, y=160)
            time_entry = Entry(update_contract_window)
            time_entry.pack()
            time_entry.place(x=190, y=160)

            weight_lb = Label(update_contract_window, text="Weight:", font=("Cooper Black", 10))
            weight_lb.pack()
            weight_lb.place(x=10, y=190)
            w_lb = Label(update_contract_window, text="KG", font=("Cooper Black", 10))
            w_lb.pack()
            w_lb.place(x=320, y=190)
            weight_entry = Entry(update_contract_window)
            weight_entry.pack()
            weight_entry.place(x=190, y=190)

            date_lb = Label(update_contract_window, text="Contract date:", font=("Cooper Black", 10))
            date_lb.pack()
            date_lb.place(x=10, y=220)
            d_lb = Label(update_contract_window, text="(Y-M-D)", font=("Cooper Black", 10))
            d_lb.pack()
            d_lb.place(x=320, y=220)
            date_entry = Entry(update_contract_window)
            date_entry.pack()
            date_entry.place(x=190, y=220)

            cost_lb = Label(update_contract_window, text="Cost:", font=("Cooper Black", 10))
            cost_lb.pack()
            cost_lb.place(x=10, y=250)
            val_lb = Label(update_contract_window, text="UAH", font=("Cooper Black", 10))
            val_lb.pack()
            val_lb.place(x=320, y=250)
            cost_entry = Entry(update_contract_window)
            cost_entry.pack()
            cost_entry.place(x=190, y=250)

            def save_updated_data():
                new_data = {
                    "Departure station": dep_entry.get(),
                    "Arrival station": arr_entry.get(),
                    "Insurance sum": insurance_entry.get(),
                    "Cargo type": type_entry.get(),
                    "Delivery time": time_entry.get(),
                    "Weight": weight_entry.get(),
                    "Date of conclusion": date_entry.get(),
                    "Cost": cost_entry.get()
                }
                update_contract_data(contract_id, new_data)
                update_contract_window.destroy()

            save_button = tk.Button(update_contract_window, text="Save", command=save_updated_data,
                                    font=("Cooper Black", 11))
            save_button.pack()
            save_button.place(x=170, y=300)
        else:
            messagebox.showinfo("Info", "Please select a contract to update.")

    def update_contract_data(contract_id, new_data):
        try:
            contract_file = os.path.join("files", "contract.txt")
            addresses_file = os.path.join("files", "addresses.txt")

            # Оновлення contract.txt
            with open(contract_file, "r") as file:
                lines = file.readlines()

            new_lines = []
            is_contract_block = False

            for line in lines:
                if line.startswith("Contract ID:") and contract_id in line:
                    is_contract_block = True
                    new_lines.append(line)
                elif line.startswith("Contract ID:") and not contract_id in line:
                    is_contract_block = False

                if is_contract_block and line.startswith("Contract ID:"):
                    for key, value in new_data.items():
                        new_lines.append(f"{key}: {value}\n")
                elif not is_contract_block:
                    new_lines.append(line)

            with open(contract_file, "w") as file:
                file.writelines(new_lines)

            # Оновлення addresses.txt
            with open(addresses_file, "r") as addr_file:
                addr_lines = addr_file.readlines()

            new_addr_lines = []
            is_contract_id_found = False

            for addr_line in addr_lines:
                if addr_line.startswith("Contract ID:") and contract_id in addr_line:
                    is_contract_id_found = True
                    new_addr_lines.append(addr_line)
                elif addr_line.startswith("Contract ID:") and not contract_id in addr_line:
                    is_contract_id_found = False

                if is_contract_id_found and addr_line.startswith("Arrival Station:"):
                    for key, value in new_data.items():
                        if key == "Arrival station":
                            new_addr_lines.append(f"{key}: {value}\n")
                elif not is_contract_id_found:
                    new_addr_lines.append(addr_line)

            with open(addresses_file, "w") as addr_file:
                addr_file.writelines(new_addr_lines)

        except FileNotFoundError as e:
            messagebox.showerror("Error", str(e))

    def get_contract_data(contract_id):
        try:
            files = os.listdir("files")

            for file_name in files:
                file_path = os.path.join("files", file_name)

                with open(file_path, "r") as file:
                    lines = file.readlines()

                contract_data = {"Contract ID": contract_id}
                is_contract_block = False

                for line in lines:
                    if line.startswith("Contract ID:") and contract_id in line:
                        is_contract_block = True
                    elif line.startswith("Contract ID:") and not contract_id in line:
                        is_contract_block = False

                    if is_contract_block:
                        parts = line.split(":")
                        if len(parts) == 2:
                            key, value = parts[0].strip(), parts[1].strip()
                            contract_data[key] = value
                return contract_data

        except FileNotFoundError:
            messagebox.showerror("Error", f"File {file_name} not found.")

    update_window = Toplevel(root)
    update_window.title("Update contract")
    update_window.geometry("500x400")
    center_window(update_window)

    back_image = PhotoImage(file="img/user.png")
    back_label = tk.Label(update_window, image=back_image)
    back_label.place(relwidth=1, relheight=1)
    back_label.image = back_image

    contracts_listbox = Listbox(update_window, selectmode="SINGLE")
    contracts_listbox.pack(pady=10)

    try:
        with open("files/contract.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("Contract ID:"):
                    contracts_listbox.insert(END, line.strip())
    except FileNotFoundError:
        messagebox.showerror("Error", "File 'contract.txt' not found.")

    update_button = Button(update_window, text="Update contract", font=("Cooper Black", 11),
                           command=update_selected_contract)
    update_button.pack(pady=10)

    delete_button = Button(update_window, text="Delete contract", font=("Cooper Black", 11), command=del_contract)
    delete_button.pack(pady=10)

update_contract_button = Button(root, text="Update contract", command=update_contract, font=("Cooper Black", 15))
update_contract_button.pack()

def client_reg():
    client_reg = tk.Toplevel(root)
    client_reg.title("Client registration")
    client_reg.resizable(width=False, height=False)
    client_reg.geometry("400x250")
    center_window(client_reg)
    back_image = PhotoImage(file="img/user.png")
    back_label = tk.Label(client_reg, image=back_image)
    back_label.place(relwidth=1, relheight=1)
    back_label.image = back_image

    firm_lab = tk.Label(client_reg, text="Firm name:",font=("Cooper Black", 11))
    firm_lab.pack()
    firm_lab.place(x=10, y=25)

    firm_ent = tk.Entry(client_reg)
    firm_ent.pack()
    firm_ent.place(x=150, y=28)

    address_lab = tk.Label(client_reg, text="Address:",font=("Cooper Black", 11))
    address_lab.pack()
    address_lab.place(x=10, y=65)

    address_ent = tk.Entry(client_reg)
    address_ent.pack()
    address_ent.place(x=150, y=68)

    phone_lab = tk.Label(client_reg, text="Phone number:",font=("Cooper Black", 11))
    phone_lab.pack()
    phone_lab.place(x=10, y=105)

    phone_ent = tk.Entry(client_reg)
    phone_ent.pack()
    phone_ent.place(x=150, y=108)

    pib_label = tk.Label(client_reg, text="PIB:",font=("Cooper Black", 11))
    pib_label.pack()
    pib_label.place(x=10, y=145)

    pib_lb = tk.Label(client_reg, text="e.g. Bosak O.S.", font=("Cooper Black", 10))
    pib_lb.pack()
    pib_lb.place(x=290, y=145)

    pib_entry = tk.Entry(client_reg)
    pib_entry.pack()
    pib_entry.place(x=150, y=148)

    def save_client_reg():
        firm_name = firm_ent.get()
        address = address_ent.get()
        phone_number = phone_ent.get()
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
                file.write("Phone number(+38): {}\n".format(phone_number))
                file.write("PIB: {}\n".format(pib))
                file.write("\n")

            messagebox.showinfo("Success", "Client successfully created.")
            client_reg.destroy()
        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid data: {str(ve)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    sv_btn = tk.Button(client_reg, text="Write to file",
                       command=save_client_reg,
                       font=("Cooper Black", 11))
    sv_btn.pack()
    sv_btn.place(relx=0.5, rely=0.9, anchor='s')

def dispatcher_reg():
    dispatcher_reg = tk.Toplevel(root)
    dispatcher_reg.title("Dispatcher registration")
    dispatcher_reg.resizable(width=False, height=False)
    dispatcher_reg.geometry("400x300")
    center_window(dispatcher_reg)
    back_image = PhotoImage(file="img/user.png")
    back_label = tk.Label(dispatcher_reg, image=back_image)
    back_label.place(relwidth=1, relheight=1)
    back_label.image = back_image

    firm_label = tk.Label(dispatcher_reg, text="Firm name:",font=("Cooper Black", 11))
    firm_label.pack()
    firm_label.place(x=10, y=25)

    firm_entry = tk.Entry(dispatcher_reg)
    firm_entry.pack()
    firm_entry.place(x=150, y=28)

    address_label = tk.Label(dispatcher_reg, text="Address:",font=("Cooper Black", 11))
    address_label.pack()
    address_label.place(x=10, y=65)

    address_entry = tk.Entry(dispatcher_reg)
    address_entry.pack()
    address_entry.place(x=150, y=68)

    phone_label = tk.Label(dispatcher_reg, text="Phone number:",font=("Cooper Black", 11))
    phone_label.pack()
    phone_label.place(x=10, y=105)

    phone_entry = tk.Entry(dispatcher_reg)
    phone_entry.pack()
    phone_entry.place(x=150, y=108)

    pib_label = tk.Label(dispatcher_reg, text="PIB:",font=("Cooper Black", 11))
    pib_label.pack()
    pib_label.place(x=10, y=145)

    pib_lb = tk.Label(dispatcher_reg, text="e.g. Bosak O.S.", font=("Cooper Black", 10))
    pib_lb.pack()
    pib_lb.place(x=290, y=145)

    pib_entry = tk.Entry(dispatcher_reg)
    pib_entry.pack()
    pib_entry.place(x=150, y=148)

    experience_label = tk.Label(dispatcher_reg, text="Work experience:",font=("Cooper Black", 11))
    experience_label.pack()
    experience_label.place(x=10, y=185)

    e_label = tk.Label(dispatcher_reg, text="years", font=("Cooper Black", 11))
    e_label.pack()
    e_label.place(x=290, y=185)

    experience_entry = tk.Entry(dispatcher_reg)
    experience_entry.pack()
    experience_entry.place(x=150, y=188)
    def save_dispatcher_reg():
        firm_name = firm_entry.get()
        address = address_entry.get()
        phone_number = phone_entry.get()
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
            experience = float(experience)
            if not isinstance(experience, float):
                raise ValueError("Work experience must be a float")

            dispatcher = Dispatcher(firm_name, address, phone_number, pib, experience)
            with open("files/dispatcher.txt", "a") as file:
                file.write("Firm name: {}\n".format(firm_name))
                file.write("Address: {}\n".format(address))
                file.write("Phone number(+38): {}\n".format(phone_number))
                file.write("PIB: {}\n".format(pib))
                file.write("Work experience: {} years\n".format(experience))
                file.write("\n")

            messagebox.showinfo("Success", "Dispatcher successfully created.")
            dispatcher_reg.destroy()
        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid data: {str(ve)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    save_btn = tk.Button(dispatcher_reg, text="Write to file",
                         command=save_dispatcher_reg,
                         font=("Cooper Black", 11))
    save_btn.pack()
    save_btn.place(relx=0.5, rely=0.9, anchor='s')

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
                    delivery_time = int(contract_info.get("Delivery time(in days)", 0))
                    if delivery_time > max_delivery:
                        max_delivery = delivery_time
                        id = current_id

                current_id = line.strip().replace("Contract ID: ", "")
                contract_info = {}
            if ":" in line:
                key, value = map(str.strip, line.split(":", 1))
                contract_info[key] = value

        if current_id:
            delivery_time = int(contract_info.get("Delivery time(in days)", 0))
            if delivery_time > max_delivery:
                max_delivery = delivery_time
                id = current_id

    if id:
        with open("files/max_delivery_time.txt", "w") as output_file:
            output_file.write(f"Contract ID: {id}\n")
            output_file.write(f"Max delivery time: {max_delivery} days\n")

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
            output_file.write(f"Number of contracts with such address: {max_count}\n")

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
                    delivery_time = int(contract_info.get("Delivery time(in days)", 0))  # Corrected key
                    total_delivery_time += delivery_time
                    contract_count += 1

                id = line.strip().replace("Contract ID: ", "")
                contract_info = {}

            if ":" in line:
                key, value = map(str.strip, line.split(":", 1))
                contract_info[key] = value
        if id:
            delivery_time = int(contract_info.get("Delivery time(in days)", 0))  # Corrected key
            total_delivery_time += delivery_time
            contract_count += 1

    if contract_count > 0:
        average_delivery_time = round(total_delivery_time / contract_count, 1)
        messagebox.showinfo("Success", f"Average delivery time saved in file")

        with open("files/avg_time.txt", "w") as output_file:
            output_file.write(f"Average delivery time: {average_delivery_time} days")

    else:
        messagebox.showerror("No contracts", "No contracts found in the file.")


def register_client():
    user_init("Client")
def register_dispatcher():
    user_init("Dispatcher")
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