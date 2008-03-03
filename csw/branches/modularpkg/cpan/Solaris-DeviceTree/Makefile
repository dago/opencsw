GARNAME = Solaris-DeviceTree
GARVERSION = 0.03
CATEGORIES = cpan
AUTHOR = DAGOBERT

DESCRIPTION = access to Solaris device information.
define BLURB
  The Solaris::DeviceTree module implements access to the Solaris device
  information. The information is collected from the kernel via access to
  libdevinfo, the contents of the file "/etc/path_to_inst" and the filesystem
  entries below "/dev" and "/devices". The devicetree is presented as a
  hierarchical collection of nodes.
endef

DISTFILES += CSWpmsoldevtree.gspec

# devtree script tests don't operate correctly
TEST_SCRIPTS =

include ../category.mk
