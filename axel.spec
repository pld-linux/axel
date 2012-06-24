Summary:	An light Linux download accelerator	
Summary(pl):	Niewielki dopalacz �ci�gania plik�w
Name:		axel
Version:	0.95
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narz�dzia
Group(pt_BR):	Rede/Utilit�rios
Source0:	http://www.lintux.cx/downloads/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program downloads a file from a FTP/HTTP through multiple
connections, managed by one single thread, storing all the data to one
file. This is because I think it's more efficient.

%description -l pl
Ten program �ci�ga pliki przez FTP/HTTP korzystaj�c w wielu
r�wnoczesnych po��cze�, zarz�dzanych przez pojedynczy w�tek, zapisuj�c
wszystkie dane w jednym pliku. Dlatego powinien by� bardzo efektywny.

%prep
%setup  -q 

%build
%{__make} CFLAGS="%{rpmcflags}"

gzip -9nf TODO CHANGES README

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}

install axel $RPM_BUILD_ROOT%{_bindir}
install axel.1 $RPM_BUILD_ROOT%{_mandir}/man1
install axelrc.example $RPM_BUILD_ROOT%{_sysconfdir}/axelrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
