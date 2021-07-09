#1. Make a list of ten students in your class. Print the name of each student whose name starts with ‘B’.
#storing the name list of ten students from class
Bca_stds=['Anil','Manoz','Prashish','Subin','Homa','Mahendra','Samita','Subin','Rohil','Bipul']
#assigining value for searching
search='b'
#storing search result
searched=[data for data in Bca_stds if data.lower().startswith(search.lower())]

#printing search value
print(f"the name of students starts with {search}: {searched}")
