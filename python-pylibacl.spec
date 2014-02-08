%define rname pylibacl

Summary: 	Posix ACL module for Python
Name: 		python-%{rname}
Version: 	0.5.0
Release: 	6
License:	GPL
Group: 		Development/Python
URL: 		http://%{rname}.sourceforge.net
Source0: 	http://prdownloads.sourceforge.net/%{rname}/%{rname}-%{version}.tar.gz
BuildRequires:	acl-devel
BuildRequires:	python-devel
BuildRequires:	python-setuptools
Provides:	%{rname} = %{version}-%{release}
Obsoletes:	%{rname}

%description
This is an extension for Python which implements POSIX ACLs (POSIX.1e).

%prep
%setup -q -n %{rname}-%{version}

%build
env CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%{py_platsitedir}/%{rname}-%{version}-py%{py_ver}.egg-info
%{py_platsitedir}/posix1e.so


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-2mdv2011.0
+ Revision: 668027
- mass rebuild

* Wed Mar 03 2010 Frederik Himpe <fhimpe@mandriva.org> 0.5.0-1mdv2011.0
+ Revision: 514023
- Update to new version 0.5.0

* Sat Dec 27 2008 Funda Wang <fwang@mandriva.org> 0.4.0-2mdv2009.1
+ Revision: 319761
- rebuild for new python

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.0-1mdv2009.1
+ Revision: 305901
- update to new version 0.4.0

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.2.2-2mdv2009.0
+ Revision: 219582
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.2-1mdv2008.0
+ Revision: 55865
- update to new version 0.2.2

* Fri Jun 29 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-3mdv2008.0
+ Revision: 45748
- Import python-pylibacl



* Fri Jun 29 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-3mdv2008.0
- renamed from pylibacl to python-pylibacl

* Sun Apr 03 2005 Michael Scherer <misc@mandrake.org> 0.2.1-2mdk
- Rebuild for new python

* Tue Jul 20 2004 Buchan Milne <bgmilne@linux-mandrake.com> 0.2.1-1mdk
- First Mandrake package
