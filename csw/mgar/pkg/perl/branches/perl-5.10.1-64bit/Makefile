NAME = perl
VERSION = 5.10.1
CATEGORIES = lang

DESCRIPTION = A high-level, general-purpose programming language
define BLURB
  Perl is a high-level, general-purpose programming language that makes easy
  things easy and hard things possible. It is optimized for scanning arbitrary
  text files and system administration. It has built-in extended regular
  expression matching and replacement, a dataflow mechanism to improve security
  with setuid scripts and is extendable via modules that can interface to C
  libraries.
endef

MASTER_SITES   = http://www.cpan.org/src/
SPKG_SOURCEURL = http://www.cpan.org/src

DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES += CSWperl
SPKG_DESC_CSWperl = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWperl += CSWbdb48
RUNTIME_DEP_PKGS_CSWperl += CSWlibgdbm3

PACKAGES += CSWperldoc
SPKG_DESC_CSWperldoc = Perl documentation
PKGFILES_CSWperldoc = .*\/pod\/.*\.pod .*\/man\/man.\/.*
ARCHALL_CSWperldoc = 1
INCOMPATIBLE_PKGS_CSWperl += CSWperlmods
INCOMPATIBLE_PKGS_CSWperl += CSWpmdigest
INCOMPATIBLE_PKGS_CSWperl += CSWpmi18nlangtags

# The diagnostics.pm module needs the podfile to output its messages.
# That means it must be included in the main package, not the docs.
EXTRA_PKGFILES_EXCLUDED_CSWperldoc = .*\/perldiag.pod
EXTRA_PKGFILES_INCLUDED_CSWperl = .*\/perldiag.pod

LICENSE = Copying

PATCHFILES += 0001-change-inc-based-on-rhel5-patch.patch

# CHECKPKG_OVERRIDES_CSWperl += surplus-dependency|CSWgdbm
# CHECKPKG_OVERRIDES_CSWperl += soname-not-found|libgdbm.so.3|is|needed|by|opt/csw/lib/perl/5.10.1/auto/GDBM_File/GDBM_File.so

# Core module updates
# Not used at the moment, leave one as example
#MASTER_SITES  += $(CPAN_FIRST_MIRROR)/S/SM/SMUELLER/
#CORE_UPDATES  += PathTools-3.30z
#CORE_OBSOLETE += Cwd.pm File/Spec* auto/Cwd

DISTFILES += $(foreach N,$(CORE_UPDATES),$(N).tar.gz)

BUILD64 = 1
NOISAEXEC = 1

# Custom configure
CONFIGURE_SCRIPTS = perl

# Compatable with all prior patch revs
INC_COMPAT = 5.8.0 5.8.2 5.8.4 5.8.6 5.8.7 5.8.8 5.10.0

# Force use of db-4.8
# TBD: Take out libperl.so, see below.
PERL_LIBS-32 += -lsocket -lnsl -lgdbm -ldb-4.8 -ldl -lm -lpthread -lc -lperl
PERL_LIBS-64 += -lsocket -lnsl -lgdbm -ldb-4.8 -ldl -lm -lpthread -lc
PERL_LIBS = $(PERL_LIBS-$(MEMORYMODEL))

# TBD: 64 bit pathes
#     ld='/opt/SUNWspro/bin/cc', ldflags ='-m64 -xarch=sparc -L/opt/csw/bdb48/lib/64 -L/opt/csw/lib/64 -L/usr/lib -L/usr/ccs/lib -L/lib -xarch=v9'

# /usr/lib -> /usr/lib/64
# /usr/ccs/lib -> /usr/ccs/lib/sparcv9
# /lib -> /lib/64

#    libpth=/usr/lib /usr/ccs/lib /lib /opt/csw/lib/64
#    libs=-lsocket -lnsl -lgdbm -ldb-4.8 -ldl -lm -lpthread -lc
#    perllibs=-lsocket -lnsl -ldb-4.8 -ldl -lm -lpthread -lc
#    libc=/usr/lib/sparcv9/libc.so, so=so, useshrplib=true, libperl=libperl.so.5.10.1
#    gnulibc_version=''
#  Dynamic Linking:
#    dlsrc=dl_dlopen.xs, dlext=so, d_dlsymun=undef, ccdlflags='-R /opt/csw/lib/64'
#    cccdlflags='-KPIC', lddlflags='-G -xarch=v9 -L/opt/csw/bdb48/lib/64 -L/opt/csw/lib/64 -L/usr/lib -L/usr/ccs/lib -L/lib'

