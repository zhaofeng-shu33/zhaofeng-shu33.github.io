# Change system language
2021/4/4

I want to change the system language of debian
operating system to Japanese. The following
steps are needed.

1. Change to `sudo`. Generating the new locale by editing `/etc/locale.gen`. and run the program `locale-gen`. After that, choose
the system language in the *Setting* UI.
2. Log out of debian and log back in. Install additional program,
including `libreoffice-l10n-ja`, `libreoffice-help-ja`, `firefox-esr-l10n-ja`.