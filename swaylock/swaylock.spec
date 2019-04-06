Name:           swaylock
Version:        1.3
Release:        1%{?dist}
Summary:        Screen locker for Wayland

License:        MIT
URL:            https://github.com/swaywm/swaylock
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  clang
BuildRequires:  meson
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  pango-devel
BuildRequires:  cairo-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  pam-devel
BuildRequires:  scdoc

Requires:       cairo
Requires:       gdk-pixbuf2


%description
swaylock is a screen locking utility for Wayland compositors.


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
%{_bindir}/swaylock
%{_datadir}/bash-completion/completions/swaylock
%{_datadir}/fish/completions/swaylock.fish
%{_datadir}/zsh/site-functions/_swaylock

%{_mandir}/man1/swaylock.1.gz

%config %{_sysconfdir}/pam.d/swaylock

%license LICENSE
%doc README.*


%changelog
* Sat Mar  9 2019 Ian Hattendorf <ian@ianhattendorf.com> - 1.3-1
- Update to 1.3

* Sun Feb  3 2019 Aurelien Rouene <aurelien@rouene.fr> - 1.2-1
- RPM release of swaylock 1.2
