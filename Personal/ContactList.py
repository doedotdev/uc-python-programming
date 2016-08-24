__author__ = 'bhorn'
'''
TODO LIST
1- on file i/o, encryption and splitting can be messed up if a , is in a name or number entry
2- add more entrys than name and number
3- Format all tkinter boxes to be uniform
4- make sizing correct so we can put on diffrenet sccreens, it should always fit
5- seacrh shouldnt have to be so specifi, ie ben should find benjamin
6- take search field down to one and just seacrh everything
7- just make general tkinter fiunction that can be called on sapecif parmaters
8- variable names should be more uniform
9- clean up and format all
10- if you exit without exit button, the list is not saved.
11- should we save as we go? or would that be too slow?
12- can the encryption be more serious, or is it neccessarey
13- is it safe to store contacts in a text file
14- SHould there be a back button? instead of reverting to the main_menu function each time?
'''

import os
import sys
import operator
import string

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import Tk, Frame, Menu

contact_list = []; # instantiate the temporary list to work through
###############################################
def main_menu(contact_list):
    main = Tk()
    main.title('Contact List')
    btn = Button(main, text="Show All", command= lambda:  show_all(contact_list, main))
    btn.pack(side=TOP)
    
    btn1 = Button(main, text="Add Contact", command= lambda: add_contact(contact_list, main))
    btn1.pack(side=TOP)
    
    btn2 = Button(main, text="Delete Contact",command = lambda: delete_contact(contact_list, main))
    btn2.pack(side=TOP)

    btn3 = Button(main, text="Edit Contact", command= lambda: edit_contact(contact_list, main))
    btn3.pack(side=TOP)
    
    btn4 = Button(main, text="Search Contacts", command= lambda: search_contacts(contact_list, main))
    btn4.pack(side=TOP)
    
    btn5 = Button(main, text="Format and Sort Contacts", command  =lambda: format_contacts(contact_list,main))
    btn5.pack(side=TOP)

    btn6 = Button(main, text="Exit Contacts", command= lambda: exit_list(contact_list, main))
    btn6.pack(side=TOP)
    main.mainloop()
    
############################################### --> DONE
def encrypt_list(entry):
    temp_store = ''
    for i in range(len(entry)):
        temp_store  = temp_store + chr(ord(entry[i])+5)
    return temp_store
    
############################################### --> DONE
def decrypt_list(entry):
    temp_store = ''
    for i in range(len(entry)):
        temp_store  = temp_store + chr(ord(entry[i])-5)
    return temp_store
    

############################################### --> DONE
def file_in(contact_list):
    print("Opening Contacts")
    if os.path.isfile("ContactList.txt"):
        my_file = open("ContactList.txt", "r+")
        my_file.close()
    else:
        my_file = open("ContactList.txt", "w")
        my_file.close()

    my_file = open("ContactList.txt", "r+")
    print("Open Successful")
    ##########
    lines = my_file.readlines()
    if len(lines) >= 1:
        for entry in lines:
            split = entry.strip().split(",")
            temp_dict = {"name": decrypt_list(split[0]), "number": decrypt_list(split[1])}
            contact_list.append(temp_dict)
        del split
        del temp_dict
        del lines
    else:
        print('Add something else here, a pop up or something')
        # TODO
    my_file.close()
    main_menu(contact_list)

############################################### --> DONE
def file_out(contact_list):
    my_file = open("ContactList.txt", "r+")
    my_file.truncate()
    for element in contact_list:
        my_file.write(encrypt_list(element['name']))
        my_file.write(",")
        my_file.write(encrypt_list(element['number']))
        my_file.write("\n")
    del contact_list
    my_file.close()


############################################### --> DONE
def format_contacts(contact_list,main):
    main.destroy()
    for item in contact_list:
        item['name'] = string.capwords(item['name'])
    sort_contacts(contact_list)


############################################### --> DONE
def sort_contacts(contact_list):
    new_list = sorted(contact_list, key=operator.itemgetter('name'))
    main_menu(new_list)


############################################### --> DONE
def show_all(contact_list, main):
    main.destroy()

    showall = Tk()
    i = 1
    for item in contact_list:
        show = Label(showall, text=item['name'] + ": " + item['number'])
        show.pack(fill=X)
    btn1 = Button(showall, text="Exit", command= lambda: showall.destroy())
    btn1.pack(side=BOTTOM)
    
    showall.mainloop()
    
    main_menu(contact_list)


############################################### --> DONE
def search_element(type, contact_list, criteria, top): 
    top.destroy()
    showall = Tk()
    i = 1
    length = len(contact_list)
    i = 0
    for item in contact_list:
        i = i + 1
        if item[type].lower() == criteria.lower():
            show = Label(showall, text=(contact_list[i-1])['name'] + ": " + item['number'])
            show.pack(fill=X)
    btn1 = Button(showall, text="Exit", command= lambda: showall.destroy())
    btn1.pack(side=BOTTOM)
    
    showall.mainloop()
    
    main_menu(contact_list)

