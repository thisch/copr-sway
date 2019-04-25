%define debug_package %{nil}
%define waybar_dir Waybar-%{version}

Name:       waybar
Version:    0.6.0
Release:    3%{?dist}
Summary:    Highly customizable Wayland bar for Sway and Wlroots based compositors.
License:    MIT
Group:      System/GUI/Other
URL:        https://github.com/Alexays/Waybar
Source0:    https://github.com/Alexays/Waybar/archive/%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	meson
BuildRequires:	gcc-c++
BuildRequires:	libinput-devel
BuildRequires:	gtkmm30-devel
BuildRequires:	jsoncpp-devel
BuildRequires:	libappindicator-gtk3-devel
BuildRequires:	libdbusmenu-gtk3-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	wayland-devel
BuildRequires:	sway >= 1.0
BuildRequires:  wlroots-devel >= 0.5
BuildRequires:	libsigc++-devel
BuildRequires:	libnl3-devel
BuildRequires:	libudev-devel
BuildRequires:	fmt >= 5.3.0
Recommends:     sway

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
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_sysconfdir}/xdg/waybar/
%{_bindir}/waybar

%changelog
* Thu Apr  25 2019 Rafael Gumieri <rafael@gumieri.com> - 0.6.0-1
- Bump to 0.6.0

* Mon Apr  8 2019 Rafael Gumieri <rafael@gumieri.com> - 0.5.1-3
- Remove Git and add Group

* Sun Apr  7 2019 Rafael Gumieri <rafael@gumieri.com> - 0.5.1-2
- Fix files

* Thu Mar 21 2019 Rafael Gumieri <rafael@gumieri.com> - 0.5.1-1
- Build for 0.5.1

* Thu Mar 21 2019 Rafael Gumieri <rafael@gumieri.com> - 0.5.0-1
- Bump to 0.5.0

* Sun Mar  3 2019 Ian Hattendorf <ian@ianhattendorf.com> - 0.4.0-1
- Bump to 0.4.0
