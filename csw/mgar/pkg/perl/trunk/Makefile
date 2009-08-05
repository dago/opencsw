GARNAME = perl
GARVERSION = 5.8.8
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

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWperl CSWperldoc
ARCHALL_CSWperldoc = 1
#REQUIRED_PKGS_CSWperl = CSWbdb44 CSWgdbm
REQUIRED_PKGS_CSWperl = CSWbdb CSWgdbm
REQUIRED_PKGS_CSWperldoc = CSWperl

# Core module updates
MASTER_SITES  += $(CPAN_FIRST_MIRROR)/S/SM/SMUELLER/
CORE_UPDATES  += PathTools-3.30
CORE_OBSOLETE += Cwd.pm File/Spec* auto/Cwd

MASTER_SITES  += $(CPAN_FIRST_MIRROR)/L/LD/LDS/
CORE_UPDATES  += CGI.pm-3.44
CORE_OBSOLETE += CGI*

MASTER_SITES  += $(CPAN_FIRST_MIRROR)/M/MS/MSCHWERN/
CORE_UPDATES  += Test-Simple-0.92
CORE_OBSOLETE += Test/Builder* Test/More.pm Test/Simple.pm Test/Tutorial.pm

MASTER_SITES  += $(CPAN_FIRST_MIRROR)/T/TJ/TJENNESS/
CORE_UPDATES  += File-Temp-0.22
CORE_OBSOLETE += File/Temp.pm

MASTER_SITES  += $(CPAN_FIRST_MIRROR)/G/GB/GBARR/
CORE_UPDATES  += IO-1.25
CORE_OBSOLETE += IO/Socket* IO/IO* IO/Socket.pm IO/Select.pm IO/Seekable.pm IO/Poll.pm IO/Pipe.pm IO/Handle.pm IO/File.pm IO/Dir.pm IO.pm

MASTER_SITES  += $(CPAN_FIRST_MIRROR)/A/AM/AMS/
CORE_UPDATES  += Storable-2.20
CORE_OBSOLETE += Storable/* Storable.pm

DISTFILES += $(foreach N,$(CORE_UPDATES),$(N).tar.gz)

# Dependencies
#LIBDEPS += lib/bdb44
LIBDEPS += lib/bdb47
LIBDEPS += lib/gdbm

# Custom configure
CONFIGURE_SCRIPTS = perl

# Compatable with all prior patch revs
PL_MAJOR   = 5.10
PL_PATCH   = 0
INC_COMPAT = $(foreach REV,$(PL_PATCH),$(PL_MAJOR).$(REV))

# Force use of db-4.4
#PERL_LIBS += -lsocket -lnsl -lgdbm -ldb-4.4 -ldl -lm -lpthread -lc
# Force use of db-4.7
PERL_LIBS += -lsocket -lnsl -lgdbm -ldb-4.7 -ldl -lm -lpthread -lc -lperl

# Configuration flags
CONFIGURE_ARGS += -Darchlib=$(libdir)/perl/$(GARVERSION)
CONFIGURE_ARGS += -Dcc=$(CC)
CONFIGURE_ARGS += -Dccflags="$(CFLAGS)"
CONFIGURE_ARGS += -Dccversion="$(CC_VERSION)"
CONFIGURE_ARGS += -Dcf_email=$(SPKG_EMAIL)
CONFIGURE_ARGS += -Dinc_version_list="$(INC_COMPAT)"
CONFIGURE_ARGS += -Dld=$(CC)
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
CONFIGURE_ARGS += -Dlibs="$(PERL_LIBS)"
#CONFIGURE_ARGS += -Dlibsdirs=" /usr/lib /opt/csw/bdb44/lib /opt/csw/lib"
CONFIGURE_ARGS += -Dlibsdirs=" /usr/lib /opt/csw/lib"
CONFIGURE_ARGS += -Dsed=$(bindir)/gsed

#EXTRA_LIB += $(prefix)/bdb44/lib
#EXTRA_INC += $(prefix)/bdb44/include

EXTRA_MERGE_EXCLUDE_FILES = perllocal.pod
PKGFILES_CSWperldoc = $(PKGFILES_DOC)

# Tests take a long time
TEST_SCRIPTS =

include gar/category.mk
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
LIB_MINOR = $(shell echo $(GARVERSION) | cut -f1-2 -d.)
LIB_PATH  = $(libdir)/perl/$(GARVERSION)/CORE
libperl:
	@( cd $(DESTDIR)$(libdir) ; \
		mv $(DESTDIR)$(LIB_PATH)/libperl.so.$(GARVERSION) \
		$(DESTDIR)$(libdir) ; \
		chmod 755 $(DESTDIR)$(libdir)/libperl.so.$(GARVERSION) ; \
		ln -s libperl.so.$(GARVERSION) libperl.so.$(LIB_MINOR) ; \
		ln -s libperl.so.$(GARVERSION) libperl.so )
	@$(MAKECOOKIE)
#	echo YOUAREHERE
#	( cd $(DESTDIR)$(libdir)/perl/$(GARVERSION)/${TARGET}/CORE ; \
#	   chmod 755 libperl.so.$(GARVERSION) ; \
#	   rm libperl.so.$(LIB_MINOR) libperl.so ; \
#	   ln -s libperl.so.$(GARVERSION) libperl.so.$(LIB_MINOR) ; \
#	   ln -s libperl.so.$(GARVERSION) libperl.so )
#	( cd $(DESTDIR)$(libdir)/perl/$(GARVERSION)/${TARGET} ; \
#	   rm libperl* ; \
#	   ln -s CORE/libperl.so.$(GARVERSION) libperl.so.$(GARVERSION) ; \
#	   ln -s CORE/libperl.so.$(GARVERSION) libperl.so.$(LIB_MINOR) ; \
#	   ln -s CORE/libperl.so.$(GARVERSION) libperl.so )
#	$(MAKECOOKIE)

# Remove build paths from Config
POST_TARGETS += perlconf
perlconf:
	@( cd $(DESTDIR)$(libdir)/perl/$(GARVERSION) ; \
        /bin/perl -i -lne "\
            next if /config_arg[1-9]/; \
            s/^config_args=.+$$/config_args=''/; \
            s/^config_argc=.+$$/config_argc='0'/; \
            s,-I$(DESTDIR)$(includedir),,g; \
            s,-[LR]$(DESTDIR)$(libdir),,g; \
            s,( -I$(includedir))+,\$$1,g; \
            s,( -[LR]$(libdir))+,\$$1,g; \
            s,-R $(libdir)/perl/$(GARVERSION)/CORE,-R $(libdir),; \
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
#post-install: $(POST_TARGETS)
post-install-modulated: $(POST_TARGETS)
	echo $(DESTDIR)
	@rm $(DESTDIR)/opt/csw/lib/perl/5.8.8/perllocal.pod
	@$(MAKECOOKIE)
