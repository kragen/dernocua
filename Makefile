all:
	rm -r dernocua-020211231-1
	./go.py
	./genpdf.py dernocua-020211231-1
	./genpdf.py dernocua-020211231-1
