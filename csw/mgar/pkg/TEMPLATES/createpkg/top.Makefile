
# This is somewhat of a "stub" Makefile, for 
# directories managed by the "createpkg" TEMPLATES.
#
# Not all of targets listed here may actualy be supported by
# the subdir in question. But they are a goal

DEFAULT_DIR=trunk


# The -C means you must use gmake, unfortunately.

garchive extract configure build package:
	$(MAKE) -C  $(DEFAULT_DIR) $@

