%include	/usr/lib/rpm/macros.perl
Summary:	Perl LIBWWW module
Summary(pl):	Modu³ perla LIBWWW
Name:		perl-libwww
Version:	5.50
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/WWW/libwww-perl-%{version}.tar.gz
Patch0: perl-libwww-rpmperl-automation-workaround.patch
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.6
%requires_eq    perl
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-URI
BuildRequires:	perl-libnet
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libwww-perl is a collection of Perl modules which provides a simple
and consistent programming interface (API) to the World-Wide Web.

%description -l pl
Libwww-perl jest kolekcj± modu³ów Perla, które dostaczaj± proste API
do WWW (World-Wide Web).

%prep
%setup -q -n libwww-perl-%{version}
%patch0 -p1


%build
perl Makefile.PL
%{__make} OPTIMIZE="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

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
%{perl_sitelib}/Bundle/*
%{perl_sitelib}/File/*
%{perl_sitelib}/HTML/*
%{perl_sitelib}/HTTP/*
%{perl_sitelib}/LWP
%{perl_sitelib}/WWW
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
