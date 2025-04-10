%define module pylibacl
# disable test on abf
%bcond_with test

Name:		python-pylibacl
Version:	0.7.2
Release:	1
Summary:	Posix ACL module for Python
License:	LGPL-2.1-or-later
Group:		Development/Python
Url:		https://%{module}.sourceforge.net
Source0:	https://files.pythonhosted.org/packages/source/p/pylibacl/%{module}-%{version}.tar.gz

BuildRequires:	python
BuildRequires:	pkgconfig(libacl)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with test}
BuildRequires:	python%{pyver}dist(pytest)
%endif
Provides:	%{module} = %{version}-%{release}

%description
This is a Python 3.7+ extension module allows you to manipulate the
POSIX.1e Access Control Lists present in some OS/file-systems combinations

%prep
%autosetup -n %{module}-%{version} -p1

%build
# Remove bundled egg-info
rm -rf %{module}.egg-info/
env CFLAGS="%{optflags}"
%py_build

%install
%py3_install

%if %{with test}
%check
pytest
%endif

%files
%{py_platsitedir}/%{module}-%{version}*.*-info
%{py_platsitedir}/posix1e*.so
%license COPYING
%doc README.md
%doc NEWS.md
