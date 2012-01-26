NAME = openmpi
VERSION = 1.4.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A High Performance Message Passing Library
define BLURB
  Long description
endef

MASTER_SITES = http://www.open-mpi.org/software/ompi/v$(GNOME_SUBV)/downloads/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# openmpi requires sparcv8plus
REQUESTED_ISAS = sparcv8plus sparcv9 i386 amd64

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
