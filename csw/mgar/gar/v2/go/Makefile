# To build and push to the web host:
#
# 1. gmake
# 2. scp to the web host to replace the old binary

BINARIES += bin/catalog-release-to-disk
# BINARIES += bin/crashtest
BINARIES += bin/gen-catalog-index
BINARIES += bin/promote-packages

# On GNU/Linux, 'install'
INSTALL = ginstall

all: bin $(BINARIES)

bin:
	mkdir -p bin

opencsw:
	mkdir -p opencsw

bin/catalog-release-to-disk: opencsw/diskformat.o src/catalog-release-to-disk/catalog-release-to-disk.o
	gccgo -g -o $@ $^

bin/gen-catalog-index: opencsw/diskformat.o src/gen-catalog-index/gen-catalog-index.o
	gccgo -g -o $@ $^

# bin/crashtest: src/crashtest/crashtest.go opencsw/diskformat.o
# 	gccgo -g -o $@ $^

bin/promote-packages: src/promote-packages/promote-packages.go opencsw/diskformat.o opencsw/mantis.o
	gccgo -g -o $@ $^

opencsw/diskformat.o: opencsw src/opencsw/diskformat/diskformat.o
	$(INSTALL) -m 755 src/opencsw/diskformat/diskformat.o opencsw/diskformat.o

opencsw/mantis.o: opencsw src/opencsw/mantis/mantis.o
	# $(INSTALL)
	cp src/opencsw/mantis/mantis.o opencsw/mantis.o

%.o: %.go
	gccgo -o $@ -g -c $<

clean:
	find . -name '*.o' -exec rm -f {} \;
	rm -f $(BINARIES)
