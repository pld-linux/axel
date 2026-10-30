Summary:	A light Linux download accelerator
Summary(pl.UTF-8):	Niewielki dopalacz ściągania plików
Name:		axel
Version:	2.17.14
Release:	2
License:	GPL v2+ with OpenSSL exception
Group:		Networking/Utilities
Source0:	https://github.com/axel-download-accelerator/axel/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	2d12aab3b617197c272f9172f300663d
Patch0:		%{name}-etc_dir.patch
Patch1:		%{name}-http-header-bound.patch
Patch2:		%{name}-redirect-credentials.patch
Patch3:		%{name}-CVE-2026-118485.patch
URL:		https://github.com/axel-download-accelerator/axel
BuildRequires:	gettext-tools
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program downloads a file from a FTP/HTTP through multiple
connections, managed by one single thread, storing all the data to one
file. This is because I think it's more efficient.

%description -l pl.UTF-8
Ten program ściąga pliki przez FTP/HTTP korzystając w wielu
równoczesnych połączeń, zarządzanych przez pojedynczy wątek, zapisując
wszystkie dane w jednym pliku. Dlatego powinien być bardzo efektywny.

%prep
%setup  -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
%configure \
	--with-ssl=openssl

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p doc/axelrc.example $RPM_BUILD_ROOT%{_sysconfdir}/axelrc

%{__mv} $RPM_BUILD_ROOT%{_localedir}/id{_ID,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README.md
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/axelrc
%attr(755,root,root) %{_bindir}/axel
%{_mandir}/man1/axel.1*
