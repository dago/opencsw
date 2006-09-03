GARNAME = SVK
GARVERSION = 1.08
CATEGORIES = cpan
AUTHOR = CLKAO

DESCRIPTION = a distributed version control system
define BLURB
  SVK is a decentralized version control system written in Perl. It uses the
  Subversion filesystem but provides additional features.
endef

DISTFILES = $(call admfiles,CSWsvk,depend prototype)

DEPENDS += utils/subversion

# Core
DEPENDS += cpan/Algorithm-Annotate cpan/Algorithm-Diff cpan/YAML
DEPENDS += cpan/Regexp-Shellish cpan/Data-Hierarchy cpan/Clone
DEPENDS += cpan/Pod-Escapes cpan/Pod-Simple cpan/PerlIO-via-dynamic
DEPENDS += cpan/PerlIO-via-symlink cpan/IO-Digest cpan/SVN-Simple
DEPENDS += cpan/TimeDate cpan/File-Type cpan/URI cpan/PerlIO-eol
DEPENDS += cpan/Class-Autouse

# Features
DEPENDS += cpan/Locale-Maketext-Simple
DEPENDS += cpan/IO-Pager
DEPENDS += cpan/SVN-Mirror
DEPENDS += cpan/Compress-Zlib cpan/FreezeThaw

include ../category.mk

