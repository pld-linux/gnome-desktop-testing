Summary:	Running installed-tests
Summary(pl.UTF-8):	Uruchamianie testów w postaci zainstalowanej
Name:		gnome-desktop-testing
Version:	2021.1
Release:	1
License:	LGPL v2+
Group:		Development/Tools
Source0:	https://download.gnome.org/sources/gnome-desktop-testing/2021/%{name}-%{version}.tar.xz
# Source0-md5:	4c397564b36c23096d54fb2021593b3d
URL:		https://wiki.gnome.org/Initiatives/GnomeGoals/InstalledTests
BuildRequires:	glib2-devel >= 1:2.50
BuildRequires:	pkgconfig
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.50
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-desktop-testing-runner, also known as ginsttest-runner, runs
"as-installed" tests. These tests are discovered using metadata in
files named installed-tests/**/*.test, and are intended to check that
a library or program is functioning correctly and has been installed
correctly by a system integrator such as an OS distributor or system
administrator.

%description -l pl.UTF-8
gnome-desktop-testing-runner, znany także jako ginsttest-runner,
uruchamia testy w postaci zainstalowanej. Testy te są odnajdywane przy
użyciu metadanych w plikach o nazwach installed-tests/**/*.test i
służą sprawdzeniu, czy biblioteka lub program działa poprawnie i
został zainstalowany poprawnie przez integratora systemów, takiego
jak dystrybutor lub administrator.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ginsttest-runner
%attr(755,root,root) %{_bindir}/gnome-desktop-testing-runner
%{_mandir}/man1/ginsttest-runner.1*
%{_mandir}/man1/gnome-desktop-testing-runner.1*
