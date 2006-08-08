Summary:	XP - an XML Parser in Java
Summary(pl):	XP - analizator sk³adniowy XML-a napisany w Javie
Name:		xp
Version:	0.5
Release:	3
Epoch:		1
Vendor:		James Clark
License:	Free
Group:		Applications/Publishing/XML/Java
Source0:	ftp://ftp.jclark.com/pub/xml/%{name}.zip
# Source0-md5:	e4a2371d5bad54eefa7287ebc62e2f1a
Patch0:		%{name}-latin2.patch
URL:		http://www.jclark.com/xml/
BuildRequires:	jar
BuildRequires:	jikes
BuildRequires:	sax
BuildRequires:	unzip
Requires:	jre
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%define		_javaclassdir	%{_datadir}/java/classes
%define 	_jredir %{_libdir}/jre
# _javaclasspath exported in build as $CLASSPATH by rpm
%define		_javaclasspath %{_jredir}/lib/rt.jar:%{_javaclassdir}/sax.jar:.

%description
XP - an XML Parser in Java.

%description -l pl
XP - analizator sk³adniowy XML-a napisany w Javie.

%prep
%setup -q -c -T
unzip -qa %{SOURCE0}
chmod -R a+rX *
%patch0 -p1

%build
rm -f %{name}.jar
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