# Configuration flags
CONFIGURE_ARGS += -Darchlib=$(libdir)/perl/$(VERSION)
CONFIGURE_ARGS += -Dcc=$(CC)
CONFIGURE_ARGS += -Dccflags="$(CFLAGS)"
CONFIGURE_ARGS += -Dccversion="$(CC_VERSION)"
CONFIGURE_ARGS += -Dcf_email=$(SPKG_EMAIL)
CONFIGURE_ARGS += -Dinc_version_list="$(INC_COMPAT)"
CONFIGURE_ARGS += -Dld=$(CC)
CONFIGURE_ARGS += -Dldflags="$(LDFLAGS)"
CONFIGURE_ARGS += -Dlibperl=libperl.so.$(VERSION)
CONFIGURE_ARGS += -Dlocincpth=$(includedir)
CONFIGURE_ARGS += -Dloclibpth=$(libdir)
CONFIGURE_ARGS += -Dman1dir=$(mandir)/man1
CONFIGURE_ARGS += -Dman1ext=1
CONFIGURE_ARGS += -Dman3dir=$(mandir)/man3
CONFIGURE_ARGS += -Dman3ext=3perl
CONFIGURE_ARGS += -Doptimize="$(OPTFLAGS)"
CONFIGURE_ARGS += -Dperladmin="root@localhost"
CONFIGURE_ARGS += -Dprefix=$(prefix)
CONFIGURE_ARGS += -Dbin=$(bindir)
CONFIGURE_ARGS += -Dscriptdir=$(bindir)
CONFIGURE_ARGS += -Dprivlib=$(datadir)/perl/$(VERSION)
CONFIGURE_ARGS += -Dsitearch=$(libdir)/perl/site_perl
CONFIGURE_ARGS += -Dsitelib=$(datadir)/perl/site_perl
CONFIGURE_ARGS += -Dsiteman1dir=$(mandir)/man1
CONFIGURE_ARGS += -Dsiteman3dir=$(mandir)/man3
CONFIGURE_ARGS += -Dsiteprefix=/usr
CONFIGURE_ARGS += -Duseshrplib
CONFIGURE_ARGS += -Dusesitecustomize
CONFIGURE_ARGS += -Dusethreads
#CONFIGURE_ARGS += -Dusedtrace
CONFIGURE_ARGS += -Dvendorarch=$(libdir)/perl/csw
CONFIGURE_ARGS += -Dvendorlib=$(datadir)/perl/csw
CONFIGURE_ARGS += -Dvendorprefix=$(prefix)
CONFIGURE_ARGS += -Dlibs="$(PERL_LIBS)"
CONFIGURE_ARGS += -Dlibsdirs=" /usr/lib $(libdir)"
CONFIGURE_ARGS += -Dsed=$(bindir)/gsed

# On 64 bit there are no largefile issues and the definition disturbs other builds (like NetSNMP embeddded Perl)
CONFIGURE_ARGS-32 += -Duselargefiles
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

EXTRA_LIB += $(prefix)/bdb48/lib
EXTRA_INC += $(prefix)/bdb48/include

# Somehow the CPPFLAGS do not make it into the compile environment.
# Add them explicitly here, otherwise specifically the bdb48/include will
# not make it resulting in db.h not to be found and DB_File.pm not to be built
# as reported here:
#   https://www.opencsw.org/mantis/view.php?id=4544
EXTRA_CFLAGS = $(CPPFLAGS)

# Adding -lperl requires that libperl.so is available during compilation, which is not
# the case on bootstrapping. However, we require explicit libperl linkage or programs
# embedding perl will have problems with duplicated static variables.
# XXX Investigate further after 64 bit has built
EXTRA_LDFLAGS-32 = -L$(libdir) -lperl
EXTRA_LDFLAGS += $(EXTRA_LDFLAGS-$(MEMORYMODEL))

# Tests take a long time
SKIPTEST ?= 1

# Make sure we don't include the path to the newly built perl as the
# library is not in place yet.
IGNORE_DESTDIR = 1

