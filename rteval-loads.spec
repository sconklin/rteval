Name:		rteval-loads
Version:	1.2
Release:	2%{?dist}
Summary:	Source files for rteval loads
Group:		Development/Tools
License:	GPLv2
URL:		http://git.kernel.org/?p=linux/kernel/git/clrkwllms/rteval.git
Source0:	http://www.kernel.org/pub/linux/kernel/v2.6/linux-2.6.26.1.tar.bz2
Source1:	dbench-4.0.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	gcc binutils make
Obsoletes:	rteval-kcompile >= 1.0
Obsoletes:	rteval-hackbench >= 1.0
BuildArch:	noarch

%description
This package provides source code for system loads used by the rteval package

%prep

%build

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/usr/share/rteval/loadsource
install -m 644 %{SOURCE0} ${RPM_BUILD_ROOT}/usr/share/rteval/loadsource
install -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}/usr/share/rteval/loadsource

%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-,root,root,-)
%dir %{_datadir}/rteval/loadsource
%{_datadir}/rteval/loadsource/*
%doc

%changelog
* Thu Jul 15 2010 Clark Williams <williams@redhat.com> - 1.2-2
- removed rteval require from specfile (caused circular dependency)

* Thu Jul  8 2010 Clark Williams <williams@redhat.com> - 1.2-1
- removed hackbench tarball (now using rt-tests hackbench)

* Fri Feb 19 2010 Clark Williams <williams@redhat.com> - 1.1-1
- updated hackbench source with fixes from David Sommerseth 
  <davids@redhat.com> to cleanup child processes

* Thu Nov  5 2009 Clark Williams <williams@redhat.com> - 1.0-1
- initial packaging effort
