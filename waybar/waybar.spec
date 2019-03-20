%define debug_package %{nil}
%define waybar_dir Waybar-%{version}

Name:       waybar
Version:    0.5.0
Release:    1%{?dist}
Summary:    Highly customizable Wayland bar for Sway and Wlroots based compositors.

License:    MIT
URL:        https://github.com/Alexays/Waybar
Source0:    https://github.com/Alexays/Waybar/archive/%{version}.tar.gz

BuildRequires:	meson
BuildRequires:	ninja-build
BuildRequires:	gcc-c++
BuildRequires:	libinput-devel
BuildRequires:	gtkmm30-devel
BuildRequires:	jsoncpp-devel
BuildRequires:	libappindicator-gtk3-devel
BuildRequires:	libdbusmenu-gtk3-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	wayland-devel
BuildRequires:	wlroots-devel
BuildRequires:	sway
BuildRequires:	libsigc++-devel
BuildRequires:	libnl3-devel
BuildRequires:	libudev-devel
BuildRequires:	fmt-devel
BuildRequires:	git
Requires:  sway
Requires:  wlroots
Requires:  fontawesome-fonts

%description
Current features

  Sway (Workspaces, Binding mode, Focused window name)
  Tray (Beta) #21
  Local time
  Battery
  Network
  Pulseaudio
  Memory
  Cpu load average
  Temperature
  Custom scripts
  Multiple output configuration
  And much more customizations

%prep
%autosetup -n %{waybar_dir}

%build
meson build
ninja -C build

%install
mkdir -p %{buildroot}%{_bindir}
DESTDIR=%{buildroot} ninja -C build install
mkdir -p %{buildroot}/etc/xdg/waybar/custom_modules
cp -r %{_builddir}/%{waybar_dir}/resources/custom_modules/* %{buildroot}/etc/xdg/waybar/custom_modules

%files
/usr/local/bin/*
/etc/xdg/waybar/*

%changelog
* Thu Mar 21 2019 Rafael Gumieri <rafael@gumieri.com> - 0.5.0-1
- Bump to 0.5.0

* Sun Mar  3 2019 Ian Hattendorf <ian@ianhattendorf.com> - 0.4.0-1
- Bump to 0.4.0
