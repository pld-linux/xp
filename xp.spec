Summary:	XP - an XML Parser in Java
Summary(pl):	XP - Parser XML napisany w Javie
Name:		xp
Version:	0.5
Release:	1
Vendor:		James Clark
License:	Free
Group:		Applications/Publishing/XML
Group(de):	Applikationen/Publizieren/XML
Group(pl):	Aplikacje/Publikowanie/XML
Source0:	ftp://ftp.jclark.com/pub/xml/%{name}.zip
Patch0:		%{name}-latin2.patch
URL:		http://www.jclark.com/xml/
BuildRequires:	unzip
#BuildRequires:	/usr/bin/jar
BuildRequires:	sax
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%define		_javaclassdir	%{_datadir}/java/classes
%define 	_jredir %{_libdir}/jre

%description
XP - an XML Parser in Java.

%description -l pl 
XP - Parser XML napisany w Javie.

%prep
%setup -q -c -T 
unzip -qa %{SOURCE0}
chmod -R a+rX *
%patch -p1

%build
rm -f %{name}.jar
export CLASSPATH=%{_jredir}/lib/rt.jar:%{_javaclassdir}/sax.jar:.
find com -name "*.java"  | xargs jikes -depend
find com -name "*.class" | xargs jar -c0f %{name}.jar

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javaclassdir}
install %{name}.jar $RPM_BUILD_ROOT%{_javaclassdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs
%{_javaclassdir}/*
