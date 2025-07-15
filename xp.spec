Summary:	XP - an XML Parser in Java
Summary(pl.UTF-8):	XP - analizator składniowy XML-a napisany w Javie
Name:		xp
Version:	0.5
Release:	4
Epoch:		1
License:	Free
Group:		Applications/Publishing/XML/Java
Source0:	ftp://ftp.jclark.com/pub/xml/%{name}.zip
# Source0-md5:	e4a2371d5bad54eefa7287ebc62e2f1a
Patch0:		%{name}-latin2.patch
URL:		http://www.jclark.com/xml/
BuildRequires:	jar
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	sax
BuildRequires:	unzip
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XP - an XML Parser in Java.

%description -l pl.UTF-8
XP - analizator składniowy XML-a napisany w Javie.

%package javadoc
Summary:	Online manual for %{name}
Summary(pl.UTF-8):	Dokumentacja online do %{name}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for %{name}.

%description javadoc -l pl.UTF-8
Dokumentacja do %{name}.

%description javadoc -l fr.UTF-8
Javadoc pour %{name}.

%prep
%define	__unzip	/usr/bin/unzip -a
%setup -qc
%patch -P0 -p1
rm -f %{name}.jar

%build
required_jars="sax"
CLASSPATH=$(build-classpath $required_jars)
export CLASSPATH

%javac -source 1.4 $(find com -name '*.java')
%jar -c0f %{name}.jar $(find com -name '*.class')

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
# jars
cp -a %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc docs/index.html
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
