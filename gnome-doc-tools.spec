Summary:	Extra tools for GDP members
Summary(pl):	Dodatkowe narzêdzia dla cz³onków GDP
Name:		gnome-doc-tools
Version:	1.0
Release:	5
License:	GPL
Group:		Applications/Text
# dead
#Source0:	http://people.redhat.com/dcm/%{name}-%{version}.tar.gz
#URL:		http://people.redhat.com/dcm/software.html
# this file differs with the one from cvs.pld.org.pl
#Source0:	ftp://freeware.sgi.com/source/gnome-doc-tools/gnome-doc-tools-1.0.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5: 2d8dea2fbbc93117f13d09b8a4734563
URL:		http://freeware.sgi.com/cd-2/relnotes/gnome-doc-tools.html
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	docbook-dtd30-sgml
Requires:	docbook-dtd31-sgml
Prereq:		sgml-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	docbook-gnome-dtd10-sgml

%description
The GNOME Documentation Project has a few tools, scripts and files
necessary for creating documentation for GNOME.

%description -l pl
GNOME Documentation Project ma kilka narzêdzi, skryptów i plików
potrzebnych do tworzenia dokumentacji dla GNOME.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
perl -pi -e "s@%{_libdir}/sgml/stylesheets/nwalsh-modular/@%{_datadir}/sgml/docbook/dsssl-stylesheets/@g" *.dsl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/gnome-customization-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install *.dtd *.cat *.dsl $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/gnome-customization-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- %{name} < 1.0-4
if ! grep -q /etc/sgml/gnome-customization-%{version}-%{release}.cat /etc/sgml/catalog ; then
	/usr/bin/install-catalog --add /etc/sgml/gnome-customization-%{version}-%{release}.cat %{_datadir}/sgml/docbook/gnome-customization-%{version}/png-support.cat > /dev/null
fi

%pre
if [ -L %{_datadir}/sgml/docbook/dsssl-stylesheets ] ; then
	rm -rf %{_datadir}/sgml/docbook/dsssl-stylesheets
fi

%post
if ! grep -q /etc/sgml/gnome-customization-%{version}-%{release}.cat /etc/sgml/catalog ; then
	/usr/bin/install-catalog --add /etc/sgml/gnome-customization-%{version}-%{release}.cat %{_datadir}/sgml/docbook/gnome-customization-%{version}/png-support.cat > /dev/null
fi

%postun
if [ "$1" = 0 ]; then
	/usr/bin/install-catalog --remove /etc/sgml/gnome-customization-%{version}-%{release}.cat %{_datadir}/sgml/docbook/gnome-customization-%{version}/png-support.cat > /dev/null
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/png2eps
%attr(755,root,root) %{_bindir}/dbnochunks
%{_mandir}/*/*
%{_datadir}/sgml/docbook/gnome-customization-%{version}
