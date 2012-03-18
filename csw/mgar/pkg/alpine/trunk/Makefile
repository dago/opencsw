NAME = alpine
VERSION = 2.00
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Alpine Messaging System
define BLURB
	Alpine is a fast, easy to use email client that is suitable for both 
	the inexperienced email user as well as for the most demanding of power 
	users. Alpine is based on the Pine® Message System, which was also
	developed at the University of Washington. Alpine can be learned by 
	exploration and the use of context-sensitive help. The user experience 
	is highly customizable through the use of the Alpine Setup command. 
endef

MASTER_SITES = ftp://ftp.cac.washington.edu/alpine/
SPKG_SOURCEURL = http://www.washington.edu/alpine/
DISTFILES  = $(NAME).tar.bz2

PACKAGES = CSWalpine
CATALOGNAME_CSWalpine = alpine
SPKG_DESC_CSWalpine = $(DESCRIPTION)
OBSOLETED_BY_CSWalpine = CSWpine

# We define upstream file regex so we can be notifed of new 
# upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

##  Needs gcc to compile imap support since ucbcc 
##  does not work on the buildfarm. GCC 4 does not work
##  GCC4 thows the following errors:
##  warning: pointer targets in passing argument 2 of 'compare_cstring' 
##           differ in signedness
GARCOMPILER = GCC4

# Patch for solaris explained in the following thread
# http://mailman2.u.washington.edu/pipermail/alpine-info/2007-December/000047.html
PATCHFILES = pubcookie.diff

NOISALIST = 1
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-quotas
CONFIGURE_ARGS += --enable-from-encoding
CONFIGURE_ARGS += --with-libiconv-prefix=/opt/csw
CONFIGURE_ARGS += --with-libintl-prefix=/opt/csw
CONFIGURE_ARGS += --with-system-pinerc=$(prefix)/etc/pine.conf
CONFIGURE_ARGS += --with-system-fixed-pinercc=$(prefix)/etc/pine.conf.fixed
CONFIGURE_ARGS += --with-ssl-dir=/opt/csw
CONFIGURE_ARGS += --with-krb5-dir=/opt/csw
CONFIGURE_ARGS += --with-ldap-dir=/opt/csw
CONFIGURE_ARGS += --with-tcl-lib=/opt/csw/lib/tcl8.4
CONFIGURE_ARGS += --with-c-client-target=gso
CONFIGURE_ARGS += --with-pubcookie
CONFIGURE_ARGS += --with-web-bin=$(libexecdir)/alpine/bin
CONFIGURE_ARGS += --with-spellcheck-prog=$(bindir)/aspell

## Libs that are not get set correctly in Makefiles
EXTRA_LDFLAGS += -lm -lgssapi_krb5 -lkrb5 -lintl -liconv

RUNTIME_DEP_PKGS  = CSWggettextrt CSWiconv CSWtcl CSWsasl CSWosslrt
RUNTIME_DEP_PKGS += CSWkrb5lib CSWlibnet CSWncurses CSWoldaprt

include gar/category.mk

PI_SCRIPTS  = cleanup-web
PI_SCRIPTS += install-mlock
PI_SCRIPTS += install-web
PI_SCRIPTS += install-pine-symlink

post-install-modulated: $(PI_SCRIPTS)

install-pine-symlink:
	@(echo "==> Installing the pine symlink")
	@(cd $(DESTDIR)/$(bindir); ln -s alpine pine)
	@$(MAKECOOKIE)

install-mlock:
	@(echo "==> Installing mlock")
	(ginstall -d $(DESTDIR)$(sbindir))
	@(gcp $(WORKSRC)/imap/mlock/mlock $(DESTDIR)$(sbindir))
	@$(MAKECOOKIE)

cleanup-web:
	@(grm -fr $(DESTDIR)/home)

install-web:
	@(echo "==> Installing Web Interface")
	@(ginstall -d $(DESTDIR)$(libexecdir)/alpine-2.00)
	@(gcp -R $(WORKSRC)/web/* $(DESTDIR)$(libexecdir)/alpine-2.00)
	@(gcp $(WORKSRC)/web/src/pubcookie/wp_gssapi_proxy \
		$(DESTDIR)$(libexecdir)/alpine-2.00/bin)
	@(gcp $(WORKSRC)/web/src/pubcookie/wp_tclsh \
		$(DESTDIR)$(libexecdir)/alpine-2.00/bin)
	@(gcp $(WORKSRC)/web/src/pubcookie/wp_uidmapper \
		$(DESTDIR)$(libexecdir)/alpine-2.00/bin)
	@(gcp $(WORKSRC)/web/src/pubcookie/wp_umc \
		$(DESTDIR)$(libexecdir)/alpine-2.00/bin)
	@(gcp $(WORKSRC)/web/src/pubcookie/debug.cgi \
		$(DESTDIR)$(libexecdir)/alpine-2.00/bin)
	@(grm -fr $(DESTDIR)$(libexecdir)/alpine-2.00/src)
	@(grm -f $(DESTDIR)$(libexecdir)/alpine-2.00/bin/tclsh)
	@(gln -s $(bindir)/tclsh  \
		$(DESTDIR)$(libexecdir)/alpine-2.00/bin/tclsh)
	@(cd $(DESTDIR)$(libexecdir); gln -s ./alpine-2.00 ./alpine)