EXTRA_MERGE_EXCLUDE_FILES = .*\/perllocal.pod

# Do not exclude static libs as at least DynaLoader.a is needed for XS compilation
MERGE_EXCLUDE_STATICLIBS =

# Splitting of a separate libperl.so requires more work and careful planning.
# Override for now.
CHECKPKG_OVERRIDES_CSWperl += shared-lib-pkgname-mismatch|file=opt/csw/lib/libperl.so.5.10.1|soname=libperl.so.5.10.1|pkgname=CSWperl|expected=CSWlibperl5-10-1
CHECKPKG_OVERRIDES_CSWperl += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libperl.so

include gar/category.mk

# This is probably due to -lperl, but during Configure the one in /opt/csw/lib is picked up and
# the one in $WORKSRC has not been built yet
# TBD: Investigate
post-extract-modulated:
	mkdir -p $(WORKSRC)
	gln -s libperl.so.5.10.1 $(WORKSRC)/libperl.so
	@$(MAKECOOKIE)

ifneq ($(CORE_UPDATES),)
POST_TARGETS = install-core-updates
include files/updatecore.mk
endif

# How to configure Perl
configure-perl:
	@(cd $(WORKSRC) ; $(CONFIGURE_ENV) ./Configure $(CONFIGURE_ARGS) -des)
	@$(MAKECOOKIE)

# Make links to libperl
POST_TARGETS += libperl
LIB_MINOR = $(shell echo $(VERSION) | cut -f1-2 -d.)
LIB_PATH  = $(libdir)/perl/$(VERSION)/CORE
libperl:
	@( cd $(DESTDIR)$(libdir) ; \
		mv $(DESTDIR)$(LIB_PATH)/libperl.so.$(VERSION) \
		$(DESTDIR)$(libdir) ; \
		chmod 755 $(DESTDIR)$(libdir)/libperl.so.$(VERSION) ; \
		ln -s libperl.so.$(VERSION) libperl.so.$(LIB_MINOR) ; \
		ln -s libperl.so.$(VERSION) libperl.so )
	@$(MAKECOOKIE)
#	echo YOUAREHERE
#	( cd $(DESTDIR)$(libdir)/perl/$(VERSION)/${TARGET}/CORE ; \
#	   chmod 755 libperl.so.$(VERSION) ; \
#	   rm libperl.so.$(LIB_MINOR) libperl.so ; \
#	   ln -s libperl.so.$(VERSION) libperl.so.$(LIB_MINOR) ; \
#	   ln -s libperl.so.$(VERSION) libperl.so )
#	( cd $(DESTDIR)$(libdir)/perl/$(VERSION)/${TARGET} ; \
#	   rm libperl* ; \
#	   ln -s CORE/libperl.so.$(VERSION) libperl.so.$(VERSION) ; \
#	   ln -s CORE/libperl.so.$(VERSION) libperl.so.$(LIB_MINOR) ; \
#	   ln -s CORE/libperl.so.$(VERSION) libperl.so )
#	$(MAKECOOKIE)

# Remove build paths from Config
POST_TARGETS += perlconf
perlconf:
	@( cd $(DESTDIR)$(libdir)/perl/$(VERSION) ; \
        /bin/perl -i -lne "\
            next if /config_arg[1-9]/; \
            s/^config_args=.+$$/config_args=''/; \
            s/^config_argc=.+$$/config_argc='0'/; \
            s,-I$(DESTDIR)$(includedir),,g; \
            s,-[LR]$(DESTDIR)$(libdir),,g; \
            s,( -I$(includedir))+,\$$1,g; \
            s,( -[LR]$(libdir))+,\$$1,g; \
            s,-R $(libdir)/perl/$(VERSION)/CORE,-R $(libdir),; \
            s, (-L)?$(CC_HOME)\S+,,g; \
            if (/^\w+=/) { \
                s/\s{2,}(\-)/ \-/g; \
                s/(^\w+=.) /\$$1/; \
                s/ (.)$$/\$$1/g; \
            } \
            print \
        " Config.pm Config_heavy.pl )
	@$(MAKECOOKIE)

# Invoke post-install targets
post-install-modulated: $(POST_TARGETS)
	@$(MAKECOOKIE)
