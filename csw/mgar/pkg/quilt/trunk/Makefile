NAME = quilt
VERSION = 0.48
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A patch management tooln
define BLURB
Quilt allows you to easily manage large numbers of patches by keeping
track of the changes each patch makes. Patches can be applied,
un-applied, refreshed, and more.

Quilt originally was based on Andrew Morton's patch scripts found at
http://www.zip.com.au/~akpm/linux/patches/.
endef

PACKAGES = CSWquilt CSWquilt-el CSWquilt-completion

SPKG_DESC_CSWquilt-el = Emacs support for quilt
SPKG_DESC_CSWquilt-completion = Bash completion support for quilt
CATALOGNAME_CSWquilt-el = quilt_el
CATALOGNAME_CSWquilt-completion = quilt_completion

ARCHALL_CSWquilt-el = 1
ARCHALL_CSWquilt-completion = 1

RUNTIME_DEP_PKGS_CSWquilt =  CSWcoreutils
RUNTIME_DEP_PKGS_CSWquilt += CSWperl CSWgawk CSWgsed CSWbash CSWdiffstat
RUNTIME_DEP_PKGS_CSWquilt += CSWgpatch CSWmktemp CSWggrep CSWggettext
RUNTIME_DEP_PKGS_CSWquilt += CSWfindutils CSWggetopt CSWdiffutils
RUNTIME_DEP_PKGS_CSWquilt += CSWgnulinks CSWcolumn

RUNTIME_DEP_PKGS_CSWquilt-el = CSWemacscommon CSWquilt
RUNTIME_DEP_PKGS_CSWquilt-complation = CSWbashcmplt CSWquilt

BUILD_DEP_PKGS = $(filter-out CSWcoreutils, $(RUNTIME_DEP_PKGS_CSWquilt))

PKGFILES_CSWquilt-el = $(datadir)/emacs/site-lisp/.*
PKGFILES_CSWquilt-completion = $(prefix)/etc/.*

MASTER_SITES = http://mirror.csclub.uwaterloo.ca/nongnu/quilt/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of
# MASTER_SITES, then uncomment the next line. Otherwise it is set by
# default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

sysconfdir = /etc/opt/csw

CONFIGURE_ARGS =  $(DIRPATHS)
CONFIGURE_ARGS += --with-bash=/opt/csw/bin/bash
CONFIGURE_ARGS += --with-cp=/opt/csw/bin/gcp
CONFIGURE_ARGS += --with-date=/opt/csw/bin/gdate
CONFIGURE_ARGS += --with-perl=/opt/csw/bin/perl
CONFIGURE_ARGS += --with-grep=/opt/csw/bin/ggrep
CONFIGURE_ARGS += --with-tail=/opt/csw/bin/gtail
CONFIGURE_ARGS += --with-tr=/opt/csw/bin/gtr
CONFIGURE_ARGS += --with-sed=/opt/csw/bin/gsed
CONFIGURE_ARGS += --with-awk=/opt/csw/bin/gawk
CONFIGURE_ARGS += --with-column=/opt/csw/bin/column
CONFIGURE_ARGS += --with-pod2man=/opt/csw/bin/pod2man
CONFIGURE_ARGS += --with-getopt=/opt/csw/bin/ggetopt
CONFIGURE_ARGS += --with-diff=/opt/csw/bin/gdiff
CONFIGURE_ARGS += --with-mktemp=/opt/csw/bin/mktemp
CONFIGURE_ARGS += --with-patch=/opt/csw/bin/gpatch
CONFIGURE_ARGS += --with-diffstat=/opt/csw/bin/diffstat
CONFIGURE_ARGS += --with-find=/opt/csw/bin/gfind
CONFIGURE_ARGS += --with-sendmail=/usr/lib/sendmail
CONFIGURE_ARGS += --without-rpmbuild

COMPILE_ELISP = 1

CHECKPKG_OVERRIDES_CSWquilt += unidentified-dependency|CSWcoreutils

# quilt overrides
CHECKPKG_OVERRIDES_CSWquilt += surplus-dependency|CSWcoreutils
CHECKPKG_OVERRIDES_CSWquilt += surplus-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWquilt += surplus-dependency|CSWgsed
CHECKPKG_OVERRIDES_CSWquilt += surplus-dependency|CSWgawk
CHECKPKG_OVERRIDES_CSWquilt += surplus-dependency|CSWfindutils
CHECKPKG_OVERRIDES_CSWquilt += surplus-dependency|CSWgnulinks
CHECKPKG_OVERRIDES_CSWquilt += surplus-dependency|CSWggrep
CHECKPKG_OVERRIDES_CSWquilt += surplus-dependency|CSWdiffstat
CHECKPKG_OVERRIDES_CSWquilt += surplus-dependency|CSWmktemp
CHECKPKG_OVERRIDES_CSWquilt += surplus-dependency|CSWbash
CHECKPKG_OVERRIDES_CSWquilt += surplus-dependency|CSWggetopt
CHECKPKG_OVERRIDES_CSWquilt += surplus-dependency|CSWdiffutils
CHECKPKG_OVERRIDES_CSWquilt += surplus-dependency|CSWggettext
CHECKPKG_OVERRIDES_CSWquilt += surplus-dependency|CSWgpatch
CHECKPKG_OVERRIDES_CSWquilt += surplus-dependency|CSWcolumn

# quilt_el overrides
CHECKPKG_OVERRIDES_CSWquilt-el += surplus-dependency|CSWquilt

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

# it seems they prefer the RPM name for this variable in their Makefile
BUILD_ROOT = $(DESTDIR)
EXTRA_COMMON_EXPORTS += BUILD_ROOT

post-install-modulated:
	@( gmkdir -p $(DESTDIR)/$(sysconfdir)/; \
	   mv $(DESTDIR)/$(prefix)/etc/quilt.quiltrc $(DESTDIR)/$(sysconfdir) )
	@$(MAKECOOKIE)
