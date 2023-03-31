%define rname pylibacl

Summary:	Posix ACL module for Python
Name:		python-%{rname}
Version:	0.6.0
Release:	2
License:	GPLv2
Group:		Development/Python
Url:		http://%{rname}.sourceforge.net
Source0:	https://files.pythonhosted.org/packages/09/23/ad116ac73a352ef82dba4c0a7b0536ed7b5071bd48227c211b745adcc468/pylibacl-0.6.0.tar.gz
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

