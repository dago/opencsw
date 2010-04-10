;; use php-mode for *.php files.
(autoload 'php-mode "php-mode" "Major mode for php code editing." t)
(add-to-list 'auto-mode-alist '("\\.php\\'" . php-mode))
