NAME = File-Which
VERSION = 1.09
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = ADAMK

DESCRIPTION = Portable implementation of the `which' utility
define BLURB
  File::Which was created to be able to get the paths to executable programs 
  on systems under which the `which' program wasn't implemented in the shell.

  File::Which searches the directories of the user's PATH (as returned by 
  File::Spec->path()), looking for executable files having the name specified 
  as a parameter to which(). Under Win32 systems, which do not have a notion 
  of directly executable files, but uses special extensions such as .exe and 
  .bat to identify them, File::Which takes extra steps to assure that you will 
  find the correct file (so for example, you might be searching for perl, 
  it'll try perl.exe, perl.bat, etc.)
endef

CATALOGNAME = pm_filehomedir
PACKAGES    = CSWpmfilehomedir

ARCHALL_CSWpmfilehomedir = 1

LICENSE = LICENSE

include gar/category.mk

