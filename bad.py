from googlesearch import search

query = "多良車站"

for j in search(query, stop=5, pause=2.0): 
	print(j)
