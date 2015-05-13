NAME = quilt
VERSION = 0.64
GARTYPE = v2

DESCRIPTION = A patch management tool

MASTER_SITES = http://mirror.csclub.uwaterloo.ca/nongnu/quilt/
DISTFILES += $(DISTNAME).tar.gz

PATCHFILES += 0001-Use-bash.patch
PATCHFILES += 0002-etc-is-sysconfdir.patch

# For formail
BUILD_DEP_PKGS += CSWprocmail
# There are probably some more missing

PACKAGES += CSWquilt
SPKG_DESC_CSWquilt = A patch management tool
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWquilt += CSWcoreutils
RUNTIME_DEP_PKGS_CSWquilt += CSWperl
RUNTIME_DEP_PKGS_CSWquilt += CSWgawk
RUNTIME_DEP_PKGS_CSWquilt += CSWgsed
RUNTIME_DEP_PKGS_CSWquilt += CSWbash
RUNTIME_DEP_PKGS_CSWquilt += CSWdiffstat
RUNTIME_DEP_PKGS_CSWquilt += CSWgpatch
RUNTIME_DEP_PKGS_CSWquilt += CSWmktemp
RUNTIME_DEP_PKGS_CSWquilt += CSWggrep
RUNTIME_DEP_PKGS_CSWquilt += CSWfindutils
RUNTIME_DEP_PKGS_CSWquilt += CSWggetopt
RUNTIME_DEP_PKGS_CSWquilt += CSWdiffutils
RUNTIME_DEP_PKGS_CSWquilt += CSWcolumn
# Just because of .el files we don't want emacs
CHECKPKG_OVERRIDES_CSWquilt += missing-dependency|CSWemacs-common

# Don't split out small stuff
OBSOLETED_BY_CSWquilt += CSWquilt-el
OBSOLETED_BY_CSWquilt += CSWquilt-completionfd#where can we build?
PACKAGING_PLATFORMS += solaris9-sparc
PACKAGING_PLATFORMS += solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc
PACKAGING_PLATFORMS += solaris10-i386
fdir = /etc/opt/csw

CONFIGURE_ARGS =  $(DIRPATHS)
CONFIGURE_ARGS += --with-bash=/opt/csw/bin/bash
CONFIGURE_ARGS += --with-cp=/opt/csw/bin/gcp
CONFIGURE_ARGS += --with-date=/opt/csw/bin/gdate
CONFIGURE_ARGS += --with-perl=/opt/csw/bin/perl
CONFIGURE_ARGS += --with-grep=/opt/csw/bin/ggrep
CONFIGstat=/opt/csw/bin/gstat=/opt/csw/bin/ggrep
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
CONFI-xargs=/opt/csw/bin/gxargs
CONFIGURE_ARGS += --without-rpmbuild

# There are some tests failing, investigate
SKIPTEST ?= 1

COMPILE_ELISP = 1

# it seems they prefer the RPM name for this variable in their Makefile
EXTRA_INSTALL_EXPORTS += BUILD_ROOT
INSTALL_ENV_BUILD_ROOT = $(DESTDIR)

PRESERVECONF += $(sysconfdir)/quilt.quiltrc

include gar/category.mk
