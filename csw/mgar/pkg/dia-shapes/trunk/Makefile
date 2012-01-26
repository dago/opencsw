# $Id$
NAME = dia-shapes
VERSION = 1.0
CATEGORIES = category
GARTYPE = v2

DESCRIPTION = Shapes for dia
define BLURB
endef

SHAPES  = building_site
SHAPES += central_data_processing
SHAPES += chemistry_lab
SHAPES += Circuit2
SHAPES += cmos
SHAPES += digital
SHAPES += edpc
SHAPES += electric2
SHAPES += electronic
SHAPES += gradient
SHAPES += lst
SHAPES += optics
SHAPES += Racks
SHAPES += renewable_energy
SHAPES += scenegraph
SHAPES += value_stream_mapping

SHAPE_DESC_building_site           = Building site shapes
SHAPE_DESC_central_data_processing = Central data processing shapes by Leonardo Oceano Martins
SHAPE_DESC_chemistry_lab           = chemistry lab shapes by Ryan Stewart
SHAPE_DESC_Circuit2                = Additional Circuit shapes by Terry Sturtevant
SHAPE_DESC_cmos                    = CMOS shapes by Jason Klaus
SHAPE_DESC_digital                 = Digital shapes by Jason Klaus
SHAPE_DESC_edpc                    = EPC shapes
SHAPE_DESC_electric2               = Additional electronic shapes by Manoj Rawat
SHAPE_DESC_electronic              = Electronic shapes by Jaroslav Benkovsky
SHAPE_DESC_gradient                = Gradient shapes
SHAPE_DESC_lst                     = Living Systems Theory shapes by Ian Smith
SHAPE_DESC_optics                  = Optics shapes by Johann Kellerman
SHAPE_DESC_Racks                   = Server rack shapes by Jaroslav Benkovsky
SHAPE_DESC_renewable_energy        = Renewable energy shapes by W. Martin Borgert
SHAPE_DESC_scenegraph              = Scene graph shapes by Alejandro Aguilar Sierra
SHAPE_DESC_value_stream_mapping    = Value stream mapping

MASTER_SITES = $(foreach S,$(SHAPES),http://dia-installer.de/shapes/$S/)
DISTFILES  = $(foreach S,$(SHAPES),$S.zip)

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# /opt/csw/share/dia/shapes

include gar/category.mk
