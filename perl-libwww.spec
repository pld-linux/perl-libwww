%define	perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)

Name:		perl-libwww
Version:	5.44
Release:	2
Vendor:		Mailing List <libwww-perl@ics.uci.edu>
Source:         libwww-perl-%{version}.tar.gz
Group:		Utilities/Text
Copyright:	Free
Summary:	Perl LIBWWW module
Summary(pl):	Modu³ perla LIBWWW
BuildRoot:	/tmp/%{name}-%{version}-root
BuildRequires:	perl >= 5.005_61
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-HTML-Parser
Requires:	perl
Requires:	%{perl_sitelib}
Requires:	perl-HTML-Parser 
Requires:	perl-MIME-Base64
Requires:	perl-Digest-MD5 
Requires:	perl-libnet 

%description
Libwww-perl is a collection of Perl modules which provides a simple
and consistent programming interface (API) to the World-Wide Web.

%description -l pl
Libwww-perl jest kolekcj± modu³ów Perla, które dostaczaj± proste
API do WWW (World-Wide Web).

%prep
%setup -q -n libwww-perl-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_archlib}

make install \
	DESTDIR=$RPM_BUILD_ROOT

(  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/libwww-perl/
   sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
   mv .packlist.new .packlist
)
      
gzip -9nf README TODO $RPM_BUILD_ROOT%{_mandir}/man{1,3}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz TODO.gz
%{perl_sitelib}/*.pm
%{perl_sitelib}/*.pod
%{perl_sitelib}/Bundle/*
%{perl_sitelib}/File/*
%{perl_sitelib}/HTTP/*
%{perl_sitelib}/LWP
%{perl_sitelib}/WWW
%{perl_sitearch}/auto/libwww-perl
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man*/*
