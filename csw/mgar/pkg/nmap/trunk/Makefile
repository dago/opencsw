NAME = nmap
VERSION = 5.21
CATEGORIES = net

DESCRIPTION = A network exploration tool and security/port scanner
define BLURB
  Nmap is a utility for network exploration or security auditing. It supports
  ping scanning (determine which hosts are up), many port scanning techniques
  (determine what services the hosts are offering), and TCP/IP fingerprinting
  (remote host OS or device identification). Nmap also offers flexible target
  and port specification, decoy/stealth scanning, sunRPC scanning, and more.
  Most Unix and Windows platforms are supported in both GUI and commandline
  modes.  Several popular handheld devices are also supported, including the
  Sharp Zaurus and the iPAQ.
endef

MASTER_SITES = http://nmap.org/dist/
DISTFILES = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

# Compile against gtk+-2.0 (2.4.0)
# PATCHFILES = gtk20.diff

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libpcre=$(prefix)
CONFIGURE_ARGS += --with-libpcap=$(prefix)
CONFIGURE_ARGS += --with-openssl=$(prefix)

#nmapdatadir=$(datadir)/nmap

#INSTALL_OVERRIDE_DIRS  = prefix exec_prefix bindir sbindir mandir
#INSTALL_OVERRIDE_DIRS += nmapdatadir deskdir

# No test suite for nmap
TEST_SCRIPTS =

include gar/category.mk

#pre-configure:
#	@( cd $(WORKSRC) ; autoconf )
#	@( cd $(WORKSRC)/nmapfe ; autoconf )
#	@$(MAKECOOKIE)
