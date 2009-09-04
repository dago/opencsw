GARNAME = libtool
RELEASE = a
GARVERSION = 2.2.6
CATEGORIES = devel

EXTRA_MODULATORS = GARVERSION GARCOMPILER
MODULATIONS_GARVERSION = 1.5.26 2.2.6
MODULATIONS_GARCOMPILER = GCC3 GCC4 SOS11

# Modulate over compiler only for 2.2.6
SKIP_MODULATIONS = $(foreach I,sparcv8 sparcv9 i386 amd64,$(foreach C,GCC3 GCC4,isa-$I-garversion-1.5.26-garcompiler-$C))

FILEVERSION_1.5.26 = 1.5.26
FILEVERSION_2.2.6 = 2.2.6$(RELEASE)

DESCRIPTION = A generic library support tool
define BLURB
  GNU libtool is a generic library support script. Libtool hides the complexity
  of using shared and static libraries behind a consistent, portable interface.
  Libtool supports building static libraries on all platforms.
endef

MASTER_SITES = $(GNU_MIRROR)
SOURCEFILES  = $(foreach VERSION,$(MODULATIONS_GARVERSION),$(GARNAME)-$(FILEVERSION_$(VERSION)).tar.gz)
DISTFILES    = $(SOURCEFILES)

PATCH_LIBTOOL = patch-libtool.diff
PATCHFILES_POSTINSTALL_isa-i386-garversion-2.2.6-garcompiler-SOS11 = $(PATCH_LIBTOOL)
PATCHFILES_POSTINSTALL_isa-sparcv8-garversion-2.2.6-garcompiler-SOS11 = $(PATCH_LIBTOOL)
DISTFILES += $(PATCH_LIBTOOL)

NOEXTRACT = $(filter-out $(GARNAME)-$(FILEVERSION_$(GARVERSION)).tar.gz,$(SOURCEFILES))

EXTRA_TAGS = gcc3 gcc4
COMPILER_TAGNAME_GCC3 = gcc3
COMPILER_TAGNAME_GCC4 = gcc4

PACKAGES = CSWlibtool CSWlibtoolrt
CATALOGNAME_CSWlibtoolrt = libtool_rt

SPKG_SOURCEURL = http://www.gnu.org/software/libtool/

REQUIRED_PKGS_CSWlibtool = CSWlibtoolrt

SPKG_DESC_CSWlibtool   = A generic library support tool
SPKG_DESC_CSWlibtoolrt = A generic library support tool runtime libraries

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

BUILD64 = 1
NO_ISAEXEC = 1

SKIPTEST = 1
TEST_TARGET = check

   MERGE_SCRIPTS_isa-i386-garversion-1.5.26-garcompiler-SOS11 = copy-only
      MERGE_DIRS_isa-i386-garversion-1.5.26-garcompiler-SOS11 = $(libdir)
  MERGE_SCRIPTS_isa-amd64-garversion-1.5.26-garcompiler-SOS11 = copy-relocated-only
     MERGE_DIRS_isa-amd64-garversion-1.5.26-garcompiler-SOS11 = $(libdir)

    MERGE_SCRIPTS_isa-i386-garversion-2.2.6-garcompiler-SOS11 = copy-all
   MERGE_SCRIPTS_isa-amd64-garversion-2.2.6-garcompiler-SOS11 = copy-relocated-only
      MERGE_DIRS_isa-amd64-garversion-2.2.6-garcompiler-SOS11 = $(libdir)

     MERGE_SCRIPTS_isa-i386-garversion-2.2.6-garcompiler-GCC3 = copy-tags
     MERGE_SCRIPTS_isa-i386-garversion-2.2.6-garcompiler-GCC4 = copy-tags

MERGE_SCRIPTS_isa-sparcv8-garversion-1.5.26-garcompiler-SOS11 = copy-only
   MERGE_DIRS_isa-sparcv8-garversion-1.5.26-garcompiler-SOS11 = $(libdir)
MERGE_SCRIPTS_isa-sparcv9-garversion-1.5.26-garcompiler-SOS11 = copy-relocated-only
   MERGE_DIRS_isa-sparcv9-garversion-1.5.26-garcompiler-SOS11 = $(libdir)

 MERGE_SCRIPTS_isa-sparcv8-garversion-2.2.6-garcompiler-SOS11 = copy-all
 MERGE_SCRIPTS_isa-sparcv9-garversion-2.2.6-garcompiler-SOS11 = copy-relocated-only
    MERGE_DIRS_isa-sparcv9-garversion-2.2.6-garcompiler-SOS11 = $(libdir)

  MERGE_SCRIPTS_isa-sparcv8-garversion-2.2.6-garcompiler-GCC3 = copy-tags
  MERGE_SCRIPTS_isa-sparcv8-garversion-2.2.6-garcompiler-GCC4 = copy-tags

PKGFILES_CSWlibtoolrt = $(PKGFILES_RT)

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

post-install-modulated: $(if $(PATCHFILES_POSTINSTALL_$(MODULATION)),patch-libtool)
post-install-modulated: $(if $(COMPILER_TAGNAME_$(GARCOMPILER)),install-libtool-$(COMPILER_TAGNAME_$(GARCOMPILER)))

patch-libtool:
	cat $(WORKDIR)/$(PATCHFILES_POSTINSTALL_$(MODULATION)) | (cd $(DESTDIR)$(bindir) && gpatch -p1)

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


