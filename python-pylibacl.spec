%define rname pylibacl

Summary:	Posix ACL module for Python
Name:		python-%{rname}
Version:	0.5.3
Release:	2
License:	GPLv2
Group:		Development/Python
Url:		http://%{rname}.sourceforge.net
Source0:	https://files.pythonhosted.org/packages/26/e8/a34474fae8a3a5cf9973bccebc833aa8828d5197f85d9e4b12c5ba0bad41/pylibacl-0.5.3.tar.gz
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

