###############################################
#
# SolarisCSWEnv.Set.sh - add CSW paths to
# Openoffice Build environment variables
#
###############################################

# python is incorrectly installed, as a result
# some build parameters are not properly detected
# we manually set them
PYTHON_CFLAGS="-I/opt/csw/include/python2.5"
PYTHON_LIBS="-L/opt/csw/lib -lpython2.5"

# We want Cairo to use CSW Xrender instead of Sun native one
# so we add /opt/csw/include in the include search directory paths
CAIRO_CFLAGS="$CAIRO_CFLAGS -I/opt/csw/include"

# We add CSW paths to compiler include and 
# linker library search directory paths
SOLARINC="$SOLARINC -I/opt/csw/include" 
# we make sure /opt/csw/lib is read befire /usr/lib so
# csw pango is used instead of sun one
SOLARLIB="`echo $SOLARLIB | sed -e 's,-L/usr/lib,-L/opt/csw/lib -L/usr/lib,'`"
