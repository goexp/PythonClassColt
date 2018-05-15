from csv import reader,writer

def update_users(first_name,last_name,new_first_name,new_last_name):
	rows=[]
	with open("users.csv") as file:
		csv_file_iterator=reader(file)
		for line in csv_file_iterator:
			if line[0] == first_name and line[1] == last_name:
				rows.append([new_first_name,new_last_name])
			else:
				rows.append([line[0],line[1]])
	
	with open("users.csv","w") as file:
		csv_file_iterator=writer(file)
		csv_file_iterator.writerows(rows)

update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.