Name:           wl-clipboard
Version:        1.0.0
Release:        1%{?dist}
Summary:        Wayland clipboard utilities
Group:          User Interface/X
License:        GPL-3.0
URL:            https://github.com/bugaevc/wl-clipboard
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  wayland-devel
Recommends:     xdg-utils
Recommends:     mailcap

%description
wl-clipboard provides two command-line Wayland clipboard utilities, wl-copy and wl-paste, that let you easily copy data between the clipboard and Unix pipes, sockets, files and so on.

%prep
%autosetup -p 1 -n %{name}-%{version}
mkdir %{_target_Platform}

%build
meson build
ninja -C build

%install
mkdir -p %{buildroot}%{_bindir}
DESTDIR=%{buildroot} ninja -C build install

%files
%license COPYING
%doc README.md
/usr/local/bin/*
/usr/local/share/man/man1/*

%changelog
* Fri Mar 29 2019 Rafael Gumieri <rafael@gumieri.com> - 1.0-1
- First config
