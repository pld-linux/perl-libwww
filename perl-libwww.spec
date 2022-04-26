#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses network)
#
%define		pdir	WWW
%define		pnam	libwww-perl
Summary:	libwww-perl - a simple and consistent API to the World-Wide Web
Summary(pl.UTF-8):	libwww-perl - prosty i logiczny API do WWW
Name:		perl-libwww
Version:	6.64
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/O/OA/OALDERS/%{pnam}-%{version}.tar.gz
# Source0-md5:	1383174f9589c33e0fb67f73eb841451
URL:		https://metacpan.org/release/libwww-perl
BuildRequires:	perl-CPAN-Meta-Requirements >= 2.120_620
BuildRequires:	perl-devel >= 1:5.8.8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(Net::FTP) >= 2.58
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-Encode >= 2.12
BuildRequires:	perl-Encode-Locale
BuildRequires:	perl-File-Listing >= 6
BuildRequires:	perl-HTML-Parser >= 3.33
BuildRequires:	perl-HTTP-Cookies >= 6
BuildRequires:	perl-HTTP-Daemon >= 6.12
BuildRequires:	perl-HTTP-Date >= 6
BuildRequires:	perl-HTTP-Message >= 6.07
BuildRequires:	perl-HTTP-Negotiate >= 6
BuildRequires:	perl-LWP-MediaTypes >= 6
BuildRequires:	perl-MIME-Base64 >= 2.1
BuildRequires:	perl-Net-HTTP >= 6.18
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Needs
BuildRequires:	perl-Test-RequiresInternet
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-URI >= 1.10
BuildRequires:	perl-WWW-RobotRules >= 6
BuildRequires:	perl-libnet
%endif
Requires:	perl-File-Listing >= 6
Requires:	perl-HTTP-Cookies >= 6
Requires:	perl-HTTP-Daemon >= 6.12
Requires:	perl-HTTP-Date >= 6
Requires:	perl-HTTP-Message >= 6
Requires:	perl-HTTP-Negotiate >= 6
Requires:	perl-LWP-MediaTypes >= 6
Requires:	perl-MIME-Base64 >= 2.1
Requires:	perl-Net-HTTP >= 6.18
Requires:	perl-URI >= 1.10
Requires:	perl-WWW-RobotRules >= 6
Provides:	perl(LWP::Debug::TraceHTTP::Socket) = %{version}
Provides:	perl(LWP::Protocol::http::Socket) = %{version}
Provides:	perl(LWP::Protocol::http::SocketMethods) = %{version}
Obsoletes:	perl-libwww-perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# modules not always required
%define	_noautoreq_perl	HTTP::GHTTP Authen::NTLM

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

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

for file in GET HEAD POST; do
	ln -sf lwp-request $RPM_BUILD_ROOT%{_bindir}/$file
	echo '.so lwp-request.1p' > $RPM_BUILD_ROOT%{_mandir}/man1/$file.1p
done
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/libwww/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.SSL
%attr(755,root,root) %{_bindir}/GET
%attr(755,root,root) %{_bindir}/HEAD
%attr(755,root,root) %{_bindir}/POST
%attr(755,root,root) %{_bindir}/lwp-*
%{perl_vendorlib}/LWP.pm
%{perl_vendorlib}/LWP/Authen
%{perl_vendorlib}/LWP/ConnCache.pm
%{perl_vendorlib}/LWP/Debug.pm
%dir %{perl_vendorlib}/LWP/Debug
%{perl_vendorlib}/LWP/Debug/TraceHTTP.pm
%{perl_vendorlib}/LWP/DebugFile.pm
%{perl_vendorlib}/LWP/MemberMixin.pm
%{perl_vendorlib}/LWP/Protocol.pm
%{perl_vendorlib}/LWP/Protocol
%{perl_vendorlib}/LWP/RobotUA.pm
%{perl_vendorlib}/LWP/Simple.pm
%{perl_vendorlib}/LWP/UserAgent.pm
%{_mandir}/man1/GET.1p*
%{_mandir}/man1/HEAD.1p*
%{_mandir}/man1/POST.1p*
%{_mandir}/man1/lwp-*.1p*
%{_mandir}/man3/LWP*.3pm*
%{_mandir}/man3/libwww::lwpcook.3pm*
%{_mandir}/man3/libwww::lwptut.3pm*
