# To build and push to the web host:
#
# 1. gmake
# 2. scp to the web host to replace the old binary

all: bin bin/catalog-release-to-disk

bin:
	mkdir -p bin

bin/catalog-release-to-disk: src/catalog-release-to-disk/catalog-release-to-disk.go
	gccgo -g -o $@ $<

# catalog-release-to-disk: catalog-release-to-disk.o
# 	gccgo -o $@ $<

# %.o: %.go
# 	gccgo -c $<
