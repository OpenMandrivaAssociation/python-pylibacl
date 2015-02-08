%define rname pylibacl

Summary:	Posix ACL module for Python
Name:		python-%{rname}
Version:	0.5.1
Release:	8
License:	GPLv2
Group:		Development/Python
Url:		http://%{rname}.sourceforge.net
Source0:	https://github.com/downloads/iustin/pylibacl/pylibacl-%{version}.tar.gz
BuildRequires:	python-setuptools
BuildRequires:	acl-devel
BuildRequires:	pkgconfig(python3)
Provides:	%{rname} = %{version}-%{release}

%description
This is an extension for Python which implements POSIX ACLs (POSIX.1e).

%prep
%setup -qn %{rname}-%{version}

%build
env CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%{py_platsitedir}/%{rname}-%{version}-py%{py_ver}.egg-info
%{py_platsitedir}/posix1e*.so

