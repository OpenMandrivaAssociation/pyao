Summary:	A wrapper for the ao libraries
Name:		pyao
Version:	0.82
Release:	17
Source0:	http://ekyo.nerim.net/software/pyogg/%{name}-%{version}.tar.gz
#gw http://groups.google.com/group/pyogg/t/9e5e6f0971604ac1?hl=en
Patch:		pyao-0.82-fix-crash-on-x86_64.patch
# (fc) 0.82-13mdv fix build with libao4 (Debian)
Patch1:		pyao-0.82-libao4.patch
License:	GPL
Group:		Development/Python
BuildRequires:	libao-devel
BuildRequires:	python-devel
Url:	https://ekyo.nerim.net/software/pyogg/index.html

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
python setup.py install --root=%{buildroot}

%files 
%doc README AUTHORS ChangeLog
%{py_platsitedir}/*




