NAME = Calendar-Simple
VERSION = 1.21
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DAVECROSS

DESCRIPTION = Perl extension to create simple calendars
define BLURB
    This function returns a data structure representing the dates in a month. The 
    data structure returned is an array of array references. The first level array 
    represents the weeks in the month. The second level array contains the actual days.
endef

# CSWpmcalendarsimp is the old package.  It is empty and depends on the new one
PACKAGES = CSWpmcalendarsimple CSWpmcalendarsimp
CATALOGNAME_CSWpmcalendarsimple = pm_calendarsimple
CATALOGNAME_CSWpmcalendarsimp   = pm_calendarsimp

SPKG_DESC_CSWpmcalendarsimple = $(DESCRIPTION)
SPKG_DESC_CSWpmcalendarsimp   = Empty stub depending on new package CSWpmcalendarsimple

RUNTIME_DEP_PKGS_CSWpmcalendarsimp = CSWpmcalendarsimple

LICENSE=files/COPYING

PKGFILES_CSWpmcalendarsimp = NOFILES
ARCHALL = 1


include gar/category.mk
