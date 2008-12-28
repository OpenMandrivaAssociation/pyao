%define name pyao
%define version 0.82
%define release %mkrel 11

Summary: A wrapper for the ao libraries
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.andrewchatham.com/pyogg/download/%{name}-%{version}.tar.bz2
#gw http://groups.google.com/group/pyogg/t/9e5e6f0971604ac1?hl=en
Patch: pyao-0.82-fix-crash-on-x86_64.patch
License: GPL
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libao-devel
BuildRequires: libpython-devel
Url: http://www.andrewchatham.com/pyogg/

%description
This is a wrapper for libao, an audio device abstraction
library.

%prep
%setup -q
%patch -p1 -b .fix-crash

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


