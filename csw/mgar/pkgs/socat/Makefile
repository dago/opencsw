GARNAME = socat
GARVERSION = 1.6.0.1
CATEGORIES = net

DESCRIPTION = Multipurpose relay for bidirectional data transfer
define BLURB
	socat is a relay for bidirectional data transfer between two independent data
	channels. Each of these data channels may be a file, pipe, device (serial line
	etc. or a pseudo terminal), a socket (UNIX, IP4, IP6 - raw, UDP, TCP), an
	SSL socket, proxy CONNECT connection, a file descriptor (stdin etc.), the GNU
	line editor (readline), a program, or a combination of two of these. 
	These modes include generation of "listening" sockets, named pipes, and pseudo
	terminals.
endef

MASTER_SITES = http://www.dest-unreach.org/socat/download/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWsocat,depend prototype)

DISTFILES += changelog.CSW

# Disable gcc specific options
PATCHFILES = cc_compile.patch

CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include ../category.mk


pre-configure:
	cd $(WORKSRC) && autoconf
	 @$(MAKECOOKIE)
