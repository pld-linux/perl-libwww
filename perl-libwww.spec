%include	/usr/lib/rpm/macros.perl
Summary:	Perl LIBWWW module
Summary(pl):	Modu� perla LIBWWW
Name:		perl-libwww
Version:	5.61
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/WWW/libwww-perl-%{version}.tar.gz
Patch0:		%{name}-Digest-MD5.patch
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-URI
BuildRequires:	perl-libnet
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# modules not always required
%define	_noautoreq "perl(HTML::Parse)" "perl(HTML::FormatPS)" "perl(HTML::FormatText)" "perl(HTTP::GHTTP)" "perl(IO::Socket::SSL)" "perl(Mail::Internet)"

%description
Libwww-perl is a collection of Perl modules which provides a simple
and consistent programming interface (API) to the World-Wide Web.

%description -l pl
Libwww-perl jest kolekcj� modu��w Perla, kt�re dostaczaj� proste API
do WWW (World-Wide Web).

%prep
%setup -q -n libwww-perl-%{version}
%patch0 -p1

%build
perl Makefile.PL </dev/null
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/*.pm
%{perl_sitelib}/*.pod
%{perl_sitelib}/File/*
%{perl_sitelib}/HTML/*
%{perl_sitelib}/HTTP/*
%{perl_sitelib}/Net/*
%{perl_sitelib}/LWP
%{perl_sitelib}/WWW
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/[FHLWl]*
