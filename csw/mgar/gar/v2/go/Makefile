# To build and push to the web host:
#
# 1. gmake
# 2. scp to the web host to replace the old binary

BINARIES += bin/catalog-release-to-disk
BINARIES += bin/crashtest
BINARIES += bin/gen-catalog-index
BINARIES += bin/promote-packages

LIBS = diskformat

all: bin $(BINARIES)

bin:
	mkdir -p bin

opencsw:
	mkdir -p opencsw

bin/catalog-release-to-disk: src/catalog-release-to-disk/catalog-release-to-disk.o src/opencsw/diskformat/diskformat.o
	gccgo -g -o $@ $?

bin/gen-catalog-index: src/gen-catalog-index/gen-catalog-index.o src/opencsw/diskformat/diskformat.o
	gccgo -g -o $@ $?

bin/crashtest: src/crashtest/crashtest.go opencsw/diskformat.o
	gccgo -g -o $@ $?

bin/promote-packages: src/promote-packages/promote-packages.go opencsw/diskformat.o
	gccgo -g -o $@ $?

opencsw/diskformat.o: opencsw src/opencsw/diskformat/diskformat.o
	# Not portable to Linux. But we can't just use 'install' on Solaris.
	ginstall -m 755 src/opencsw/diskformat/diskformat.o opencsw/diskformat.o

# This is a poor hack, but it gets it to compile.
src/catalog-release-to-disk/catalog-release-to-disk.o: src/opencsw/diskformat/diskformat.o opencsw/diskformat.o
	gccgo -o $@ -g -c src/catalog-release-to-disk/catalog-release-to-disk.go

src/gen-catalog-index/gen-catalog-index.o: src/opencsw/diskformat/diskformat.o opencsw/diskformat.o
	gccgo -o $@ -g -c src/gen-catalog-index/gen-catalog-index.go

src/promote-packages/promote-packages.o: src/opencsw/diskformat/diskformat.o opencsw/diskformat.o
	gccgo -o $@ -g -c src/promote-packages/promote-packages.go

src/crashtest/crashtest.o: src/opencsw/diskformat/diskformat.o opencsw/diskformat.o
	gccgo -o $@ -g -c src/crashtest/crashtest.go

%.o: %.go
	gccgo -o $@ -g -c $<

clean:
	find . -name '*.o' -exec rm -f {} \;
	rm -f $(BINARIES)