############################################### --> DONE
def search_contacts(contact_list, main):
    main.destroy()
    search = Tk()
    search.title('Contact Search')
    btn = Button(search, text="Search Name", command= lambda:  search_name(contact_list,search))
    btn.pack(side=TOP)
    
    btn1 = Button(search, text="Search Number", command= lambda: search_number(contact_list,search))
    btn1.pack(side=TOP)

    def search_name(contact_list, search):
        search.destroy()
        top = Tk()
        top.title('Add Contact')
        # Box 1
        Label(top, text="Enter name:").pack(side=TOP)
        ent = Entry(top)
        ent.insert(INSERT, 'Name') #pre populates the field
        ent.pack(side=TOP)

        btn6 = Button(top, text="Search", command= lambda: search_element('name', contact_list, ent.get(), top))
        btn6.pack(side=TOP)

        top.mainloop()
    def search_number(contact_list, search):
        search.destroy()
        top = Tk()
        top.title('Add Contact')
        # Box 1
        Label(top, text="Enter Number:").pack(side=TOP)
        ent = Entry(top)
        ent.insert(INSERT, 'Number') #pre populates the field
        ent.pack(side=TOP)

        btn6 = Button(top, text="Search", command= lambda: search_element('number', contact_list, ent.get(), top))
        btn6.pack(side=TOP)

        top.mainloop()


############################################### --> DONE
def add_contact(contact_list, main):
    main.destroy()
    
    top = Tk()
    top.title('Add Contact')
    # Box 1
    Label(top, text="Enter your name:").pack(side=TOP)
    ent = Entry(top)
    ent.pack(side=TOP)
    #Box 2
    Label(top, text="Enter your number:").pack(side=TOP)
    ent2 = Entry(top)
    ent2.pack(side=TOP)
    # Button 1
    btn = Button(top, text="Submit", command=(lambda: saveContact(ent.get(), ent2.get())))
    btn.pack(side=LEFT)
    
    btn2 = Button(top, text="Exit", command=(lambda: top.destroy()))
    btn2.pack(side=LEFT)
    def saveContact(name, number):
            temp_dict = {"name": name, "number": number}
            contact_list.append(temp_dict)
            showinfo(title='Success', message='Contact Added!')
            del temp_dict
    top.mainloop()
    
    main_menu(contact_list)


############################################### --> DONE
def delete_contact(contact_list, main):
    main.destroy()
    def tkinter_delete():
        delete = Tk()
        delete.title('Contact List')
        
        for i in range(len(contact_list)):
            each = contact_list[i]
            btn = Button(delete,text = each['name'], command= lambda to_del = i: to_delete(to_del,delete))
            btn.pack(side = TOP)
        btn2 = Button(delete, text="Exit", command=(lambda: exit_delete(delete)))
        btn2.pack(side=LEFT)
    def to_delete(number, delete):
        delete.destroy()
        del contact_list[number]
        tkinter_delete()
    def exit_delete(delete):
        delete.destroy()
        main_menu(contact_list)
        
    tkinter_delete()

############################################### --> DONE
def edit_contact(contact_list, main):
    main.destroy()
    def tkinter_edit():
        edit = Tk()
        edit.title('Contact List')
        
        for i in range(len(contact_list)):
            each = contact_list[i]
            btn = Button(edit,text = each['name'], command= lambda to_edit = i: to_be_edited(to_edit,edit))
            btn.pack(side = TOP)
        btn2 = Button(edit, text="Exit", command=(lambda: exit_edit(edit)))
        btn2.pack(side=LEFT)
    def to_be_edited(number, edit):
        edit.destroy()
        ##################
        each = contact_list[number]
        top = Tk()
        top.title('Add Contact')
        # Box 1
        Label(top, text="Enter your name:").pack(side=TOP)
        ent = Entry(top)
        ent.insert(INSERT, each['name']) #pre populates the field
        ent.pack(side=TOP)
        #Box 2
        Label(top, text="Enter your number:").pack(side=TOP)
        ent2 = Entry(top)
        ent2.insert(INSERT, each['number'])
        ent2.pack(side=TOP)
        # Button 1
        btn = Button(top, text="Submit", command=(lambda: saveContact(number,ent.get(), ent2.get())))
        btn.pack(side=LEFT)
        
        btn2 = Button(top, text="Exit", command=(lambda: top.destroy()))
        btn2.pack(side=LEFT)
        def saveContact(place, name, number):
                temp_dict = {"name": name, "number": number}
                contact_list[place] = temp_dict
                showinfo(title='Success', message='Contact Edited!')
                del temp_dict
        top.mainloop()

        ####################
        tkinter_edit()
    def exit_edit(edit):
        edit.destroy()
        main_menu(contact_list)
        
    tkinter_edit()


############################################### --> DONE
def exit_list(contact_list, main):
    file_out(contact_list)
    main.destroy()
    sys.exit()
    

###############################################
# To do at run time
print(encrypt_list('hello'))
print(decrypt_list(encrypt_list('hello')))
file_in(contact_list) # Take file in intitialy
main_menu(contact_list) # start the main loop


