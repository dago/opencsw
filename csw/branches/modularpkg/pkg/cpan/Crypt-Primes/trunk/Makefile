GARNAME = Crypt-Primes
GARVERSION = 0.50
CATEGORIES = cpan
AUTHOR = VIPUL

DESCRIPTION = prime number generator suitable for cryptographic applications.
define BLURB
  This module implements Ueli Maurer's algorithm for generating large provable
  primes and secure parameters for public-key cryptosystems. The generated
  primes are almost uniformly distributed over the set of primes of the
  specified bitsize and expected time for generation is less than the time
  required for generating a pseudo-prime of the same size with Miller-Rabin
  tests. Detailed description and running time analysis of the algorithm can
  be found in Maurer's paper[1].
endef

DISTFILES += CSWpmcryptprimes.gspec CSWpmcryptprimes.depend

DEPENDS += cpan/Crypt-Random

include gar/category.mk
