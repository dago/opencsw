GARNAME = SVK
GARVERSION = 2.0.0
CATEGORIES = cpan
AUTHOR = CLKAO

DESCRIPTION = a distributed version control system
define BLURB
  SVK is a decentralized version control system written in Perl. It uses the
  Subversion filesystem but provides additional features.
endef

DISTFILES = $(call admfiles,CSWsvk,depend prototype)

MODDIST = $(GARNAME)-v$(GARVERSION).tar.gz

# Build
#BUILDDEPS += cpan/ExtUtils-AutoInstall

# Core
DEPENDS += utils/subversion
DEPENDS += cpan/Algorithm-Annotate
DEPENDS += cpan/Algorithm-Diff
DEPENDS += cpan/App-CLI
DEPENDS += cpan/Class-Accessor
DEPENDS += cpan/Class-Autouse
DEPENDS += cpan/Class-Data-Inheritable
DEPENDS += cpan/Data-Hierarchy
DEPENDS += cpan/IO-Digest
DEPENDS += cpan/List-MoreUtils
DEPENDS += cpan/Path-Class
DEPENDS += cpan/PerlIO-eol
DEPENDS += cpan/PerlIO-via-dynamic
DEPENDS += cpan/PerlIO-via-symlink
DEPENDS += cpan/SVN-Simple
DEPENDS += cpan/TermReadKey
DEPENDS += cpan/UNIVERSAL-require
DEPENDS += cpan/URI
DEPENDS += cpan/YAML
DEPENDS += cpan/YAML-Syck

# No longer needed?
#DEPENDS += cpan/Regexp-Shellish
#DEPENDS += cpan/Clone
#DEPENDS += cpan/Pod-Escapes
#DEPENDS += cpan/Pod-Simple
#DEPENDS += cpan/TimeDate
#DEPENDS += cpan/File-Type

# Features
DEPENDS += cpan/Compress-Zlib
DEPENDS += cpan/FreezeThaw
DEPENDS += cpan/IO-Pager
DEPENDS += cpan/Locale-Maketext-Lexicon
DEPENDS += cpan/Locale-Maketext-Simple
DEPENDS += cpan/Log-Log4perl
DEPENDS += cpan/SVN-Mirror

WORKSRC = $(WORKDIR)/$(GARNAME)-v$(GARVERSION)

include ../category.mk

