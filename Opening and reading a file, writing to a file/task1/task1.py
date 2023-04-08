import pprint
cook_book = {}
d = []

with open('recipes.txt', 'rt', encoding='utf8') as file:
	for l in file:
		name = l.strip()
		ingredient_list = []
		dishes = {"name": name, "ingredient_name": []}
		person_count = file.readline()
		for i in range(int(person_count)):
			emp = file.readline()
			ingredient_name, quantity, measure  = emp.strip().split(' | ')
			ingredient_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
			dep = {name: ingredient_list}
		blank_line = file.readline()
		cook_book.update(dep)
		d.append(name)

pp = pprint.PrettyPrinter(indent=5)
pp.pprint(cook_book)



