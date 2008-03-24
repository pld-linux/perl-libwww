#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	WWW
%define		pnam	libwww-perl
Summary:	libwww-perl - a simple and consistent API to the World-Wide Web
Summary(pl.UTF-8):	libwww-perl - prosty i logiczny API do WWW
Name:		perl-libwww
Version:	5.808
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	72120d9195ab1649c2d787eb1102a90c
URL:		http://search.cpan.org/dist/libwww-perl/
BuildRequires:	perl(Net::FTP) >= 2.58
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-HTML-Parser >= 3.33
BuildRequires:	perl-MIME-Base64 >= 2.1
BuildRequires:	perl-URI >= 1.10
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-libnet
BuildRequires:	rpm-perlprov >= 4.1-13
Suggests:	perl-IO-Socket-SSL
Obsoletes:	perl-libwww-perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# modules not always required
%define	_noautoreq 'perl(HTML::Parse)' 'perl(HTML::FormatPS)' 'perl(HTML::FormatText)' 'perl(HTTP::GHTTP)' 'perl(IO::Socket::SSL)' 'perl(Mail::Internet)' 'perl(Authen::NTLM)'

%description
The libwww-perl collection is a set of Perl modules which provides a
simple and consistent application programming interface to the
World-Wide Web. The main focus of the library is to provide classes
and functions that allow you to write WWW clients. The library also
contain modules that are of more general use and even classes that
help you implement simple HTTP servers.

%description -l pl.UTF-8
libwww-perl jest zbiorem modułów Perla, dostarczających prostego API
do WWW (World-Wide Web). Głównym zadaniem biblioteki jest
udostępnianie klas i funkcji, pozwalających na pisanie klientów WWW.
Biblioteka zawiera także moduły bardziej ogólnego przeznaczenia, a
nawet klasy, pozwalające na implementację prostego serwera HTTP.

%prep
%setup -q -n libwww-perl-%{version}

%build
yes | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

for file in GET HEAD POST; do
	ln -sf lwp-request $RPM_BUILD_ROOT%{_bindir}/$file
	rm -f $RPM_BUILD_ROOT%{_mandir}/man1/$file.1p
	echo '.so lwp-request.1p' > $RPM_BUILD_ROOT%{_mandir}/man1/$file.1p
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/File/*
%{perl_vendorlib}/HTML/*
%{perl_vendorlib}/HTTP/*
%{perl_vendorlib}/Net/*
%{perl_vendorlib}/LWP
%{perl_vendorlib}/WWW/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/[!B]*
