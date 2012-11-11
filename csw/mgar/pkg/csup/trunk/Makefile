NAME = csup
VERSION = snap
PATCHLEVEL = 20060318
GARTYPE = v2

DESCRIPTION = A replacement for CVSup
define BLURB
  A solid replacement for CVSup for checkout-only functionality.
endef

MASTER_SITES = http://www.mu.org/~mux/
DISTFILES  = $(NAME)-$(VERSION)-$(PATCHLEVEL).tgz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

LICENSE = LICENSE

CONFIGURE_ARGS = $(DIRPATHS)

# PATH=$PATH:/opt/csw/bin gmake \
#	CC=/opt/studio/SOS12/SUNWspro/bin/cc \
#	WARNS= \
#	PREFIX=/opt/csw \
#	LEX=/opt/csw/bin/flex \
#	YACC=/opt/csw/bin/bison \
#	CFLAGS="-I/usr/include -I/opt/csw/include -features=extensions -D_POSIX_PTHREAD_SEMANTICS" \
#	LDFLAGS="-R/usr/ucblib -R/opt/csw/lib -L/opt/csw/lib -lcrypto -lz -lsocket -lnsl -L/usr/ucblib -lucb"

include gar/category.mk
