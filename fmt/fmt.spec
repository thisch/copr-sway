#
# spec file for package fmt
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define _suffix 5
Name:           fmt
Version:        5.3.0
Release:        0
Summary:        A modern formatting library
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
Url:            https://github.com/fmtlib/fmt
Source:         https://github.com/fmtlib/fmt/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
fmt is an open-source formatting library for C++.
It can be used as a safe and fast alternative to (s)printf and IOStreams.

%package -n libfmt%{_suffix}
Summary:        A modern formatting library
Group:          System/Libraries

%description -n libfmt%{_suffix}
fmt is an open-source formatting library for C++.
It can be used as a safe and fast alternative to (s)printf and IOStreams.

%package devel
Summary:        Development files for fmt
Group:          Development/Libraries/C and C++
Requires:       libfmt%{_suffix} = %{version}

%description devel
This package provides development files for fmt.

%prep
%autosetup

%build
%cmake
make %{?_smp_mflags}

%install
%make_install


%ldconfig_scriptlets


%files
%{_libdir}/libfmt.so.%{_suffix}*
%{!?_licensedir:%global license %%doc}
%license LICENSE.rst
%doc README.rst ChangeLog.rst CONTRIBUTING.rst

%files devel
%{_includedir}/fmt
%{_libdir}/libfmt.so
%{_libdir}/cmake/fmt

%changelog

