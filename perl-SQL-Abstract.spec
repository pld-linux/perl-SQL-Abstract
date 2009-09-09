#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	SQL
%define		pnam	Abstract
Summary:	SQL::Abstract - generate SQL from Perl data structures
Summary(pl.UTF-8):	SQL::Abstract - generujący SQL z perlowych struktur danych
Name:		perl-SQL-Abstract
Version:	1.58
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4ab50f21c4795a7ec988efa7b21e6270
URL:		http://search.cpan.org/dist/SQL-Abstract/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Clone) >= 0.31
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Warn
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module was inspired by the excellent DBIx::Abstract. However, in
using the module I found that what I wanted to do was generate SQL,
but still retain complete control over my statement handles and use
the DBI interface. So, I set out to create an abstract SQL generation
module.

%description -l pl.UTF-8
Ten moduł był zainspirowany wspaniałym DBIx::Abstract. Jest to moduł
do abstrakcyjnego tworzenia SQL, pozwalający na pełną kontrolę nad
wyrażeniami i używanie interfejsu DBI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/SQL/Abstract

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL
%dir %{perl_vendorlib}/SQL/Abstract
%{perl_vendorlib}/SQL/*.pm
%{perl_vendorlib}/SQL/Abstract/Test.pm
%{_mandir}/man3/*
