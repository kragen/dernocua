all:
	if [ -f dernocua-020211231 ]; then rm -r dernocua-020211231; fi
	./go.py
	./genpdf.py dernocua-020211231
	./genpdf.py dernocua-020211231
