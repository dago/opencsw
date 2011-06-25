NAME = Path-Class
VERSION = 0.24
CATEGORIES = cpan
AUTHOR = KWILLIAMS

DESCRIPTION = Cross-platform path specification manipulation
define BLURB
  Path::Class is a module for manipulation of file and directory
  specifications (strings describing their locations, like '/home/ken/foo.txt'
  or 'C:\Windows\Foo.txt') in a cross-platform manner. It supports pretty much
  every platform Perl runs on, including Unix, Windows, Mac, VMS, Epoc,
  Cygwin, OS/2, and NetWare.
endef

BUILD_DEP_PKGS               = CSWpmextutilsdepends CSWpmextutpkgconf
RUNTIME_DEP_PKGS_CSWpmpathclass = CSWpmextutilsdepends CSWpmextutpkgconf

CATALOGNAME = pm_pathclass
PACKAGES        = CSWpmpathclass

ARCHALL_CSWpmpathclass = 1

LICENSE = README

CHECKPKG_OVERRIDES_CSWpmpathclass += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/Path::Class::File.3perl
CHECKPKG_OVERRIDES_CSWpmpathclass += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/Path::Class::Dir.3perl
CHECKPKG_OVERRIDES_CSWpmpathclass += file-with-bad-content|/usr/local|root/opt/csw/share/perl/csw/Path/Class/File.pm
CHECKPKG_OVERRIDES_CSWpmpathclass += file-with-bad-content|/usr/local|root/opt/csw/share/perl/csw/Path/Class/Dir.pm
CHECKPKG_OVERRIDES_CSWpmpathclass += catalogname-does-not-match-pkgname|pkgname=CSWpmpathclass|catalogname=pm_pathclass|expected-catalogname=pmpathclass

include gar/category.mk

