%define upstream_name gfbi_core
%define beta    b3

Name: 		python-%{upstream_name}
Version: 	0.5
Release: 	3
Summary: 	Core files for interactive git filter branch
License:	BSD
Group: 		Development/Python
Url: 		https://pypi.python.org/pypi/gfbi_core
Source0: 	http://pypi.python.org/packages/source/g/gfbi_core/gfbi_core-%{version}%{beta}.tar.gz
Requires:       python-gitpython
BuildArch:      noarch

%description
These are the core files for interactive git filter-branch. There are two
frontends : qGitFilterBranch and gfbi.

%prep
%setup -q -n %{upstream_name}-%{version}%{beta}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc AUTHORS.txt CHANGELOG README.rst LICENSE.txt
%{python_sitelib}/gfbi_core
%{python_sitelib}/gfbi_core-%{version}%{beta}-py%{py_ver}.egg-info


%changelog
* Thu Jun 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.5-1mdv2011.0
+ Revision: 688346
- import python-gfbi_core

