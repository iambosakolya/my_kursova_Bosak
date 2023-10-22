import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import Scrollbar
from Dispatcher import Dispatcher
from Client import Client
from Contract import Contract

# constructor Tk()
root = tk.Tk()
root.geometry("750x650")
root.title("Rail Cargo Solutions")
root.resizable(width=False, height=False)

# for choosing registration
registration_type = StringVar()

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def user_window(user_type):
    user_window = Toplevel(root)
    user_window.title(f"{user_type}")
    user_window.resizable(width=False, height=False)
    user_window.geometry("750x650")
    center_window(user_window)

    data_text = Text(user_window, wrap=tk.WORD, height=30, width=50)
    data_text.pack()
    data_text.place(x=300, y=100)

    def view_contract():
        with open("contract.txt", "r") as file:
            contracts = file.read()
            data_text.delete(1.0, tk.END)
            data_text.insert(tk.INSERT, contracts)

    def view_address():
        with open("addresses.txt", "r") as file:
            addresses = file.read()
            data_text.delete(1.0, tk.END)
            data_text.insert(tk.INSERT, addresses)

    def view_firms():
        with open("client_firm.txt", "r") as file:
            clients = file.read()
            data_text.delete(1.0, tk.END)
            data_text.insert(tk.INSERT, clients)

    if user_type == "Client":
        client_label = tk.Label(user_window, text="You are currently signed as a client:", font=("Cooper Black", 12))
        client_label.pack()
        client_label.place(x=200, y=20)

        new_client_btn = Button(user_window, text="Create new client", command=client_reg_window)
        new_contract_btn = Button(user_window, text="New contract", command=create_contract)
        view_contract_btn = Button(user_window, text="View the list of contracts", command=view_contract)
        view_address_btn = Button(user_window, text="View the list of delivery addresses", command=view_address)
        view_firms_btn = Button(user_window, text="View the list of client's firms", command=view_firms)

        new_client_btn.pack()
        new_contract_btn.pack()
        view_contract_btn.pack()
        view_address_btn.pack()
        view_firms_btn.pack()

        new_client_btn.place(x=70, y=160)
        new_contract_btn.place(x=70, y=200)
        view_contract_btn.place(x=70, y=240)
        view_address_btn.place(x=70, y=280)
        view_firms_btn.place(x=70, y=320)

    elif user_type == "Dispatcher":
        dispatcher_label = tk.Label(user_window, text="You are currently signed as a dispatcher:",
                                    font=("Cooper Black", 12))
        dispatcher_label.pack()
        dispatcher_label.place(x=200, y=20)

        new_dispatcher_btn = Button(user_window, text="Create new dispatcher")
        new_contract_btn = Button(user_window, text="New contract", command=create_contract)
        view_contract_btn = Button(user_window, text="View the list of contracts", command=view_contract)
        view_address_btn = Button(user_window, text="View the list of delivery addresses", command=view_address)
        view_firms_btn = Button(user_window, text="View the list of client's firms", command=view_firms)

        new_dispatcher_btn.pack()
        new_contract_btn.pack()
        view_contract_btn.pack()
        view_address_btn.pack()
        view_firms_btn.pack()

        new_dispatcher_btn.place(x=70, y=160)
        new_contract_btn.place(x=70, y=200)
        view_contract_btn.place(x=70, y=240)
        view_address_btn.place(x=70, y=280)
        view_firms_btn.place(x=70, y=320)


