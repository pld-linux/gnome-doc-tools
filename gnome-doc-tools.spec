Summary:	Extra tools for GDP members
Summary(pl):	Dodatkowe narzêdzia dla cz³onków GDP
Name:		gnome-doc-tools
Version:	1.0
Release:	1
License:	2000 Red Hat, Inc.
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(pl):	Aplikacje/Tekst
Source0:	http://people.redhat.com/dcm/%{name}-%{version}.tar.gz
URL:		http://people.redhat.com/dcm/software.html
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Prereq:		sgml-common
Requires:	docbook-dtd31-sgml
Requires:	docbook-dtd30-sgml
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
%configure2_13
perl -pi -e "s@/usr/lib/sgml/stylesheets/nwalsh-modular/@%{_datadir}/sgml/docbook/dsssl-stylesheets/@g" *.dsl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/gnome-customization-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install *.dtd *.cat *.dsl $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/gnome-customization-%{version}

%clean 
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/install-catalog --add /etc/sgml/gnome-customization-%{version}.cat %{_datadir}/sgml/docbook/gnome-customization-%{version}/png-support.cat > /dev/null

%postun
/usr/bin/install-catalog --remove /etc/sgml/gnome-customization-%{version}.cat %{_datadir}/sgml/docbook/gnome-customization-%{version}/png-support.cat > /dev/null

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/png2eps
%attr(755,root,root) %{_bindir}/dbnochunks
%{_mandir}/*/*
%{_datadir}/sgml/docbook/gnome-customization-%{version}
