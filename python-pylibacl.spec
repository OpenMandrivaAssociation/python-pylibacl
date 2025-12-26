%define module pylibacl
%bcond test 1

Name:		python-pylibacl
Version:	0.7.3
Release:	1
Summary:	Posix ACL module for Python
License:	LGPL-2.1-or-later
Group:		Development/Python
URL:		https://github.com/iustin/pylibacl
Source0:	https://files.pythonhosted.org/packages/source/p/pylibacl/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	pkgconfig(libacl)
BuildRequires:	pkgconfig(python)
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
# Remove bundled egg-info
rm -rf %{module}.egg-info/

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{ldflags} -lpython%{py_ver}"
%py_build

%install
%py_install

%if %{with test}
%check
export CI=true
export PYTHONPATH=%{buildroot}%{python_sitearch}:%{python_sitearch}
pytest
%endif

%files
%{py_platsitedir}/%{module}-%{version}*.*-info
%{py_platsitedir}/posix1e*.so
%license COPYING
%doc README.md
%doc NEWS.md
