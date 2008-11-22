GARNAME = Cache
GARVERSION = 2.04
CATEGORIES = cpan
AUTHOR = CLEISHMAN

DESCRIPTION = new cache interface.
define BLURB
  The Cache modules are designed to assist a developer in persisting data for
  a specified period of time. Often these modules are used in web applications
  to store data locally to save repeated and redundant expensive calls to
  remote machines or databases.
endef

DISTFILES = $(call admfiles,CSWpmcache,depend prototype)

DEPENDS += cpan/Heap cpan/IO-String cpan/File-NFSLock
DEPENDS += cpan/Digest-SHA1 cpan/TimeDate

include ../category.mk
