GARNAME = alpine
GARVERSION = 2.00
CATEGORIES = apps

DESCRIPTION = Alpine Messaging System
define BLURB
	Alpine is a fast, easy to use email client that is suitable for both 
	the inexperienced email user as well as for the most demanding of power 
	users. Alpine is based on the Pine® Message System, which was also
   	developed at the University of Washington. Alpine can be learned by 
	exploration and the use of context-sensitive help. The user experience 
	is highly customizable through the use of the Alpine Setup command. 
endef

MASTER_SITES = http://www.washington.edu/alpine/
UPSTREAM_MASTER_SITES = ftp://ftp.cac.washington.edu/alpine/
DISTFILES  = $(GARNAME).tar.bz2

PACKAGES = CSWalpine
CATALOGNAME_CSWgd = alpine
SPKG_DESC_CSWgd = $(DESCRIPTION)

# We define upstream file regex so we can be notifed of new 
# upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

##  Needs gcc to compile imap support since ucbcc 
##  does not work on the buildfarm. GCC 4 does not work
##  GCC4 thows the following errors:
##  warning: pointer targets in passing argument 2 of 'compare_cstring' 
##           differ in signedness
GARCOMPILER = GCC3

# Patch for solaris explained in the following thread
# http://mailman2.u.washington.edu/pipermail/alpine-info/2007-December/000047.html
PATCHFILES = pubcookie.diff

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-quotas
CONFIGURE_ARGS += --enable-from-encoding
CONFIGURE_ARGS += --with-libiconv-prefix=$(prefix)
CONFIGURE_ARGS += --with-libintl-prefix=$(prefix)
CONFIGURE_ARGS += --with-pubcookie
CONFIGURE_ARGS += --with-system-pinerc=$(libdir)/pine.conf
CONFIGURE_ARGS += --with-system-fixed-pinercc=$(libdir)/pine.conf.fixed
CONFIGURE_ARGS += --with-ssl-dir=$(prefix)
CONFIGURE_ARGS += --with-krb5-dir=$(prefix)
CONFIGURE_ARGS += --with-ldap-dir=$(prefix)
CONFIGURE_ARGS += --with-tcl-lib=$(libdir)/tcl8.4
CONFIGURE_ARGS += --with-c-client-target=gso
CONFIGURE_ARGS += --with-web-bin=$(libexecdir)/alpine/bin

## Libs that are not get set correctly in Makefiles
LIBS += -lm -lgssapi_krb5 -lkrb5 -lintl -liconv
export LIBS

TEST_TARGET = check

include gar/category.mk
