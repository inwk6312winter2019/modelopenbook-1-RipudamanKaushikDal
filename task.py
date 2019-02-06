keys=[]
val=[]
file=open('running-config.cfg')
def list_ifname_ip(fin):
	for lines in fin:
		line=lines.strip()
		for word in line.split():
			if word=='nameif':
				list1=line.split()
				keys.append(list1[-1])
	return keys


def print_val(fin):
	for sent in fin:
		sents=sent.strip()
		for words in sents.split():
			if words=='address':
				list2=sents.split()
				val.append((list2[-2],list2[-1]))

	return val

names=list_ifname_ip(file)
file=open('running-config.cfg')
values=print_val(file)

dic=dict(zip(names,values))
print(dic)
