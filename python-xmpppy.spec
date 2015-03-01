Summary:	Jabber/XMPP package for Python
Summary(pl.UTF-8):	Biblioteka Jabber/XMPP dla Pythona
Name:		python-xmpppy
Version:	0.4.1
Release:	4
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/xmpppy/xmpppy-%{version}.tar.gz
# Source0-md5:	ca36d685643f2c56ab07323a09ece9e4
URL:		http://xmpppy.sourceforge.net/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a Python interface to XMPP and Jabber protocols.

%description -l pl.UTF-8
Ten pakiet udostępnia interfejs Pythona do protokołów XMPP i Jabber.

%prep
%setup -qn xmpppy-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%dir %{py_sitescriptdir}/xmpp
%{py_sitescriptdir}/xmpp/*.py[co]
%{py_sitescriptdir}/*.egg-info
