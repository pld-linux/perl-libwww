Name:		perl-libwww
Version:	5.44
Release:	1
Vendor:		Mailing List <libwww-perl@ics.uci.edu>
Source:         libwww-perl-%{version}.tar.gz
#Patch:		libwww-Makefile.patch
Group:		Utilities/Text
Copyright:	Free
Summary:	Perl LIBWWW module
BuildRoot:	/tmp/%{name}-%{version}-root
BuildRequires:	perl
%requires_eq	perl
Requires:	perl-HTML-Parser, perl-MIME-Base64, perl-MD5, perl-libnet, perl-Data-Dumper

%description
Libwww-perl is a collection of Perl modules which provides a simple
and consistent programming interface (API) to the World-Wide Web.

%prep
%setup -q -n libwww-perl-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL
#patch -p1 < %{PATCH}
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{perl_sitearch} \
	$RPM_BUILD_ROOT{%{_mandir}/man{1,3},%{_bindir}}

make install PREFIX=$RPM_BUILD_ROOT/usr \
	INSTALLMAN3DIR=$RPM_BUILD_ROOT%{_mandir}/man3 \
	INSTALLMAN1DIR=$RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README TODO $RPM_BUILD_ROOT%{_mandir}/man{1,3}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.gz TODO.gz
%{_libdir}/perl5/site_perl/5.005/LWP.pm
%{_libdir}/perl5/site_perl/5.005/Bundle/*.pm
%{_libdir}/perl5/site_perl/5.005/File/*.pm
%{_libdir}/perl5/site_perl/5.005/HTTP/*
%{_libdir}/perl5/site_perl/5.005/LWP/*
%{_libdir}/perl5/site_perl/5.005/WWW/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
