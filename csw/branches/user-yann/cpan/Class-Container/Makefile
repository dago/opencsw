GARNAME = Class-Container
GARVERSION = 0.12
CATEGORIES = cpan
AUTHOR = KWILLIAMS

DESCRIPTION = glues object frameworks together transparently
define BLURB
  This class facilitates building frameworks of several classes that
  inter-operate. It was first designed and built for HTML::Mason, in which the
  Compiler, Lexer, Interpreter, Resolver, Component, Buffer, and several other
  objects must create each other transparently, passing the appropriate
  parameters to the right class, possibly substituting other subclasses for
  any of these objects.
endef

DISTFILES += CSWpmclscontainer.gspec CSWpmclscontainer.depend

DEPENDS += cpan/Params-Validate

include ../category.mk
