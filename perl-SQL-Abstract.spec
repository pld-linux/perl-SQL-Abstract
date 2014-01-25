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
Version:	1.77
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4e7af7304a5e6c89e1e23582c7d6b657
URL:		http://search.cpan.org/dist/SQL-Abstract/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Clone) >= 0.31
BuildRequires:	perl-Class-Accessor-Grouped >= 0.10002
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-Getopt-Long-Descriptive >= 0.091
BuildRequires:	perl-Hash-Merge >= 0.12
BuildRequires:	perl-Storable
BuildRequires:	perl-Test-Deep >= 0.106
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
%doc Changes
%attr(755,root,root) %{_bindir}/format-sql
#{perl_vendorlib}/DBIx/Class/Storage/Debug/PrettyPrint.pm
%dir %{perl_vendorlib}/SQL/Abstract
%{perl_vendorlib}/SQL/*.pm
%{perl_vendorlib}/SQL/Abstract/Tree.pm
%{perl_vendorlib}/SQL/Abstract/Test.pm
%{_mandir}/man3/*
