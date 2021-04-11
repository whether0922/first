list_data = []
for i in xrange(10):
	data = {
		"id": i,
		"out": i + 10,
	}
	list_data.append(data)
list_data.sort(key=lambda info: info.get("id"))
print list_data