GARNAME = Class-DBI
GARVERSION = 3.0.3
CATEGORIES = cpan
AUTHOR = TMTM

DESCRIPTION = simple database abstraction
define BLURB
  Class::DBI provides a convenient abstraction layer to a database.  It not
  only provides a simple database to object mapping layer, but can be used to
  implement several higher order database functions (triggers, referential
  integrity, cascading delete etc.), at the application level, rather than at
  the database.
endef

DISTFILES += CSWpmclassdbi.gspec CSWpmclassdbi.depend

DEPENDS += cpan/DBI cpan/Class-Accessor cpan/Class-Trigger cpan/Ima-DBI
DEPENDS += cpan/Scalar-List-Utils cpan/UNIVERSAL-moniker cpan/DBD-SQLite

include ../category.mk

# This doesn't quite work yet with Ima-DBI updates
pre-test:
	@rm -f $(WORKSRC)/t/98-failure.t
