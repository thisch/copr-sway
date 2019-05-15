Name:       rootbar
Version:    0.0.0.r117
Release:    0%{?dist}
Summary:    Bar for wlroots based wayland compositors such as sway.
License:    MIT
Group:      System/GUI/Other
URL:        https://hg.sr.ht/~scoopta/rootbar
Source0:    https://github.com/gumieri/rootbar/archive/master.tar.gz

BuildRequires:	gcc
BuildRequires:	mercurial
BuildRequires:	gtk3
BuildRequires:	pkgconfig(gtk+-3.0)
# BuildRequires:	json-c
BuildRequires:	json-c-devel
# BuildRequires:	gtkmm30-devel
# BuildRequires:	jsoncpp-devel
# BuildRequires:	libappindicator-gtk3-devel
# BuildRequires:	libdbusmenu-gtk3-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	wayland-devel
Recommends:     sway

%description
Root Bar is a bar for wlroots based wayland compositors such as sway and was designed to address the lack of good bars for wayland.

%prep
%autosetup -n %{name}-master

%build
cd Release
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
cp Release/rootbar %{buildroot}%{_bindir}/rootbar

%files
%license COPYING.md
%doc README.md
/usr/bin/rootbar

%changelog
* Wed May 15 2019 Rafael Gumieri <rafael@gumieri.com> - 0.0.0.r117.7119b6b34dc7-0
- Update build.

* Mon Apr 15 2019 Rafael Gumieri <rafael@gumieri.com> - 0.0.0.r98.63ee1eed0bfc-0
- Create build.
