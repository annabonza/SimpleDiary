from database import create_table, add_entry, get_entries

menu = """Please select one of the following options:
1) New Entry
2) View Entries
3) Exit

What would you like to do? \n"""

welcome = "Hi! I'm your diary.\nFell welcome to share your thoughts!"


def prompt_new_entry():
	entry_content = input("Tell me about your day! ")
	entry_date = input("Please enter the date: ")

	add_entry(entry_content, entry_date)


def view_entries(entries):
	"""
	we receive entries as a tuple
	"""
	for entry in entries:
		print(f"{entry[1]}\n{entry[0]}\n\n")


print(welcome)
create_table()

user_input = input(menu)

while user_input != "3":
	if user_input == "1":
		prompt_new_entry()
	elif user_input == "2":
		view_entries(get_entries())
	else:
		print("Whoops! I don't understand...Try again with 1,2 or 3.\n ")

	user_input = input(menu)
