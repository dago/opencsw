GARNAME = File-chdir
GARVERSION = 0.06
CATEGORIES = cpan
AUTHOR = MSCHWERN

DESCRIPTION = a more sensible way to change directories
define BLURB
  Perl's chdir() has the unfortunate problem of being very, very, very global.
  If any part of your program calls chdir() or if any library you use calls
  chdir(), it changes the current working directory for the whole program.
  This sucks.  File::chdir gives you an alternative, $$CWD and @CWD. These two
  variables combine all the power of chdir(), File::Spec and Cwd.
endef

DISTFILES = $(call admfiles,CSWpmfilechdir,depend prototype)

include ../category.mk
