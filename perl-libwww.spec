%include	/usr/lib/rpm/macros.perl
%define		pdir	WWW
%define		pnam	libwww-perl
Summary:	LIBWWW Perl module
Summary(cs):	Modul LIBWWW pro Perl
Summary(da):	Perlmodul LIBWWW
Summary(de):	LIBWWW Perl Modul
Summary(es):	Módulo de Perl LIBWWW
Summary(fr):	Module Perl LIBWWW
Summary(it):	Modulo di Perl LIBWWW
Summary(ja):	LIBWWW Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	LIBWWW ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul LIBWWW
Summary(pl):	Modu³ Perla LIBWWW
Summary(pt):	Módulo de Perl LIBWWW
Summary(pt_BR):	Módulo Perl LIBWWW
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl LIBWWW
Summary(sv):	LIBWWW Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl LIBWWW
Summary(zh_CN):	LIBWWW Perl Ä£¿é
Name:		perl-libwww
Version:	5.65
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
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
%define	_noautoreq "perl(HTML::Parse)" "perl(HTML::FormatPS)" "perl(HTML::FormatText)" "perl(HTTP::GHTTP)" "perl(IO::Socket::SSL)" "perl(Mail::Internet)"

%description
LIBWWW is a collection of Perl modules which provides a simple and
consistent programming interface (API) to the World-Wide Web.

%description -l pl
LIBWWW jest kolekcj± modu³ów Perla, które dostaczaj± proste API do
WWW (World-Wide Web).

%prep
%setup -q -n libwww-perl-%{version}

%build
perl Makefile.PL </dev/null
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%{perl_sitelib}/*.pm
%{perl_sitelib}/File/*
%{perl_sitelib}/HTML/*
%{perl_sitelib}/HTTP/*
%{perl_sitelib}/Net/*
%{perl_sitelib}/LWP
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
