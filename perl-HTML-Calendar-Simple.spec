#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Calendar-Simple
Summary:	HTML::Calendar::Simple - a simple HTML calendar
Summary(pl):	HTML::Calendar::Simple - prosty kalendarz w HTML
Name:		perl-HTML-Calendar-Simple
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4524a1c386f63e7fe6e9815ef37a13c5
%if %{with tests}
BuildRequires:	perl-CGI >= 2.752
BuildRequires:	perl-Date-Simple >= 1.03
BuildRequires:	perl-Test-Simple >= 0.40
%endif
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple module which will make an HTML representation of a
given month. You can add links to individual days, or in fact, any
sort of information you want.

Yes, the inspiration for this came out of me looking at
HTML::CalendarMonthSimple, and thinking 'Hmmm. A bit too complicated
for what I want. I know, I will write a simplified version.' So it was
done.

%description -l pl
Ten prosty modu� tworzy reprezentacj� podanego miesi�ca w HTML. Mo�na
dodawa� odno�niki do poszczeg�lnych dni, lub, w praktyce, dowolny
rodzaj informacji.

Inspiracja wzi�a si� z patrzenia na HTML::CalendarMonthSimple i
my�lenia "Hmmm. Troch� zbyt skomplikowane do tego, co chc�. Wiem,
napisz� uproszczon� wersj�.". No i zosta�a napisana.

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
%doc Changes README
%dir %{perl_vendorlib}/HTML/Calendar
%{perl_vendorlib}/HTML/Calendar/Simple.pm
%{_mandir}/man3/*
