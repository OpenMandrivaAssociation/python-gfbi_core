%define upstream_name gfbi_core
%define name    python-%{upstream_name}
%define version 0.5
%define beta    b3
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Core files for interactive git filter branch
License:	BSD
Group: 		Development/Python
Url: 		http://pypi.python.org/pypi/gfbi_core
Source0: 	http://pypi.python.org/packages/source/g/gfbi_core/gfbi_core-%{version}%{beta}.tar.gz
Requires:       python-gitpython
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
These are the core files for interactive git filter-branch. There are two
frontends : qGitFilterBranch and gfbi.

%prep
%setup -q -n %{upstream_name}-%{version}%{beta}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS.txt CHANGELOG README.rst LICENSE.txt
%{python_sitelib}/gfbi_core
%{python_sitelib}/gfbi_core-%{version}%{beta}-py%{pyver}.egg-info
