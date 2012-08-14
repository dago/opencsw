NAME = File-Which
VERSION = 1.09
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = ADAMK

DESCRIPTION = Portable implementation of the "which" utility
define BLURB
  File::Which was created to be able to get the paths to executable programs on
  systems under which the `which' program wasn't implemented in the shell.

  File::Which searches the directories of the user's PATH (as returned by
  File::Spec->path()), looking for executable files having the name specified
  as a parameter to which(). Under Win32 systems, which do not have a notion of
  directly executable files, but uses special extensions such as .exe and .bat
  to identify them, File::Which takes extra steps to assure that you will find
  the correct file (so for example, you might be searching for perl, it'll try
  perl.exe, perl.bat, etc.)
endef

CATALOG_RELEASE = unstable
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

LICENSE_TEXT = This module is licensed under the perl license

PACKAGES = CSWpm-file-which
ARCHALL = 1

BUILDIME_DEP_PKGS_CSWpm-file-which += CSWpm-test-script

RUNTIME_DEP_PKGS_CSWpm-file-which += CSWpm-pathtools

include gar/category.mk
