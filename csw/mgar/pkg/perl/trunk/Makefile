NAME = perl
VERSION = 5.16.2
#CATEGORIES = lang
CATEGORIES = lang
GARTYPE = v2

DESCRIPTION = A high-level, general-purpose programming language
define BLURB
  Perl is a high-level, general-purpose programming language that makes easy
  things easy and hard things possible. It is optimized for scanning arbitrary
  text files and system administration. It has built-in extended regular
  expression matching and replacement, a dataflow mechanism to improve security
  with setuid scripts and is extendable via modules that can interface to C
  #MASTER_SITES   = http://www.cpan.org/src/
#SPKG_SOURCEURL = http://www.cpan.org/src
MASTER_SITES = manual://
DISTFILES  = $(NAME)-$(VERSION)-patched.tar.gz

# Make extra Solaris 10 package with DTrace support
#PACKAGING_PLATFORMS  = solaris9-sparc solaris9-i386
#PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386
PACKAGING_PLATFORMS += solaris10-sparc

PACKAGES                 += CSWperl
SPKG_DESC_CSWperl         = $(DESCRIPTION)
#RUNTIME_DEP_PKGS_CSWperl  = CSWbdb48 CSWlibgdbm4
RUNTIME_DEP_PKGS_CSWperl  = Wbdb48 CSWlibgdbm4
INCOMPATIBLE_PKGS_CSWperl = CSWperlmods CSWpmdigest CSWpmi18nlangtags

PACKAGES                   += CSWperldoc
SPKG_DESC_CSWperldoc        = Perl documentation
RUNTIME_DEP_PKGS_CSWperldoc = CSWperl
ARCHALL_CSWperldoc          = 1

LICENSE = Copying

CHECKPKG_OVERRIDES_CSWperl    += file-with-bad-content
CHECKPKG_OVERRIDES_CSWperldoc += file-with-bad-content
CHECKPKG_OVERRIDES_CSWperldoc += surplus-dependency|CSWperl

# Core module updates
# Not used at the moment, leave one as example
#MASTER_SITES  += $(CPAN_FIRST_MIRROR)/S/SM/SMUELLER/
#CORE_UPDATES  += PathTools-3.30
#CORE_OBSOLETE += Cwd.pm File/Spec* auto/Cwd

DISTFILES += $(foreach N,$(CORE_UPDATESGCC build (Sunstudio is problematic) # claudio
GARCOMPILER = GCC4
ATES),$(N).tar.gz)

# Custom configure
CONFIGURE_SCRIPTS = perl

# Compatable with all prior patch revs
INC_COMPAT = 5.8.0 5.8.2 5.8.4 5.8.6 5.8.7 5.8.8 5.10.0 5.10.1 5.12.0 5. 5.12.4 5.14.0 5.14.1 5.14.2

# Force use of db-4.8
# TBD: Reinsert libperl.so, see below.
#rl.so, see below.
PERL_LIBS-32 += -lsocket -lnsl -lgdbm -ldb-4.8 -ldl #PERL_LIBS-32 += -lsocket -lnsl -ldl -lm -lpthread -lc -lpthread -lgdbm -ldb-4.8 -lcrypt
PERL_LIBS-32 += -lsocket -lnsl -ldl -lm -lpthread -lc -lpthread -lgdbm -lcrypt -lm -lpthread -lc
PERL_LIBS = $(PERL_LIBS-$(MEMORYMODEL)) 

#BUILD64 = 1

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

# When built on Solaris 10, enable DTrace support
CONFIGURE_ARGS-5.10 = -Dusedtrace
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(GAROSREL))

# Largefiles is on by default for 64 bit
CONFIGURE_ARGS-32 += -Duselargefiles 
CONFIGURE_ARGS += $(CONFIGURE_ARGS-#$(MEMORYMODEL)) 

CONFIGURE_ARGS += -Dvendorarch=$(libdir)/perl/csw
CONFIGURE_ARGS += -Dvendorlib=$(datadir)/perl/csw
CONFIGURE_ARGS += -Dvendorprefix=$(prefix)
CONFIGURE_ARGS += -Dlibs="$(PERL_LIBS)"
CONFIGURE_ARGS += -Dlibsdirs=" $(abspath /usr/lib/$(MEMORYMODEL)) $(libdir)"
CONFIGURE_ARGS += -Dsed=$(bindir)/gsed

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
#EXTRA_LDFLAGS-32 = -L$(libdir) -lperl 
EXTRA_LDFLAG -L/usr/lib
#EXTRA_LDFLAGS += $(EXTRA_LDFLAGS-$(MEMORYMODEL)) -R /usr/lib -R/opt/csw/bdb48/lib -R/opt/csw/lib
EXTRA_LDFLAGS += $(EXTRA_LDFLAGS-$(MEMORYMODEL)) -R /usr/libS-$(MEMORYMODEL)) 

# We want 64 bit binaries
#MERGE_DIRS_isa-extra = $(bindir) $(sbindir) $(libdir) $(libexecdir)

EXTRA_MERGE_EXCLUDE_FILES = .*\/perllocal.pod
PKGFILES_CSWperldoc = .*\/pod\/.*\.pod .*\/man\/man.\/.*

# The diagnostics.pm module needs the podfile to output its messages.
# That means it must be included in the main package, not the docs.
EXTRA_PKGFILES_EXCLUDED_CSWperldoc = .*\/perldiag.pod
EXTRA_PKGFILES_INCLUDED_CSWperl = .*\/perldiag.pod

# Tests take a long time, run once for every release
TEST_SCRIPTS =

BUILD_SCRIPTS = perl

TEST_SCRIPTS = perl

