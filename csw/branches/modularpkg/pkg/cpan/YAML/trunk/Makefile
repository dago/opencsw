GARNAME = YAML
GARVERSION = 0.62
CATEGORIES = cpan
AUTHOR = INGY

DESCRIPTION = YAML Aint Markup Language
define BLURB
  The YAML.pm module implements a YAML Loader and Dumper based on the YAML 1.0
  specification. YAML is a generic data serialization language that is
  optimized for human readability. It can be used to express the data
  structures of most modern programming languages. (Including Perl!!!)
endef

DISTFILES = $(call admfiles,CSWpmyaml,prototype)

# Don't ask questions
PATCHFILES += build.diff

include gar/category.mk
