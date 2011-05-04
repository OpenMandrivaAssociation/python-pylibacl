%define rname pylibacl

Summary: 	Posix ACL module for Python
Name: 		python-%{rname}
Version: 	0.5.0
Release: 	%mkrel 2
License:	GPL
Group: 		Development/Python
URL: 		http://%{rname}.sourceforge.net
Source0: 	http://prdownloads.sourceforge.net/%{rname}/%{rname}-%{version}.tar.gz
BuildRequires:	acl-devel
BuildRequires:	python-devel
BuildRequires:	python-setuptools
Provides:	%{rname} = %{version}-%{release}
Obsoletes:	%{rname}
BuildRoot: 	%{_tmppath}/%{name}-buildroot

%description
This is an extension for Python which implements POSIX ACLs (POSIX.1e).

%prep

%setup -q -n %{rname}-%{version}

%build
env CFLAGS="%{optflags}" python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
#%doc README
