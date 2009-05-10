GARNAME = socat
GARVERSION = 1.7.1.1
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

SPKG_SOURCEURL = http://www.dest-unreach.org/socat/

REQUIRED_PKGS = CSWosslrt CSWreadline CSWtcpwrap

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Delete or substitute gcc specific options (-Wall, -Werror, -O0)
PATCHFILES = cc_compile.patch
# Amend AC_CHECK_HEADERS check on netinet/ip.h with req. system headers
PATCHFILES += patch-configure-netinetip.diff
# Fix some broken tests (pending to push some of it upstream)
PATCHFILES += patch-test.diff
# Include utils.h in sycls.c so that setenv() is declared
PATCHFILES += patch-sycls-utils.diff

CONFIGURE_ARGS = $(DIRPATHS)

# 250+ tests take a while. Run them manually when packaging a new version.
# To do so, change to $(WORKSRC) after building and execute ./test.sh
TEST_SCRIPTS =

# When you run the tests on a non IPV6 system you can set HAVENOT_IP6
# to shortcut some tests
#TEST_ENV="HAVENOT_IP6=1"

# socat 1.7.1.1: 
# --------------
# Running test.sh on a non IPV6 system as root i get:
#
#   summary: 282 tests; 145 ok, 8 failed, 129 could not be performed
#
# The 8 FAILED ones are
#
# 126 PTMXWAITSLAVE: test if master pty (ptmx) waits for slave connection
# 214 UDP4SCM_IP_OPTIONS: UDP4 log ancillary message IP_OPTIONS options
# 221 UDP4SCM_IP_RECVIF: UDP4 log ancillary message IP_RECVIF if
# 222 UDP4SCM_IP_RECVDSTADDR: UDP4 log ancillary message IP_RECVDSTADDR dstaddr
# 246 UDP4ENV_IP_OPTIONS: UDP4 ancillary message brings IP_OPTIONS into env
# 248 UDP4ENV_IP_TTL: UDP4 ancillary message brings IP_TTL into environment
# 253 UDP4ENV_IP_IF: UDP4 ancillary message brings IP_IF into environment
# 254 UDP4ENV_IP_DSTADDR: UDP4 ancillary message brings IP_DSTADDR into env
#
# Most of them (all of them?) relate to ancillary data. Seems as if there are
# two competing socket libraries on Solaris: 3SOCKET and 3XNET, where only the
# latter handles ancillary data.
#
# http://www.mail-archive.com/networking-discuss@opensolaris.org/msg01146.html
#
# 3XNET is only defined when using SUS/XPG4v2 feature macros. socat README 
# suggests
#
#   EXTRA_CFLAGS = -D_XPG4_2 -D__EXTENSIONS__
#
# However, when compiling with these flags the above tests still fail.
# Might well be that the ancillary data handling within socat is not
# coded to work on Solaris.
#
# As a matter of fact, the socat man page even points out that some of
# the address options related to ancillary data are restricted to
# specific platforms (see IP4 and IP6 option groups).

# Note to self: standards(5) says something like the following for XPG4v2
#EXTRA_CFLAGS = -D_XOPEN_SOURCE=1 -D_XOPEN_SOURCE_EXTENDED=1 -D__EXTENSIONS__
#EXTRA_LDFLAGS = -lxnet

# Individual tests can be run by changing to $(WORKSRC) and running
#
#   ./test.sh <TESTNAME>
#
# where TESTNAME is one of the uppercase testnames from above 
# (for example PTMXWAITSLAVE).

include gar/category.mk

# Run autoconf to re-evaulate the patched configure.in / Makefile.in
pre-configure-modulated:
	cd $(WORKSRC) && autoconf
	 @$(MAKECOOKIE)

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated: 
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(FILEDIR)/README.CSW $(DOCDEST)
	@$(MAKECOOKIE)
