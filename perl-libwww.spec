#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	WWW
%define		pnam	libwww-perl
Summary:	libwww-perl - a simple and consistent API to the World-Wide Web
Summary(pl):	libwww-perl - prosty i logiczny API do WWW 
Name:		perl-libwww
Version:	5.69
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:  perl(Net::FTP) >= 2.58
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-URI
BuildRequires:	perl-libnet
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	perl-libwww-perl

# modules not always required
%define	_noautoreq "perl(HTML::Parse)" "perl(HTML::FormatPS)" "perl(HTML::FormatText)" "perl(HTTP::GHTTP)" "perl(IO::Socket::SSL)" "perl(Mail::Internet)" "perl(Authen::NTLM)"

%description
The libwww-perl collection is a set of Perl modules which provides a
simple and consistent application programming interface to the World-Wide
Web. The main focus of the library is to provide classes and functions
that allow you to write WWW clients. The library also contain modules
that are of more general use and even classes that help you implement
simple HTTP servers.

%description -l pl
libwww-perl jest zbiorem modu³ów Perla, dostarczaj±cych prostego API
do WWW (World-Wide Web). G³ównym zadaniem biblioteki jest udostêpnianie
klas i funkcji, pozwalaj±cych na pisanie klientów WWW. Biblioteka zawiera
tak¿e modu³y bardziej ogólnego przeznaczenia, a nawet klasy, pozwalaj±ce
na implementacjê prostego serwera HTTP.

%prep
%setup -q -n libwww-perl-%{version}

%build
perl Makefile.PL </dev/null
%{__make}

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{perl_sitelib}/*.pm
%{perl_sitelib}/File/*
%{perl_sitelib}/HTML/*
%{perl_sitelib}/HTTP/*
%{perl_sitelib}/Net/*
%{perl_sitelib}/LWP
%{perl_sitelib}/WWW/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/[^B]*
