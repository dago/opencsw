GARNAME = CGI-Application-Plugin-LogDispatch
GARVERSION = 1.00
CATEGORIES = cpan
AUTHOR = CEESHEK

DESCRIPTION = Add Log::Dispatch support to CGI::Application
define BLURB
  CGI::Application::Plugin::LogDispatch adds logging support to your
  CGI::Application modules by providing a Log::Dispatch dispatcher object that
  is accessible from anywhere in the application
endef

DISTFILES += $(call admfiles,CSWpmcgiapplogdisp,depend prototype)

DEPENDS += cpan/Log-Dispatch
DEPENDS += cpan/CGI-Application
DEPENDS += cpan/UNIVERSAL-require

include gar/category.mk
