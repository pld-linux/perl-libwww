%define		perl_sitelib   %(eval "`perl -V:installsitelib`"; echo $installsitelib)

%define name perl-libwww
%define version 5.43
%define release 1
%define builddir $RPM_BUILD_DIR/libwww-perl-5.35
Name:		perl-libwww
Version:	5.44
Release:	1.1
Source:         libwww-perl-%{version}.tar.gz
#Patch0:		Makefile.patch
Group:		Utilities/Text
Copyright:	Free
Summary:	Perl LIBWWW module
BuildPreReq:	perl
BuildPrereq:	perl-URI
BuildPrereq:	perl-MIME-Base64
BuildPrereq:	perl-libnet
BuildPrereq:	perl-HTML-Parser
BuildPrereq:	perl-Digest-MD5
Requires:	perl
Requires:	perl-HTML-Parser
Requires:	perl-MIME-Base64
Requires:	perl-Digest-MD5
Requires:	perl-libnet 
Requires:	perl-URI
#Requires:	perl-Data-Dumper
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Libwww-perl is a collection of Perl modules which provides a simple
and consistent programming interface (API) to the World-Wide Web.

%prep
%setup -q -n libwww-perl-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{perl_sitearch} \
	$RPM_BUILD_ROOT%{_mandir}/man3 \
	$RPM_BUILD_ROOT/%{perl_archlib}

make \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	INSTALLMAN3DIR=$RPM_BUILD_ROOT%{_mandir}/man3 \
	INSTALLMAN1DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	install

rm -f $RPM_BUILD_ROOT%{_bindir}/{GET,POST,HEAD}
ln -s lwp-request $RPM_BUILD_ROOT%{_bindir}/GET
ln -s lwp-request $RPM_BUILD_ROOT%{_bindir}/POST
ln -s lwp-request $RPM_BUILD_ROOT%{_bindir}/HEAD

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/libwww-perl
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%dir %{perl_sitelib}/
%{perl_sitelib}/*.pm
%{perl_sitelib}/*.pod
%{perl_sitelib}/File
%{perl_sitelib}/HTTP
%{perl_sitelib}/LWP
%{perl_sitelib}/WWW
%{perl_sitelib}/Bundle/*

%{perl_sitearch}/auto/libwww-perl

%{_mandir}/man*/*
