Summary:	XP - an XML Parser in Java
Summary(pl):	XP - Parser XML napisany w Javie
Name:		xp
Version:	19991105
Release:	1
Vendor:		James Clark
License:	Free
Group:		Applications/Publishing/XML
Group(de):	Applikationen/Publizieren/XML
Group(pl):	Aplikacje/Publikowanie/XML
Source0:	ftp://ftp.jclark.com/pub/xml/%{name}.zip
URL:		http://www.jclark.com/xml/
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%define		_javaclassdir	%{_datadir}/java/classes

%description
XP - an XML Parser in Java.

%description -l pl 
XP - Parser XML napisany w Javie.

%prep
%setup -q -c -T 
unzip -qa %{SOURCE0}
chmod -R a+rX *

%install
rm -rf $RPM_BUILD_ROOT
install -d 	$RPM_BUILD_ROOT%{_javaclassdir}
install *.jar 	$RPM_BUILD_ROOT%{_javaclassdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs
%{_javaclassdir}/*
