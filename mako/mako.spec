Name:		  mako
Version:	1.4
Release:	1%{?dist}
Summary:	A lightweight notification daemon for Wayland.

License:	MIT
URL:      https://wayland.emersion.fr/mako
Source0:	https://github.com/emersion/mako/archive/v%{version}.tar.gz

Requires:       cairo
Requires:       pango
BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:  systemd-devel
BuildRequires:  wayland-devel
BuildRequires:	wayland-protocols-devel >= 1.14
BuildRequires:	cairo-devel
BuildRequires:	pango-devel
BuildRequires:	scdoc
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)

%description
%{summary}

%prep
%setup -q


%build
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README*.md
%{_bindir}/mako
%{_bindir}/makoctl
%{_mandir}/man1/mako.1.gz
%{_mandir}/man1/makoctl.1.gz


%changelog
* Fri Jul 19 2019 Rafael Gumieri <rafael@gumieri.com> - 1.4-1
- New release

* Sun Apr 21 2019 Rafael Gumieri <rafael@gumieri.com> - 1.3-1
- New release

* Sun Mar 19 2019 Rafael Gumieri <rafael@gumieri.com> - 1.2-1
- New release

* Thu Nov 22 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1-1.1
- Added missing build requisite

* Thu Nov 22 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1-1
- Initial build
