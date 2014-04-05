# To build and push to the web host:
#
# 1. gmake
# 2. scp to the web host to replace the old binary

all: bin bin/catalog-release-to-disk bin/gen-catalog-index

bin:
	mkdir -p bin

bin/catalog-release-to-disk: src/catalog-release-to-disk/catalog-release-to-disk.o src/opencsw/diskformat/diskformat.o
	gccgo -g -o $@ $?

bin/gen-catalog-index: src/gen-catalog-index/gen-catalog-index.o src/opencsw/diskformat/diskformat.o
	gccgo -g -o $@ $?

# This is a poor hack, but it gets it to compile.
src/catalog-release-to-disk/catalog-release-to-disk.o: src/opencsw/diskformat/diskformat.o
	mkdir -p opencsw
	ln -sf ../src/opencsw/diskformat/diskformat.o opencsw/diskformat.o
	gccgo -o $@ -g -c src/catalog-release-to-disk/catalog-release-to-disk.go

src/gen-catalog-index/gen-catalog-index.o: src/opencsw/diskformat/diskformat.o
	mkdir -p opencsw
	ln -sf ../src/opencsw/diskformat/diskformat.o opencsw/diskformat.o
	gccgo -o $@ -g -c src/gen-catalog-index/gen-catalog-index.go

%.o: %.go
	gccgo -o $@ -g -c $<

clean:
	rm -f src/opencsw/diskformat/diskformat.o bin/catalog-release-to-disk bin/gen-catalog-index
