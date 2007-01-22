myprefix?=/opt/csw
LDFLAGS+=-lm -llcms -ljpeg

all: dcraw

objs = dcraw.o

dcraw: $(objs)
	${CC} $(LDFLAGS) -o dcraw $(objs)

install: all
	test -x /usr/ccs/bin/strip && /usr/ccs/bin/strip dcraw
	test -x /usr/ccs/bin/mcs && /usr/ccs/bin/mcs -d dcraw
	ginstall -D dcraw $(DESTDIR)$(myprefix)/bin/dcraw
	ginstall -D dcraw.1 $(DESTDIR)$(myprefix)/share/man/man1/dcraw.1

clean:
	rm -f *.o dcraw
