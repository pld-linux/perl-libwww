%define name perl-libwww
%define version 5.35
%define release 1
%define builddir $RPM_BUILD_DIR/libwww-perl-5.35
Name:		%{name}
Version:	%{version}
Release:	1
Vendor:		Mailing List <libwww-perl@ics.uci.edu>
Source:         libwww-perl-5.35.tar.gz
Patch0:		Makefile.patch
Group:		Utilities/Text
Copyright:	Free
Summary:	Perl LIBWWW module
BuildRoot:	/var/tmp/perl-libwww-root
Requires:	perl-HTML-Parser, perl-MIME-Base64, perl-MD5, perl-libnet, perl-Data-Dumper

%description
Libwww-perl is a collection of Perl modules which provides a simple
and consistent programming interface (API) to the World-Wide Web.

%changelog
* Thu Jul 23 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- initial RPM release

%prep
%setup -n libwww-perl-5.35

%build
perl Makefile.PL
patch -p1 < $RPM_SOURCE_DIR/Makefile.patch
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT/usr/lib/perl5/site_perl/auto/URI/URL/file
mkdir -p $RPM_BUILD_ROOT/usr/lib/perl5/man/man3
mkdir -p $RPM_BUILD_ROOT/usr/lib/perl5/site_perl/auto/LWP/UserAgent
mkdir -p $RPM_BUILD_ROOT/usr/lib/perl5/i386-linux/5.00404
mkdir -p $RPM_BUILD_ROOT/usr/lib/perl5/site_perl/WWW/RobotRules
mkdir -p $RPM_BUILD_ROOT/usr/lib/perl5/site_perl/HTTP
mkdir -p $RPM_BUILD_ROOT/usr/lib/perl5/site_perl/Bundle
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/lib/perl5/site_perl/i386-linux/auto/libwww-perl
make install PREFIX=$RPM_BUILD_ROOT/usr

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}

