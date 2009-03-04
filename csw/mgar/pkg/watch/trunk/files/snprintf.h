/* $Id: system.h,v 1.1.1.1 2008/01/06 03:24:00 holger Exp $ */

#ifndef SYSTEM_H
#define SYSTEM_H

#if HAVE_CONFIG_H
#include <config.h>
#endif	/* HAVE_CONFIG_H */

#if HAVE_STDARG_H
#include <stdarg.h>
#if !HAVE_VSNPRINTF
int rpl_vsnprintf(char *, size_t, const char *, va_list);
#define vsnprintf rpl_vsnprintf
#endif	/* !HAVE_VSNPRINTF */
#if !HAVE_SNPRINTF
int rpl_snprintf(char *, size_t, const char *, ...);
#define snprintf rpl_snprintf
#endif	/* !HAVE_SNPRINTF */
#if !HAVE_VASPRINTF
int rpl_vasprintf(char **, const char *, va_list);
#define vasprintf rpl_vasprintf
#endif	/* !HAVE_VASPRINTF */
#if !HAVE_ASPRINTF
int rpl_asprintf(char **, const char *, ...);
#define asprintf rpl_asprintf
#endif	/* !HAVE_ASPRINTF */
#endif	/* HAVE_STDARG_H */
#endif	/* SYSTEM_H */
