GARNAME = Crypt-Random
GARVERSION = 1.25
CATEGORIES = cpan
AUTHOR = VIPUL

DESCRIPTION = cryptographically secure, true random number generator.
define BLURB
  Crypt::Random is an interface module to the /dev/random device found on most
  modern unix systems. It also interfaces with egd, a user space entropy
  gathering daemon, available for systems where /dev/random (or similar)
  devices are not available. When Math::Pari is installed, Crypt::Random can
  generate random integers of arbritary size of a given bitsize or in a
  specified interval.
endef

DISTFILES = $(call admfiles,CSWpmcryptrandom,depend)

DEPENDS += cpan/Math-Pari cpan/Class-Loader

include ../category.mk
