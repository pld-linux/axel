Summary:	A light Linux download accelerator
Summary(pl.UTF-8):	Niewielki dopalacz ściągania plików
Name:		axel
Version:	2.3
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://alioth.debian.org/frs/download.php/2717/%{name}-%{version}.tar.gz
# Source0-md5:	6f49813ffc1dd10829d74b73712cb5ed
Patch0:		%{name}-etc_dir.patch
URL:		http://axel.alioth.debian.org/
BuildRequires:	gettext-devel
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
%patch0 -p1

%build
# it doesn't use autoconf
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--etcdir=%{_sysconfdir} \
	--mandir=%{_mandir} \
	--locale=%{_datadir}/locale \
	--i18n=1

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir},%{_datadir}/locale}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGES README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(zh_CN) %{_mandir}/zh_CN/man1/*
