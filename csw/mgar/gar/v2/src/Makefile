# To build and push to the web host:
#
# 1. gmake
# 2. scp to the web host to replace the old binary

all: catalog-release-to-disk

catalog-release-to-disk: catalog-release-to-disk.o
	gccgo -o $@ $<

%.o: %.go
	gccgo -c $<
