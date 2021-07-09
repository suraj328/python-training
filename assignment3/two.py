#2.Make a list of ten students in your class. Print the name of each student whose name ends with ‘a’.
Bca_stds=['Anil','Manoz','Prashish','Subin','Homa','Mahendra','Samita','Subin','Rohil','Bipul']
#assigining value for searching
search='a'
#storing search result
searched=[data for data in Bca_stds if data.lower().endswith(search.lower())]

#printing search value
print(f"the name of students end with {search}: {searched}")