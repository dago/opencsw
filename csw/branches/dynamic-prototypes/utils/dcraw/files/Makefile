myprefix?=/opt/csw
LDFLAGS+=-lm -llcms -ljpeg

BINARIES = dcraw clean_crw

all: $(BINARIES)

dcraw: dcraw.o
	${CC} $(LDFLAGS) -o dcraw dcraw.o

clean_crw: clean_crw.o
	${CC} -o clean_crw clean_crw.o

install: all
	test -x /usr/ccs/bin/strip && /usr/ccs/bin/strip $(BINARIES) 
	test -x /usr/ccs/bin/mcs && /usr/ccs/bin/mcs -d $(BINARIES)
	ginstall -D dcraw $(DESTDIR)$(myprefix)/bin/dcraw
	ginstall -D clean_crw $(DESTDIR)$(myprefix)/bin/clean_crw
	ginstall -D dcraw.1 $(DESTDIR)$(myprefix)/share/man/man1/dcraw.1

clean:
	rm -f *.o $(BINARIES)
