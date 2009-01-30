/*
 *	Spider
 *
 *	(c) Copyright 1989,  Donald R. Woods and Sun Microsystems, Inc.
 *	(c) Copyright 1990, David Lemke and Network Computing Devices Inc.
 *
 *	See copyright.h for the terms of the copyright.
 *
 *	@(#)assert.h	2.1	90/04/25
 *
 */

#ifdef DEBUG
#define assert(ex)	{if (!(ex)){(void)fprintf(stderr,"Assertion \"ex\" failed: file \"%s\", line %d\n", __FILE__, __LINE__);abort();}}
#else
#define assert(ex)
#endif
