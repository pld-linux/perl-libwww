#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	WWW
%define		pnam	libwww-perl
Summary:	libwww-perl - a simple and consistent API to the World-Wide Web
Summary(pl):	libwww-perl - prosty i logiczny API do WWW
Name:		perl-libwww
Version:	5.802
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	198794b54d91effa200a7a82202ccaea
Patch0:		%{name}-lwp_download_dest_dir_support.patch
URL:		http://search.cpan.org/dist/libwww-perl/
BuildRequires:	perl(Net::FTP) >= 2.58
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-HTML-Parser >= 3.33
BuildRequires:	perl-MIME-Base64 >= 2.1
BuildRequires:	perl-URI >= 1.10
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-libnet
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	perl-libwww-perl

# modules not always required
%define	_noautoreq 'perl(HTML::Parse)' 'perl(HTML::FormatPS)' 'perl(HTML::FormatText)' 'perl(HTTP::GHTTP)' 'perl(IO::Socket::SSL)' 'perl(Mail::Internet)' 'perl(Authen::NTLM)'

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
%patch0 -p0

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
