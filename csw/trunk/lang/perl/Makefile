GARNAME = perl
GARVERSION = 5.8.7
CATEGORIES = lang

DESCRIPTION = A high-level, general-purpose programming language.
define BLURB
  Perl is a high-level, general-purpose programming language that makes easy
  things easy and hard things possible. It is optimized for scanning arbitrary
  text files and system administration. It has built-in extended regular
  expression matching and replacement, a dataflow mechanism to improve security
  with setuid scripts and is extendable via modules that can interface to C
  libraries.
endef

MASTER_SITES = $(CPAN_ROOT)/src/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWperl.gspec CSWperl.prototype CSWperl.depend
DISTFILES += CSWperldoc.gspec CSWperldoc.prototype CSWperldoc.depend

#LIBDEPS += lib/db lib/gdbm

# Custom configure
CONFIGURE_SCRIPTS = perl

# Compatable with all prior patch revs
INC_COMPAT = 5.8.0 5.8.2 5.8.4 5.8.6

# Configuration flags
CONFIGURE_ARGS += -Darchlib=$(libdir)/perl/$(GARVERSION)
CONFIGURE_ARGS += -Dccflags="$(CFLAGS)"
CONFIGURE_ARGS += -Dccversion="$(CC_VERSION)"
CONFIGURE_ARGS += -Dcf_email=$(SPKG_EMAIL)
CONFIGURE_ARGS += -Dinc_version_list="$(INC_COMPAT)"
CONFIGURE_ARGS += -Dldflags="$(LDFLAGS)"
CONFIGURE_ARGS += -Dlibperl=libperl.so.$(GARVERSION)
CONFIGURE_ARGS += -Dlocincpth=$(includedir)
CONFIGURE_ARGS += -Dloclibpth=$(libdir)
CONFIGURE_ARGS += -Dman1dir=$(mandir)/man1
CONFIGURE_ARGS += -Dman1ext=1
CONFIGURE_ARGS += -Dman3dir=$(mandir)/man3
CONFIGURE_ARGS += -Dman3ext=3perl
CONFIGURE_ARGS += -Doptimize="$(OPTFLAGS)"
CONFIGURE_ARGS += -Dperladmin="root@localhost"
CONFIGURE_ARGS += -Dprefix=$(prefix)
CONFIGURE_ARGS += -Dprivlib=$(datadir)/perl/$(GARVERSION)
CONFIGURE_ARGS += -Dsitearch=$(libdir)/perl/site_perl
CONFIGURE_ARGS += -Dsitelib=$(datadir)/perl/site_perl
CONFIGURE_ARGS += -Dsiteman1dir=$(mandir)/man1
CONFIGURE_ARGS += -Dsiteman3dir=$(mandir)/man3
CONFIGURE_ARGS += -Dsiteprefix=/usr
CONFIGURE_ARGS += -Duselargefiles
CONFIGURE_ARGS += -Duseshrplib
CONFIGURE_ARGS += -Dusesitecustomize
CONFIGURE_ARGS += -Dusethreads
CONFIGURE_ARGS += -Dvendorarch=$(libdir)/perl/csw
CONFIGURE_ARGS += -Dvendorlib=$(datadir)/perl/csw
CONFIGURE_ARGS += -Dvendorprefix=$(prefix)

# Tests take a long time
ENABLE_TEST = 0

include ../category.mk

# How to configure Perl
configure-perl:
	@(cd $(WORKSRC) ; $(CONFIGURE_ENV) ./Configure $(CONFIGURE_ARGS) -des)
	@$(MAKECOOKIE)

# Make links to libperl
LIB_MINOR = $(shell echo $(GARVERSION) | cut -f1-2 -d.)
LIB_PATH  = $(libdir)/perl/$(GARVERSION)/CORE
post-install:
	@( cd $(DESTDIR)$(libdir) ; \
		mv $(DESTDIR)$(LIB_PATH)/libperl.so.$(GARVERSION) \
		$(DESTDIR)$(libdir) ; \
		chmod 755 $(DESTDIR)$(libdir)/libperl.so.$(GARVERSION) ; \
		ln -s libperl.so.$(GARVERSION) libperl.so.$(LIB_MINOR) ; \
		ln -s libperl.so.$(GARVERSION) libperl.so )
	@$(MAKECOOKIE)

