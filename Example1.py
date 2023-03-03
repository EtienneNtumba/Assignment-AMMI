import fileinput,os,sys

F = open(sys.argv[2],"wt")

D ={}

for line in open(sys.argv[1]):
	data = line.split()
	if data[0] in D:
		paass
	else:
		F.write("\t".join(data)+"\n") 
