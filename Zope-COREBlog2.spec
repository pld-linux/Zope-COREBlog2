%define		zope_subname	COREBlog2
%define		sub_ver b
%define		header_load _08b
Summary:	Blog / Weblog / Web Nikki system on Zope and Plone
Summary(pl):	System bloga/webloga oparty na Zope i Plone
Name:		Zope-%{zope_subname}
Version:	0.8
Release:	0.%{sub_ver}.1
License:	GPL
Group:		Development/Tools
Source0:	http://coreblog.org/junk/%{zope_subname}%{header_load}.tgz
# Source0-md5:	6a75d95b2068266b5dd59e1781eff54a
URL:		http://coreblog.org/
BuildRequires:	python
%pyrequires_eq	python-modules
Requires:	Zope >= 2.7.7
Requires:	Zope-CMFPlone >= 2.1.1
Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Blog / Weblog / Web Nikki system on Zope and Plone.

%description -l pl
System bloga/webloga oparty na Zope i Plone.

%prep
%setup -q -n %{zope_subname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af * $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/{README.txt,changelog.txt,LICENSE.*}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc README.txt changelog.txt
%{_datadir}/%{name}
