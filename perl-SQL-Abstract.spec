#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	SQL
%define	pnam	Abstract
Summary:	SQL::Abstract - generate SQL from Perl data structures
Summary(pl):	SQL::Abstract - generuj±cy SQL z perlowych struktur danych
Name:		perl-SQL-Abstract
Version:	1.15
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d8bd12b0b9caef4e8849908bb04641e7
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module was inspired by the excellent DBIx::Abstract.  However,
in using the module I found that what I wanted to do was generate SQL,
but still retain complete control over my statement handles and use
the DBI interface. So, I set out to create an abstract SQL generation
module.

%description -l pl
Ten modu³ by³ zainspirowany wspania³ym DBIx::Abstract. Jest to modu³
do abstrakcyjnego tworzenia SQL, pozwalaj±cy na pe³n± kontrolê nad
wyra¿eniami i u¿ywanie interfejsu DBI.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
