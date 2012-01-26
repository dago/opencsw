# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = fakeroot
VERSION = 1.12.4
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = A fake root environment by means of LD_PRELOAD and SYSV IPC (or TCP) trickery.
define BLURB
  A fake root environment by means of LD_PRELOAD and SYSV IPC (or TCP) trickery.
endef

MASTER_SITES = http://ftp.debian.org/debian/pool/main/f/fakeroot/
DISTFILES  = $(NAME)_$(VERSION).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS = 

include gar/category.mk

# The ACL implemenatation in fakeroot doesn't work on solaris so remove it
pre-configure-modulated:
	@( cd $(WORKSRC); gsed -i -e 's%sys/acl.h%%' configure.ac; \
        autoreconf )
	@$(MAKECOOKIE) 

