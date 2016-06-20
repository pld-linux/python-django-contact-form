#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	django-contact-form
Summary:	An extensible contact-form application for Django
Name:		python-django-contact-form
Version:	1.1
Release:	1
License:	BSD
Group:		Development/Languages
Source0:	https://pypi.python.org/packages/source/d/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	cd015803837f8fd1baa45dc7d21d7fce
URL:		http://bitbucket.org/ubernostrum/django-contact-form/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-django
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An extensible contact-form application for Django

%package -n python3-%{module}
Summary:	An extensible contact-form application for Django
Requires:	python3-django

%description -n python3-%{module}
An extensible contact-form application for Django

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/contact_form/tests
%endif

%if %{with python3}
%py3_install
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/contact_form/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst docs/
%{py_sitescriptdir}/contact_form
%{py_sitescriptdir}/django_contact_form-%{version}-py*.egg-info

%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE README.rst docs/
%{py3_sitescriptdir}/contact_form
%{py3_sitescriptdir}/django_contact_form-%{version}-py*.egg-info
