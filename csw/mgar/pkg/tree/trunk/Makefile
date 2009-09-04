# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

## This file contains comments to guide you through various GAR settings.
## Please remove unnecessary comments before committing your code to the code
## repository. The comments to remove are marked with double hashes.
## If you want to remove them all in-place, use:
## gsed -i -e '/^##/d' Makefile
##
## For more information about GAR variables, please see:
## https://sourceforge.net/apps/trac/gar/wiki/GAR%20Variable%20Reference
##
GARNAME = tree
GARVERSION = 1.5.2.2
##
## The category that your software fits in. This is not a descriptive field, but
## influences the build process. Depending on the CATEGORIES setting, different
## Makefiles are included from gar/categories/ in your trunk directory, which
## adjust the build settings for the respective category.
##
## Possible settings are:
## apps, cpan, devel, gnome, java, kde, lang, lib, meta, net, python, server,
## utils, x11, xfce, xorg, xtra
CATEGORIES = utils
##
## A one-line description of the package, which will appear in the pkginfo.
DESCRIPTION = A recursive directory listing program
##
## A longer description of the package. This is only for descriptive purposes
## inside the Makefile and is not used elsewhere.
define BLURB
  Tree is a recursive directory listing program that produces a depth indented
  listing of files, which is colorized ala dircolors if the LS_COLORS
  environment variable is set and output is to tty. 
endef
##
## Upstream URL that should show up in the VENDOR field as well as on
## http://opencsw.org/packages/<packagename>.
SPKG_SOURCEURL = http://mama.indstate.edu/users/ice/tree/
##
## Whitespace-separated list of URLs to download the source package from.
## There are presets: $(SF_MIRRORS), $(GNU_MIRRORS) and $(GOOGLE_MIRROR).
MASTER_SITES  = ftp://mama.indstate.edu/linux/tree/
MASTER_SITES += http://www.sfr-fresh.com/linux/misc/
##
## SF_PROJ is required if you set $(MASTER_SITES) to $(SF_MIRRORS) and the
## Sourceforge project name differs from $(GARNAME). Specifies the Sourceforge
## project name of the software you wish to download.
## SF_PROJ =
##
## A list of space separated patch filenames from files/ that are to be applied
## to the extracted software before the ./configure stage. Patches need to be
## included in the DISTFILES variable as well.
# PATCHFILES  = 0001-Solaris-settings.patch
# PATCHFILES += 0002-install-binary-as-a-parameter.patch
# PATCHFILES += 0003-Destdir-support.patch
PATCHFILES = solaris.patch
##
## Whitespace-separated list of files which comprise this build. mGAR will look
## for the files in the $(FILEDIR) (trunk/files) directory and on the
## $(MASTER_SITES).
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
##
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tgz
##
## Catalog name is the name to be used with pkg{-get,util} -i <pkgname>.
## It is different from the system package name, which by convention is CSWpkgname.
## CATALOGNAME =
##
## Set to 1 to mark the package as architecture-independent.
## ARCHALL = 0
##
## A list of files / patterns that should be excluded from the package. Amends
## the default list of excluded filenames $(MERGE_EXCLUDE_DEFAULT), which
## contains things like libtool .la files and files with a leading ~.
## EXTRA_MERGE_EXCLUDE_FILES =
##
## A list of space separated package names that should be marked as
## incompatible with the current package. This will go into the depend file.
## When a user has one of the incompatible packages installed and installs
## your package, he will be prompted that the incompatible package must be
## removed. He will however not be prevented to install your package without
## removing the conflicting package first.
## INCOMPATIBLE_PKGS =
##
##  The name of the license file that should be included in your package. Defaults
##  to COPYING. See http://sourceforge.net/apps/trac/gar/wiki/CopyRightfor details
##  on including and displaying licenses.
## LICENSE =
##
## A list of space separated package names that should be produced from your
## Makefile. This is used when a software has different components that can be
## packaged and used individually (think runtime libraries, client tools, server
## files, development headers). You don't need to set this when you just want to
## produce one package.
##
## When you set this variable to include more than one package, you also need to
## set PKGFILES_CSWpkgname for each package (except for the first one in your
## $(PACKAGES) list) to define which files go into each package. The first
## package from $(PACKAGES) one will hold all files that are not matched by
## PKGFILES_ for other packages.
## PACKAGES =
##
## If specified, GAR feeds the almost-final package prototype file to
## $(PROTOTYPE_FILTER) and reads the final package prototype file from it.
## $(PROTOTYPE_FILTER) is usually a sed/awk/perl one-liner, which was mostly used
## to prepare the prototype file for use with cswclassutils (see
## $(SPKG_CLASSES)). Now that there are convenience variables for cswclassutils,
## you will rarely have to use this. A still valid use case would be to change
## the file permissions of a file to be set-UID.
## See http://wiki.opencsw.org/cswclassutils-package for common usage information
## PROTOTYPE_FILTER =
##
## cswclassutils settings
##
## A list of action classes. Possible values are:
## none cswpreserveconf cswcpsampleconf cswpycompile cswusergroup cswinitsmf
## The class 'cswinitsmf' must be the last class listed. When you use cswclassutils,
## you need to add CSWcswclassutils to REQUIRED_PKGS.
## SPKG_CLASSES = none
## Simplified settings for classes:
## PRESERVECONF =
## SAMPLECONF =
## INITSMF =
## USERGROUP =
## A list of runtime package dependencies in the form of CSWfoo.
## REQUIRED_PKGS =
##
## A list of packages necessary to build this package
## PREREQUISITE_PKGS = $(REQUIRED_PKGS)
##
## When using non-empty $(PACKAGES):
## REQUIRED_PKGS_CSWpkgname =
## SPKG_DESC_CSWpkgname =
## PKGFILES_CSWpkgname =
## CATALOGNAME_CSWpkgname =
##
## A list of space separated directories where objects should be stripped in
## addition to the bin/ and sbin/ directories.
## STRIP_DIRS =
##
## Define a custom target for the configure phase. When you set this, the target
## that will be used instead of configure: target, is named
## configure-$(CONFIGURE_SCRIPTS) and you will need to define it in your Makefile
## after including gar/gar.include.mk. If you want to skip the configure phase
## completely (for example when your software doesn't need to be compiled) assign
## this variable an empty value. The procedure works for configure, build,
## install and test steps.
CONFIGURE_SCRIPTS =
## BUILD_SCRIPTS =
## INSTALL_SCRIPTS =
SKIPTEST = 1
##
## Compilation settings
##
## The build directory.
## WORKSRC = $(WORKDIR)/$(GARNAME)-$(GARVERSION)
##
## BUILD_ARGS is passed as an argument to gmake during the build phase. Use this
## for example, if you need to override Makefile variables.
## BUILD_ARGS =
##
## Arguments passed to the ./configure script.
## CONFIGURE_ARGS = $(DIRPATHS)
##
## BUILD64 =
## CONFIGURE_ENV =
## EXTRA_CFLAGS =
## EXTRA_LDFLAGS =
## EXTRA_INC =
## EXTRA_LIB =
## GARFLAVOR =
## INSTALL_ARGS =
## OPT_FLAGS_SOS = -xO3
## OPT_FLAGS_GCC = -O2 -pipe
##
## The compiler to use. Defaults to SOS11, can be also: SOS12, GCC3, GCC4.
## GARCOMPILER = SOS11
##
include gar/category.mk
