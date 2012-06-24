%include	/usr/lib/rpm/macros.perl
Summary:	Perl LIBWWW module
Summary(pl):	Modu� perla LIBWWW
Name:		perl-libwww
Version:	5.47
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	libwww-perl-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.005_03-14
%requires_eq    perl
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-HTML-Format
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-MailTools
BuildRequires:	perl-URI
BuildRequires:	perl-libnet
BuildRequires:	perl-IO-Socket-SSL
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libwww-perl is a collection of Perl modules which provides a simple
and consistent programming interface (API) to the World-Wide Web.

%description -l pl
Libwww-perl jest kolekcj� modu��w Perla, kt�re dostaczaj� proste API
do WWW (World-Wide Web).

%prep
%setup -q -n libwww-perl-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

(  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/libwww-perl/
   sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
   mv .packlist.new .packlist
)
      
gzip -9nf README TODO $RPM_BUILD_ROOT%{_mandir}/man{1,3}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO}.gz
%{perl_sitelib}/*.pm
%{perl_sitelib}/*.pod
%{perl_sitelib}/Bundle/*
%{perl_sitelib}/File/*
%{perl_sitelib}/HTML/*
%{perl_sitelib}/HTTP/*
%{perl_sitelib}/LWP
%{perl_sitelib}/WWW
%{perl_sitearch}/auto/libwww-perl
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man*/*
