GARNAME = perl
GARVERSION = 5.8.6
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

# Configuration flags
CONFIGURE_ARGS += -Dprefix=$(prefix)
CONFIGURE_ARGS += -Doptimize="$(OPTFLAGS)"
CONFIGURE_ARGS += -Dccflags="$(CFLAGS)"
CONFIGURE_ARGS += -Dldflags="$(LDFLAGS)"
CONFIGURE_ARGS += -Dloclibpth=$(libdir)
CONFIGURE_ARGS += -Dlocincpth=$(includedir)
CONFIGURE_ARGS += -Dinc_version_list="5.8.0 5.8.2 5.8.4"
CONFIGURE_ARGS += -Dccversion="$(CC_VERSION)"
CONFIGURE_ARGS += -Duselargefiles
CONFIGURE_ARGS += -Dusethreads
CONFIGURE_ARGS += -Dprivlib=$(libdir)/perl/$(GARVERSION)
CONFIGURE_ARGS += -Darchlib=$(libdir)/perl/$(GARVERSION)
CONFIGURE_ARGS += -Dvendorprefix=$(prefix)
CONFIGURE_ARGS += -Dvendorlib=$(datadir)/perl/csw
CONFIGURE_ARGS += -Dvendorarch=$(datadir)/perl/csw
CONFIGURE_ARGS += -Dsiteprefix=$(prefix)
CONFIGURE_ARGS += -Dsitelib=$(datadir)/perl/csw
CONFIGURE_ARGS += -Dsitearch=$(datadir)/perl/csw
CONFIGURE_ARGS += -Dman1dir=$(mandir)/man1
CONFIGURE_ARGS += -Dman3dir=$(mandir)/man3
CONFIGURE_ARGS += -Dsiteman1dir=$(mandir)/man1
CONFIGURE_ARGS += -Dsiteman3dir=$(mandir)/man3

include ../category.mk

# How to configure Perl
configure-perl:
	@(cd $(WORKSRC) ; $(CONFIGURE_ENV) ./Configure $(CONFIGURE_ARGS) -des)
	@$(MAKECOOKIE)