def create_contract():
    contract_window = Toplevel(root)
    contract_window.title("Create new contract")
    contract_window.resizable(width=False, height=False)
    contract_window.geometry("400x300")
    center_window(contract_window)

    def save_contract():
        contract_id = contract_id_entry.get()
        dep_st = dep_st_entry.get()
        arr_st = arr_st_entry.get()
        insurance_sum = insurance_sum_entry.get()
        cargo_type = cargo_type_entry.get()
        delivery_time = delivery_time_entry.get()
        weight = weight_entry.get()
        date = date_entry.get()
        cost = cost_entry.get()

        contract = Contract(contract_id, dep_st, arr_st, insurance_sum, cargo_type,
                            delivery_time, weight, date, cost)
        save_contract_to_file(contract)
        messagebox.showinfo("Success", f"Contract {contract_id} created successfully.")

    contract_id_label = Label(contract_window, text="Contract ID:")
    contract_id_label.pack()
    contract_id_label.place(x=10, y=10)

    contract_id_entry = Entry(contract_window)
    contract_id_entry.pack()
    contract_id_entry.place(x=150, y=10)

    dep_st_label = Label(contract_window, text="Departure station:")
    dep_st_label.pack()
    dep_st_label.place(x=10, y=40)

    dep_st_entry = Entry(contract_window)
    dep_st_entry.pack()
    dep_st_entry.place(x=150, y=40)

    arr_st_label = Label(contract_window, text="Arrival station:")
    arr_st_label.pack()
    arr_st_label.place(x=10, y=70)

    arr_st_entry = Entry(contract_window)
    arr_st_entry.pack()
    arr_st_entry.place(x=150, y=70)

    insurance_sum_label = Label(contract_window, text="Insurance sum:")
    insurance_sum_label.pack()
    insurance_sum_label.place(x=10, y=100)

    insurance_sum_entry = Entry(contract_window)
    insurance_sum_entry.pack()
    insurance_sum_entry.place(x=150, y=100)

    cargo_type_label = Label(contract_window, text="Cargo type:")
    cargo_type_label.pack()
    cargo_type_label.place(x=10, y=130)

    cargo_type_entry = Entry(contract_window)
    cargo_type_entry.pack()
    cargo_type_entry.place(x=150, y=130)

    delivery_time_label = Label(contract_window, text="Delivery time:")
    delivery_time_label.pack()
    delivery_time_label.place(x=10, y=160)

    delivery_time_entry = Entry(contract_window)
    delivery_time_entry.pack()
    delivery_time_entry.place(x=150, y=160)

    weight_label = Label(contract_window, text="Weight:")
    weight_label.pack()
    weight_label.place(x=10, y=190)

    weight_entry = Entry(contract_window)
    weight_entry.pack()
    weight_entry.place(x=150, y=190)

    date_label = Label(contract_window, text="Date of conclusion:")
    date_label.pack()
    date_label.place(x=10, y=220)

    date_entry = Entry(contract_window)
    date_entry.pack()
    date_entry.place(x=150, y=220)

    cost_label = Label(contract_window, text="Cost:")
    cost_label.pack()
    cost_label.place(x=10, y=250)

    cost_entry = Entry(contract_window)
    cost_entry.pack()
    cost_entry.place(x=150, y=250)

    create_contract_btn = Button(contract_window, text="Save contract", command=save_contract)
    create_contract_btn.pack()
    create_contract_btn.place(x=150, y=270)

def save_contract_to_file(contract):
    with open("contract.txt", "a") as file:
        file.write(f"\nContract ID: {contract.contract_id}\n")
        file.write(f"Departure station: {contract.dep_st}\n")
        file.write(f"Arrival station: {contract.arr_st}\n")
        file.write(f"Insurance sum: {contract.insurance_sum}\n")
        file.write(f"Cargo type: {contract.cargo_type}\n")
        file.write(f"Delivery time: {contract.delivery_time}\n")
        file.write(f"Weight: {contract.weight}\n")
        file.write(f"Date of conclusion: {contract.date}\n")
        file.write(f"Cost: {contract.cost}\n")

    with open("addresses.txt", "a") as arrivalSt_file:
        arrivalSt_file.write(f"\nContract ID: {contract.contract_id}\n"
                                       f"Arrival Station: {contract.arr_st}")

def client_reg_window():
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

    def save_client_registration():
        firm_name = firm_name_entry.get()
        address = address_entry.get()
        phone_number = phone_number_entry.get()
        pib = pib_entry.get()

        try:
            client = Client(firm_name, address, phone_number, pib)
            with open("client_firm.txt", "a") as file:
                file.write("Firm Name: {}\n".format(firm_name))
                file.write("Address: {}\n".format(address))
                file.write("Phone Number: {}\n".format(phone_number))
                file.write("PIB: {}\n".format(pib))
                file.write("\n")

            messagebox.showinfo("Success", "Client successfully сreated.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    sv_btn = tk.Button(client_reg_window, text="Write to file", command=save_client_registration)
    sv_btn.pack()
    sv_btn.place(relx=0.5, rely=0.8, anchor='s')

def register_client():
    user_window("Client")

def register_dispatcher():
    user_window("Dispatcher")

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