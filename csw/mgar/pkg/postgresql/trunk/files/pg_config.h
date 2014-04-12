/*
 * pg_config.h for 32bit is distinct from pg_config.h for 64bit
 * architectures. In order to take this into account, this wrapper
 * includes the proper pg_config.h depending on the architecture.
 *
 * This header is not part of the regular postgresql headers. It has
 * been introduced due to the way things are handled in OpenCSW
 * Postgresql.
 *
 * It is required that this header works with Sun Studio compilers as
 * well as GNU GCC compilers.
 *
 * $Id$
 */

#if defined(__amd64) || defined(__sparcv9)
# include <pg_config_64.h>
#else
# include <pg_config_32.h>
#endif
