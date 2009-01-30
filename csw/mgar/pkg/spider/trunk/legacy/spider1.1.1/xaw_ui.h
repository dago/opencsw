/*
 *	Spider
 *
 *	(c) Copyright 1989, Donald R. Woods and Sun Microsystems, Inc.
 *	(c) Copyright 1990, David Lemke and Network Computing Devices Inc.
 *
 *	See copyright.h for the terms of the copyright.
 *
 *	@(#)xaw_ui.h	2.2	90/04/30
 *
 */

/*
 * Athena widget interface definitions
 */

#include	<X11/Intrinsic.h>
#include	<X11/StringDefs.h>

#include	<X11/Xaw/Command.h>
#include	<X11/Xaw/Box.h>
#include	<X11/Xaw/AsciiText.h>
#include	<X11/Xaw/Paned.h>
#include	<X11/Xaw/Viewport.h>
#include	<X11/Xaw/MenuButton.h>
#include	<X11/Xaw/SimpleMenu.h>
#include	<X11/Xaw/Sme.h>
#include	<X11/Xaw/SmeBSB.h>

#include	<X11/Xaw/Cardinals.h>

extern	void		score_handler(),
			backup_handler(),
			expand_handler(),
			locate_handler(),
			file_handler(),
			help_handler(),
			change_help(),
			newgame_handler(),
			confirm_callback();

extern	void		xaw_redraw_table(),
			xaw_button_press(),
			xaw_button_release(),
			xaw_resize(),
			xaw_key_press();

extern Widget		create_help_popup();

extern	Widget	file,
		toplevel,
		confirm_box,
		confirm_label,
		helptext;
