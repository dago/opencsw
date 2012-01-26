NAME = Readonly
VERSION = 1.03
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = ROODE

DESCRIPTION = Readonly - Facility for creating read-only scalars, arrays, hashes.
define BLURB
	This is a facility for creating non-modifiable variables. This is useful for
	configuration files, headers, etc. It can also be useful as a development and
	debugging tool, for catching updates to variables that should not be changed.

	If any of the values you pass to Scalar, Array, or Hash are references, then
	those functions recurse over the data structures, marking everything as
	Readonly. Usually, this is what you want: the entire structure nonmodifiable.
	If you want only the top level to be Readonly, use the alternate Scalar1,
	Array1 and Hash1 functions.

	Please note that most users of Readonly will also want to install a companion
	module Readonly::XS. See the "CONS" section below for more details.
endef

PACKAGES = CSWpmreadonly
CATALOGNAME = pm_readonly

ARCHALL = 1
LICENSE = README

include gar/category.mk
