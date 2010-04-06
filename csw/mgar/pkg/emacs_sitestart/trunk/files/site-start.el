;;; load each file in site-start.d/ at startup; this happens prior to
;;; the load of both .emacs and default.el
(mapc 'load
      (directory-files "/opt/csw/share/emacs/site-lisp/site-start.d" t "\\.el\\'"))
