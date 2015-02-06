Summary: A wrapper for the ao libraries
Name: pyao
Version: 0.82
Release: 16
Source0: http://ekyo.nerim.net/software/pyogg/%{name}-%{version}.tar.bz2
#gw http://groups.google.com/group/pyogg/t/9e5e6f0971604ac1?hl=en
Patch: pyao-0.82-fix-crash-on-x86_64.patch
# (fc) 0.82-13mdv fix build with libao4 (Debian)
Patch1: pyao-0.82-libao4.patch
License: GPL
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libao-devel
BuildRequires: python-devel
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
python setup.py install --root=%{buildroot}

%files 
%defattr(-,root,root)
%doc README AUTHORS ChangeLog
%py_platsitedir/*




%changelog
* Fri Nov 04 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.82-14mdv2012.0
+ Revision: 717574
- rebuild

* Mon May 10 2010 Frederic Crozat <fcrozat@mandriva.com> 0.82-13mdv2011.0
+ Revision: 544423
- Patch1 (Debian): fix build with libao4

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.82-12mdv2010.0
+ Revision: 441979
- rebuild

* Sun Dec 28 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.82-11mdv2009.1
+ Revision: 320595
- rebuild for new python

* Sat Oct 11 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.82-10mdv2009.1
+ Revision: 292469
- fix a crash

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.82-9mdv2009.0
+ Revision: 259393
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.82-8mdv2009.0
+ Revision: 247252
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- remove URL from description

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Tue Nov 28 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.82-6mdv2007.0
+ Revision: 88123
- Import pyao

* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 0.82-6mdv2007.1
- update file list

* Mon Dec 05 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.82-5mdk
- Rebuild

* Sat Dec 04 2004 Michael Scherer <misc@mandrake.org> 0.82-4mdk
- Rebuild for new python

* Sat Sep 04 2004 Götz Waschk <waschk@linux-mandrake.com> 0.82-3mdk
- rebuild