# Make sure we don't include the path to the newly built perl as the
# library is not in place yet.
IGNORE_DESTDIR = 1

# Do not exclude static libs as at least DynaLoader.a is needed for XS compilation
MERGE_EXCLUDE_STATICLIBS =

# This is for the communication with checkpkg. These pathes are searched for modules
# when resolving dependencies.
PROTOTYPE_FILTER_CSWperl = ( cat; echo "i cswperlincpath=CSWperl.cswperlincpath")

# Splitting of a separate libperl.so requires more work and careful planning.
# #Override for now.
CHECKPKG_OVERRIDES_CSWperl += shared-lib-package-contains-so-symlink|file=/opt/c#CHECKPKG_OVERRIDES_CSWperl += shared-lib-pkgname-mismatch|file=opt/csw/lib/libperl.so.5.16.1|soname=libperl.so.5.16.1|pkgname=CSWperl|expected=CSWlibperl5-16-1d=CSWlibperl5-12-4

include gar/category.mk

# This is probably due to -lperl, but during Configure the one in /opt/csw/lib is picked up and 
# the one in $WORKSRC has not been built yet 
# TBD: Investigate
post-extract-modulated:
	mkd#ir -p $(WORKSRC)
	gln -s libperl.so.$(VERSION) $(WORKSRC)/libperl.so
	@$(MAKECOOKIE)

ifneq ($(CORE_UPDATES),)
POST_TARGETS = install-core-updates
include files/updatecore.mk
endif

# How to configure Perl
#configure-perl: CONFIGURE_EXPORTS = PATH LD_OPTIONS
configure-perl: ARGS-64 = -dusedtrace
configure-perl:
	(cd $(WORKSRC) ; $(CONFIGURE_ENV) ./Configure $(CrONFIGURE_ARGS) -des)
	#cd $(WORKSRC) && ./Configure -ders -Dusethreads -Duselongdouble -Dinc_version_list=none $(ARGS-$(GAROSREL)) -Dprefix=$(prefix) -Dsed=/usr/bin/sed -Duseshrplib -Dcf_by='Claudio_Ramirez' -Dcf_email=claudio.ramirez@smals.be
	@# 64 bit: -Duse64bitall 
	@$(MAKECOOKIE)

build-perl: BUILD_EXPORTS = LD_OPTIONS
build-perl:
	@echo " ==> Running make in $*"
	@#cd $* && $(BUILD_ENV) $(MAKE) $(PARALLELMFLAGS) $(foreach TTT,$(BUILD_OVERRIDE_VARS),$(TTT)="$(BUILD_OVERRIDE_VAR_$(TTT))") $(foreach TTT,$(BUILD_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $(OBJDIR) $(BUILD_ARGS)
	cd $(WORKSRC) && $(BUILD_ENV) gmake
	@$(MAKECOOKIE)

test-perl:
	@echo " ==> Running make $(TEST_TARGET) in $*"
	@#cd $* && $(TEST_ENV) $(MAKE) $(PARALLELMFLAGS) $(foreach TTT,$(TEST_OVERRIDE_VARS),$(TTT)="$(TEST_OVERRIDE_VAR_$(TTT))") $(foreach TTT,$(TEST_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $(OBJDIR) $(TEST_ARGS) $(TEST_TARGET)
	cd $(WORKSRC) && gmake check
	@$(MAKECOOKIE)

# Make#POST_TARGETS += libperl
#LIB_MINOR = $(shell echo $(VERSION) | cut -f1-2 -d.)
#LIB_PATH  = $(libdir)/perl/$(VERSION)/CORE
#libperl:
#	@( cd $(DESTDIR)$(libdir) ; \
#		mv $(DESTDIR)$(LIB_PATH)/libperl.so.$(VERSION) \
#		$(DESTDIR)$(libdir) ; \
#		chmod 755 $(DESTDIR)$(libdir)/libperl.so.$(VERSION) ; \
#		ln -s libperl.so.$(VERSION) libperl.so.$(LIB_MINOR) 
#		#; \
#		#ln -s libperl.so.$(VERSION) libperl.so )
#	@$(MAKECOOKIE)

# Remove build paths from Config
#POST_TARGETS += perlconf
#perlconf:
#	@( cd $(DESTDIR)$(libdir)/perl/$(VERSION) ; \
#        /bin/perl -i -lne "\
#            next if /config_arg[1-9]/; \
#            s/^config_args=.+$$/config_args=''/; \
#            s/^config_argc=.+$$/config_argc='0'/; \
#            s,-I$(DESTDIR)$(includedir),,g; \
#            s,-[LR]$(DESTDIR)$(libdir),,g; \
#            s,( -I$(includedir))+,\$$1,g; \
#            s,( -[LR]$(libdir))+,\$$1,g; \
#            s,-R $(libdir)/perl/$(VERSION)/CORE,-R $(libdir),; \
#            s, (-L)?$(CC_HOME)\S+,,g; \
#            if (/^\w+=/) { \
#                s/\s{2,}(\-)/ \-/g; \
#                s/(^\w+=.) /\$$1/; \
#                s/ (.)$$/\$$1/g; \
#            } \
#            print \
#        " Config.pm Config_heavy.pl )
#	@$(MAKECOOKIE)

#POST_TARGETS += CSWperl.cswperlincpath
#CSWperl.cswperlincpath:
#l.cswperlincpath:
	LD_LIBRARY_PATH=$(WORKSRC) $(WORKSRC)/perl -I./lib -e 'print "$$_\n" foreach(@INC)' >$(WORKDIR_GLOBAL)/CSWperl.cswperlincpath

# Invoke pos#post-install-modulated: $(POST_TARGETS)
#	@$(MAKECOOKIE)
