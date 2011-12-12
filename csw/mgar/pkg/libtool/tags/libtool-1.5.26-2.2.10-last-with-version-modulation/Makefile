NAME = libtool
VERSION = 2.2.10
CATEGORIES = devel

EXTRA_MODULATORS = VERSION GARCOMPILER
MODULATIONS_VERSION = 1.5.26 2.2.10
MODULATIONS_GARCOMPILER = GCC3 GCC4 SOS12

# Modulate over compiler only for 2.2.6
SKIP_MODULATIONS = $(foreach I,sparcv8 sparcv9 i386 amd64,$(foreach C,GCC3 GCC4,isa-$I-garversion-1.5.26-garcompiler-$C))
# Compile 64 bit libraries only with SOS12
SKIP_MODULATIONS += $(foreach I,sparcv9 amd64,$(foreach C,GCC3 GCC4,isa-$I-garversion-2.2.10-garcompiler-$C))

DESCRIPTION = A generic library support tool
define BLURB
  GNU libtool is a generic library support script. Libtool hides the complexity
  of using shared and static libraries behind a consistent, portable interface.
  Libtool supports building static libraries on all platforms.
endef

MASTER_SITES = $(GNU_MIRROR)
SOURCEFILES  = $(foreach VERSION,$(MODULATIONS_VERSION),$(NAME)-$(VERSION).tar.gz)
DISTFILES    = $(SOURCEFILES)

PATCH_LIBTOOL = patch-libtool.diff
PATCHFILES_POSTINSTALL_isa-i386-garversion-2.2.10-garcompiler-SOS12 = $(PATCH_LIBTOOL)
PATCHFILES_POSTINSTALL_isa-sparcv8-garversion-2.2.10-garcompiler-SOS12 = $(PATCH_LIBTOOL)
DISTFILES += $(PATCH_LIBTOOL)

NOEXTRACT = $(filter-out $(NAME)-$(VERSION).tar.gz,$(SOURCEFILES))

EXTRA_TAGS = gcc3 gcc4 sos12
COMPILER_TAGNAME_GCC3 = gcc3
COMPILER_TAGNAME_GCC4 = gcc4
COMPILER_TAGNAME_SOS12 = sos12

PACKAGES = CSWlibtool CSWlibtoolrt
CATALOGNAME_CSWlibtoolrt = libtool_rt

SPKG_SOURCEURL = http://www.gnu.org/software/libtool/

RUNTIME_DEP_PKGS_CSWlibtool = CSWlibtoolrt

SPKG_DESC_CSWlibtool   = A generic library support tool
SPKG_DESC_CSWlibtoolrt = A generic library support tool runtime libraries

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

BUILD64 = 1
NOISAEXEC = 1

SKIPTEST = 1
TEST_TARGET = check

   MERGE_SCRIPTS_isa-default-garversion-1.5.26-garcompiler-SOS12 = copy-only
      MERGE_DIRS_isa-default-garversion-1.5.26-garcompiler-SOS12 = $(libdir)
 MERGE_SCRIPTS_isa-default64-garversion-1.5.26-garcompiler-SOS12 = copy-relocated-only
    MERGE_DIRS_isa-default64-garversion-1.5.26-garcompiler-SOS12 = $(libdir)

   MERGE_SCRIPTS_isa-default-garversion-2.2.10-garcompiler-SOS12 = copy-all
 MERGE_SCRIPTS_isa-default64-garversion-2.2.10-garcompiler-SOS12 = copy-relocated-only
    MERGE_DIRS_isa-default64-garversion-2.2.10-garcompiler-SOS12 = $(libdir)

    MERGE_SCRIPTS_isa-default-garversion-2.2.10-garcompiler-GCC3 = copy-tags
    MERGE_SCRIPTS_isa-default-garversion-2.2.10-garcompiler-GCC4 = copy-tags

PKGFILES_CSWlibtoolrt = $(PKGFILES_RT)

CHECKPKG_OVERRIDES_CSWlibtool += surplus-dependency|CSWlibtoolrt

include gar/category.mk

post-install-modulated: $(if $(PATCHFILES_POSTINSTALL_$(MODULATION)),patch-libtool)
post-install-modulated: $(if $(COMPILER_TAGNAME_$(GARCOMPILER)),install-libtool-$(COMPILER_TAGNAME_$(GARCOMPILER)))

patch-libtool:
	cat $(WORKDIR)/$(PATCHFILES_POSTINSTALL_$(MODULATION)) | (cd $(DESTDIR)$(bindir) && gpatch -p1)
	# Remove arch-specific flags from the libtool-compilation so they don't spoil the target build
	perl -pi -e 's/^LTCFLAGS=.*/LTCFLAGS="-O"/' $(DESTDIR)$(bindir)/libtool
	@$(MAKECOOKIE)

install-libtool-%:
	perl -ane 'print if( /^available_tags/ ); $$p = 1 if( /^# ### BEGIN LIBTOOL CONFIG/ ); print if( $$p ); $$p = 0 if( /^# ### END LIBTOOL CONFIG/ )' \
		<$(DESTDIR)$(bindir)/libtool >$(DESTDIR)$(datadir)/libtool/$*.conf
	perl -ane '$$p = 1 if( /^# ### BEGIN LIBTOOL TAG CONFIG/ ); print if( $$p ); if( /^# ### END LIBTOOL TAG CONFIG/ ) { $$p = 0; print "\n"; }' \
		<$(DESTDIR)$(bindir)/libtool >$(DESTDIR)$(datadir)/libtool/$*.tags
	@$(MAKECOOKIE)

merge-copy-tags:
	$(_DBG_MERGE)(cd $(INSTALLISADIR); pax -r -w -v $(_PAX_ARGS) \
		-s ",^\(\..*\.conf\)\$$,\1,p" \
		-s ",^\(\..*\.tags\)\$$,\1,p" \
		-s ",.*,," \
		. $(PKGROOT) \
	)
	@$(MAKECOOKIE)


