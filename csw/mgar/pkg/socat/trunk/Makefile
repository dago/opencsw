# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! Why does OPENSSL_TCP4 fail?
#
#     $ /opt/csw/bin/bash test.sh OPENSSL_TCP4
#     using temp directory /tmp/skayser/12533
#     test  60 OPENSSL_TCP4: openssl connect... FAILED: ./socat:
#     ./socat -t 0.1  exec:'openssl s_server -accept 12021 -quiet -cert testsrv.pem' pipe &
#     ./socat -t 0.1  - openssl:127.0.0.1:12021,pf=ip4,verify=0,
#     1d0
#     < test60 Fri Dec 10 00:48:32 CET 2010 31169
#
#   Client connections to listener service (pipe ^= echo) don't get an
#   immediate response (seems like data is stuck or procs exiting early).
#   Upon the 2nd or 3rd connection, input is usually echoed fine.
#   echo foo | openssl s_client -connect localhost:12021 -quiet -no_ign_eof
#
# * Send 0001 patch upstream, if you want to be 100% accurate you could
#   also ask why here strings (<<<) are used over here docs (<<EOM).
#   Solaris 9 bin bash doesn't support here strings.
#
NAME = socat
VERSION = 1.7.1.3
CATEGORIES = net
GARTYPE = v2

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

VENDOR_URL   = http://www.dest-unreach.org/socat/
MASTER_SITES = http://www.dest-unreach.org/socat/download/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz


RUNTIME_DEP_PKGS = CSWosslrt CSWreadline CSWtcpwrap

# test.sh uses unescaped nested double quotes (doesn't work with /bin/bash)
PATCHFILES += 0001-Escape-nested-double-quotes.patch

CONFIGURE_ARGS = $(DIRPATHS)

# 250+ tests take a while. Run them manually when packaging a new version.
# Note that test.sh tends to see advanced bash feature creep, don't bother
# getting them all working with /bin/bash, it's only the test suite.
#TEST_SCRIPTS = /opt/csw/bin/bash $(WORKSRC)/test.sh

# When you run the tests on a non IPV6 system you can set HAVENOT_IP6
# to shortcut some tests
#TEST_ENV="HAVENOT_IP6=1"

# socat 1.7.1.3: 
# --------------
# Running test.sh on an IPV6 system as non-root i get:
#
#   summary: 287 tests; 185 ok, 23 failed, 78 could not be performed
#
# The 23 FAILED ones are
#
# 60 OPENSSL_TCP4: openssl connect
# 126 PTMXWAITSLAVE: test if master pty (ptmx) waits for slave connection
# 214 UDP4SCM_IP_OPTIONS: UDP4 log ancillary message IP_OPTIONS options
# 216 UDP4SCM_IP_TTL: UDP4 log ancillary message IP_TTL
# 218 UDP4SCM_IP_PKTINFO: UDP4 log ancillary message IP_PKTINFO locaddr
# 219 UDP4SCM_IP_PKTINFO: UDP4 log ancillary message IP_PKTINFO dstaddr
# 220 UDP4SCM_IP_PKTINFO: UDP4 log ancillary message IP_PKTINFO
# 221 UDP4SCM_IP_RECVIF: UDP4 log ancillary message IP_RECVIF if
# 222 UDP4SCM_IP_RECVDSTADDR: UDP4 log ancillary message IP_RECVDSTADDR dstaddr
# 233 UDP6SCM_IPV6_PKTINFO: UDP6 log ancillary message IPV6_PKTINFO
# 234 UDP6SCM_IPV6_HOPLIMIT: UDP6 log ancillary message IPV6_HOPLIMIT hoplimit
# 243 SCTP4LISTENENV: SCTP4-LISTEN fills environment variables with socket addresses
# 244 SCTP6LISTENENV: SCTP6-LISTEN fills environment variables with socket addresses
# 246 UDP4ENV_IP_OPTIONS: UDP4 ancillary message brings IP_OPTIONS into env
# 248 UDP4ENV_IP_TTL: UDP4 ancillary message brings IP_TTL into environment
# 250 UDP4ENV_IP_LOCADDR: UDP4 ancillary message brings IP_LOCADDR into environment
# 251 UDP4ENV_IP_DSTADDR: UDP4 ancillary message brings IP_DSTADDR into environment
# 252 UDP4ENV_IP_IF: UDP4 ancillary message brings IP_IF into environment
# 253 UDP4ENV_IP_IF: UDP4 ancillary message brings IP_IF into environment
# 254 UDP4ENV_IP_DSTADDR: UDP4 ancillary message brings IP_DSTADDR into env
# 264 UDP6ENV_IPV6_DSTADDR: UDP6 ancillary message brings IPV6_DSTADDR into environment
# 265 UDP6ENV_IPV6_HOPLIMIT: UDP6 ancillary message brings IPV6_HOPLIMIT into environment
# 271 SOCKET_CONNECT_TCP6: socket connect with TCP/IPv6
# 281 SCTP4STREAM: echo via connection to SCTP V4 socket
# 282 SCTP6STREAM: echo via connection to SCTP V6 socket
# 
#
# Most of them relate to ancillary data. Seems as if there are two competing
# socket libraries on Solaris: 3SOCKET and 3XNET, where only the latter handles
# ancillary data.
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

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated: 
	ginstall -d $(DOCDEST)
	cp $(FILEDIR)/changelog.CSW $(FILEDIR)/README.CSW $(DOCDEST)
	@$(MAKECOOKIE)
