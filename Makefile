all:
	rm -r dernocua-020211231-2
	./go.py
	./genpdf.py dernocua-020211231-2
	./genpdf.py dernocua-020211231-2