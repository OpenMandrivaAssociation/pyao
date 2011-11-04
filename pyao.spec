%define name pyao
%define version 0.82
%define release %mkrel 14

Summary: A wrapper for the ao libraries
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ekyo.nerim.net/software/pyogg/%{name}-%{version}.tar.bz2
#gw http://groups.google.com/group/pyogg/t/9e5e6f0971604ac1?hl=en
Patch: pyao-0.82-fix-crash-on-x86_64.patch
# (fc) 0.82-13mdv fix build with libao4 (Debian)
Patch1: pyao-0.82-libao4.patch
License: GPL
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libao-devel
BuildRequires: libpython-devel
Url: http://ekyo.nerim.net/software/pyogg/index.html

%description
This is a wrapper for libao, an audio device abstraction
library.

%prep
%setup -q
%patch -p1 -b .fix-crash
%patch1 -p1 -b .libao4

%build
python config_unix.py
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc README AUTHORS ChangeLog
%py_platsitedir/*


