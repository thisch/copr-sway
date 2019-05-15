Name:           swaybg
Version:        1.0
Release:        1%{?dist}
Summary:        Wallpaper utility for Wayland compositors

License:        MIT
URL:            https://github.com/swaywm/swaybg
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  clang
BuildRequires:  meson
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  cairo-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  scdoc


%description
swaybg is a wallpaper utility for Wayland compositors. It is compatible with any Wayland compositor which implements the following Wayland protocols:
  wlr-layer-shell
  xdg-output
  xdg-shell


%prep
%autosetup


%build
%meson -Dwerror=false --auto-features=auto
%meson_build


%install
%meson_install


%check
%meson_test


%files
%{_bindir}/swaybg
%{_mandir}/man1/swaybg.1.gz

%license LICENSE
%doc README.*


%changelog
* Tue May 14 2019 Rafael Gumieri <rafael@gumieri.com> - 1.0-1
- RPM release of swayidle 1.0

