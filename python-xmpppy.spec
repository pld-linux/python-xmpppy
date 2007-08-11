Summary:	Jabber/XMPP package for Python
Summary(pl.UTF-8):	Biblioteka Jabber/XMPP dla Pythona
Name:		python-xmpppy
Version:	0.4.0
Release:	2
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/xmpppy/xmpppy-%{version}.tar.gz
# Source0-md5:	bcec3068bc297e672a1d5b258090ee3d
URL:		http://xmpppy.sourceforge.net/
BuildRequires:	python-devel >= 1:2.4
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
