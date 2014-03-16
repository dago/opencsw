all: make-catalog-links

catalog-release-to-disk: catalog-release-to-disk.o
	gccgo -o $@ $<

%.o: %.go
	gccgo -c $<
