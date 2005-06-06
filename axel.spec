Summary:	A light Linux download accelerator
Summary(pl):	Niewielki dopalacz ¶ci±gania plików
Name:		axel
Version:	1.0b
Release:	2
License:	GPL
Group:		Networking/Utilities
Source0:	http://wilmer.gaast.net/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	679da19b47570f7ddff1e7958d5df97f
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-etc_dir.patch
URL:		http://wilmer.gaast.net/main.php/axel.html
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program downloads a file from a FTP/HTTP through multiple
connections, managed by one single thread, storing all the data to one
file. This is because I think it's more efficient.

%description -l pl
Ten program ¶ci±ga pliki przez FTP/HTTP korzystaj±c w wielu
równoczesnych po³±czeñ, zarz±dzanych przez pojedynczy w±tek, zapisuj±c
wszystkie dane w jednym pliku. Dlatego powinien byæ bardzo efektywny.

%prep
%setup  -q
%patch1 -p1

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
