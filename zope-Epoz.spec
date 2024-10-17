%define Product Epoz
%define product epoz
%define name    zope-%{Product}
%define version 2.0.2
%define release %mkrel 8

%define zope_minver     2.7
%define zope_home       %{_prefix}/lib/zope
%define software_home   %{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Epoz allows you to edit Zope-objects with a wysiwyg-editor
License:    GPL
Group:      System/Servers
URL:        https://mjablonski.zope.de/Epoz
Source:     http://mjablonski.zope.de/Epoz/releases/Epoz-%{version}.tar.bz2
Requires:   zope >= %{zope_minver}
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
No plugins are required. You only have to use a recent browser (IE >= 5.5, 
Mozilla >= 1.3.1, Netscape >= 7.1, Firebird >= 0.7) that supports 
Rich-Text-controls (called Midas for Mozilla).

%prep
%setup -c -q

%build
find -name '*.tar.gz' -exec rm -f {} \;
rm -f Epoz/.project

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