%files
%doc README TODO
/usr/lib/perl5/site_perl/auto/URI/URL/file/newlocal.al
/usr/lib/perl5/site_perl/auto/URI/URL/file/unix_path.al
/usr/lib/perl5/site_perl/auto/URI/URL/file/dos_path.al
/usr/lib/perl5/site_perl/auto/URI/URL/file/mac_path.al
/usr/lib/perl5/site_perl/auto/URI/URL/file/vms_path.al
/usr/lib/perl5/site_perl/auto/URI/URL/file/autosplit.ix
/usr/lib/perl5/site_perl/auto/URI/URL/newlocal.al
/usr/lib/perl5/site_perl/auto/URI/URL/strict.al
/usr/lib/perl5/site_perl/auto/URI/URL/base.al
/usr/lib/perl5/site_perl/auto/URI/URL/scheme.al
/usr/lib/perl5/site_perl/auto/URI/URL/crack.al
/usr/lib/perl5/site_perl/auto/URI/URL/abs.al
/usr/lib/perl5/site_perl/auto/URI/URL/rel.al
/usr/lib/perl5/site_perl/auto/URI/URL/as_string.al
/usr/lib/perl5/site_perl/auto/URI/URL/eq.al
/usr/lib/perl5/site_perl/auto/URI/URL/bad_method.al
/usr/lib/perl5/site_perl/auto/URI/URL/print_on.al
/usr/lib/perl5/site_perl/auto/URI/URL/autosplit.ix
/usr/lib/perl5/site_perl/auto/URI/URL/_generic/user.al
/usr/lib/perl5/site_perl/auto/URI/URL/_generic/password.al
/usr/lib/perl5/site_perl/auto/URI/URL/_generic/host.al
/usr/lib/perl5/site_perl/auto/URI/URL/_generic/port.al
/usr/lib/perl5/site_perl/auto/URI/URL/_generic/_netloc_elem.al
/usr/lib/perl5/site_perl/auto/URI/URL/_generic/epath.al
/usr/lib/perl5/site_perl/auto/URI/URL/_generic/path.al
/usr/lib/perl5/site_perl/auto/URI/URL/_generic/path_components.al
/usr/lib/perl5/site_perl/auto/URI/URL/_generic/eparams.al
/usr/lib/perl5/site_perl/auto/URI/URL/_generic/params.al
/usr/lib/perl5/site_perl/auto/URI/URL/_generic/equery.al
/usr/lib/perl5/site_perl/auto/URI/URL/_generic/query.al
/usr/lib/perl5/site_perl/auto/URI/URL/_generic/frag.al
/usr/lib/perl5/site_perl/auto/URI/URL/_generic/crack.al
/usr/lib/perl5/site_perl/auto/URI/URL/_generic/abs.al
/usr/lib/perl5/site_perl/auto/URI/URL/_generic/rel.al
/usr/lib/perl5/site_perl/auto/URI/URL/_generic/eq.al
/usr/lib/perl5/site_perl/auto/URI/URL/_generic/autosplit.ix
/usr/lib/perl5/site_perl/auto/URI/URL/http/keywords.al
/usr/lib/perl5/site_perl/auto/URI/URL/http/query_form.al
/usr/lib/perl5/site_perl/auto/URI/URL/http/autosplit.ix
/usr/lib/perl5/site_perl/auto/LWP/UserAgent/clone.al
/usr/lib/perl5/site_perl/auto/LWP/UserAgent/is_protocol_supported.al
/usr/lib/perl5/site_perl/auto/LWP/UserAgent/mirror.al
/usr/lib/perl5/site_perl/auto/LWP/UserAgent/proxy.al
/usr/lib/perl5/site_perl/auto/LWP/UserAgent/env_proxy.al
/usr/lib/perl5/site_perl/auto/LWP/UserAgent/no_proxy.al
/usr/lib/perl5/site_perl/auto/LWP/UserAgent/_need_proxy.al
/usr/lib/perl5/site_perl/auto/LWP/UserAgent/autosplit.ix
/usr/lib/perl5/site_perl/HTTP/Request/Common.pm
/usr/lib/perl5/site_perl/HTTP/Request.pm
/usr/lib/perl5/site_perl/HTTP/Headers/Util.pm
/usr/lib/perl5/site_perl/HTTP/Headers/Auth.pm
/usr/lib/perl5/site_perl/HTTP/Headers/ETag.pm
/usr/lib/perl5/site_perl/HTTP/Response.pm
/usr/lib/perl5/site_perl/HTTP/Daemon.pm
/usr/lib/perl5/site_perl/HTTP/Negotiate.pm
/usr/lib/perl5/site_perl/HTTP/Status.pm
/usr/lib/perl5/site_perl/HTTP/Message.pm
/usr/lib/perl5/site_perl/HTTP/Cookies.pm
/usr/lib/perl5/site_perl/HTTP/Headers.pm
/usr/lib/perl5/site_perl/HTTP/Date.pm
/usr/lib/perl5/site_perl/LWP/Protocol.pm
/usr/lib/perl5/site_perl/LWP/Protocol/https.pm
/usr/lib/perl5/site_perl/LWP/Protocol/nntp.pm
/usr/lib/perl5/site_perl/LWP/Protocol/http.pm
/usr/lib/perl5/site_perl/LWP/Protocol/mailto.pm
/usr/lib/perl5/site_perl/LWP/Protocol/data.pm
/usr/lib/perl5/site_perl/LWP/Protocol/file.pm
/usr/lib/perl5/site_perl/LWP/Protocol/gopher.pm
/usr/lib/perl5/site_perl/LWP/Protocol/ftp.pm
/usr/lib/perl5/site_perl/LWP/RobotUA.pm
/usr/lib/perl5/site_perl/LWP/Debug.pm
/usr/lib/perl5/site_perl/LWP/UserAgent.pm
/usr/lib/perl5/site_perl/LWP/Authen/Digest.pm
/usr/lib/perl5/site_perl/LWP/Authen/Basic.pm
/usr/lib/perl5/site_perl/LWP/MediaTypes.pm
/usr/lib/perl5/site_perl/LWP/media.types
/usr/lib/perl5/site_perl/LWP/MemberMixin.pm
/usr/lib/perl5/site_perl/LWP/Simple.pm
/usr/lib/perl5/site_perl/URI/URL/_login.pm
/usr/lib/perl5/site_perl/URI/URL/prospero.pm
/usr/lib/perl5/site_perl/URI/URL/data.pm
/usr/lib/perl5/site_perl/URI/URL/file.pm
/usr/lib/perl5/site_perl/URI/URL/gopher.pm
/usr/lib/perl5/site_perl/URI/URL/ftp.pm
/usr/lib/perl5/site_perl/URI/URL/whois.pm
/usr/lib/perl5/site_perl/URI/URL/rlogin.pm
/usr/lib/perl5/site_perl/URI/URL/telnet.pm
/usr/lib/perl5/site_perl/URI/URL/tn3270.pm
/usr/lib/perl5/site_perl/URI/URL/https.pm
/usr/lib/perl5/site_perl/URI/URL/wais.pm
/usr/lib/perl5/site_perl/URI/URL/finger.pm
/usr/lib/perl5/site_perl/URI/URL/webster.pm
/usr/lib/perl5/site_perl/URI/URL/_generic.pm
/usr/lib/perl5/site_perl/URI/URL/news.pm
/usr/lib/perl5/site_perl/URI/URL/nntp.pm
/usr/lib/perl5/site_perl/URI/URL/http.pm
/usr/lib/perl5/site_perl/URI/URL/mailto.pm
/usr/lib/perl5/site_perl/URI/Heuristic.pm
/usr/lib/perl5/site_perl/URI/Escape.pm
/usr/lib/perl5/site_perl/URI/URL.pm
/usr/lib/perl5/site_perl/WWW/RobotRules.pm
/usr/lib/perl5/site_perl/WWW/RobotRules/AnyDBM_File.pm
/usr/lib/perl5/site_perl/File/Listing.pm
/usr/lib/perl5/site_perl/LWP.pm
/usr/lib/perl5/site_perl/Bundle/LWP.pm
/usr/lib/perl5/site_perl/lwpcook.pod
/usr/man/man1/lwp-download.1
/usr/man/man1/lwp-mirror.1
/usr/man/man1/lwp-request.1
/usr/man/man1/lwp-rget.1
/usr/lib/perl5/man/man3/URI::Heuristic.3
/usr/lib/perl5/man/man3/HTTP::Negotiate.3
/usr/lib/perl5/man/man3/HTTP::Request::Common.3
/usr/lib/perl5/man/man3/URI::Escape.3
/usr/lib/perl5/man/man3/LWP::UserAgent.3
/usr/lib/perl5/man/man3/URI::URL.3
/usr/lib/perl5/man/man3/LWP.3
/usr/lib/perl5/man/man3/HTTP::Status.3
/usr/lib/perl5/man/man3/LWP::Protocol.3
/usr/lib/perl5/man/man3/HTTP::Message.3
/usr/lib/perl5/man/man3/LWP::MediaTypes.3
/usr/lib/perl5/man/man3/HTTP::Headers::Util.3
/usr/lib/perl5/man/man3/HTTP::Request.3
/usr/lib/perl5/man/man3/Bundle::LWP.3
/usr/lib/perl5/man/man3/HTTP::Cookies.3
/usr/lib/perl5/man/man3/LWP::RobotUA.3
/usr/lib/perl5/man/man3/HTTP::Response.3
/usr/lib/perl5/man/man3/LWP::MemberMixin.3
/usr/lib/perl5/man/man3/lwpcook.3
/usr/lib/perl5/man/man3/HTTP::Daemon.3
/usr/lib/perl5/man/man3/WWW::RobotRules.3
/usr/lib/perl5/man/man3/LWP::Debug.3
/usr/lib/perl5/man/man3/File::Listing.3
/usr/lib/perl5/man/man3/HTTP::Headers.3
/usr/lib/perl5/man/man3/LWP::Simple.3
/usr/lib/perl5/man/man3/HTTP::Date.3
/usr/lib/perl5/man/man3/WWW::RobotRules::AnyDBM_File.3
/usr/bin/lwp-download
/usr/bin/lwp-request
/usr/bin/lwp-rget
/usr/bin/lwp-mirror
/usr/bin/GET
/usr/bin/HEAD
/usr/bin/POST
/usr/lib/perl5/site_perl/i386-linux/auto/libwww-perl/.packlist
