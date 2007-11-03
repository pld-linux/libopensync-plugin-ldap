Summary:	OpenSync Plugin for LDAP
Summary(pl.UTF-8):	Wtyczka LDAP do OpenSync
Name:		libopensync-plugin-ldap
Version:	0.22
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.bz2?format=raw
# Source0-md5:	9a37bd9ae84fcba2f72be802d278cdfc
URL:		http://www.opensync.org/
BuildRequires:	cyrus-sasl-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libgcrypt-devel >= 1.1.91
BuildRequires:	libopensync-devel >= %{version}
BuildRequires:	libxml2-devel
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync Plugin for LDAP.

%description -l pl.UTF-8
Wtyczka LDAP do OpenSync.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/opensync/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/opensync/plugins/ldap_plugin.so
%{_datadir}/opensync/defaults/ldap-sync
