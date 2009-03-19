GARNAME = socat
GARVERSION = 1.7.0.0
CATEGORIES = net

DESCRIPTION = Multipurpose relay for bidirectional data transfer
define BLURB
	socat is a relay for bidirectional data transfer between two independent
	data channels. Each of these data channels may be a file, pipe, device
	(serial line etc. or a pseudo terminal), a socket (UNIX, IP4, IP6 - raw,
	UDP, TCP), an SSL socket, proxy CONNECT connection, a file descriptor
	(stdin etc.), the GNU line editor (readline), a program, or a
	combination of two of these.  These modes include generation of
	"listening" sockets, named pipes, and pseudo terminals.
endef

MASTER_SITES = http://www.dest-unreach.org/socat/download/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += changelog.CSW

SPKG_SOURCEURL = http://www.dest-unreach.org/socat/

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Disable gcc specific options
PATCHFILES = cc_compile.patch

CONFIGURE_ARGS = $(DIRPATHS)

# 200+ tests take a while. Run them manually when packaging a new version
TEST_SCRIPTS =

EXTRA_EXCLUDE_FILES = $(bindir)/procan $(bindir)/filan

include gar/category.mk

# Run autoconf to re-evaulate the patched configure.in / Makefile.in
pre-configure-modulated:
	cd $(WORKSRC) && autoconf
	 @$(MAKECOOKIE)
