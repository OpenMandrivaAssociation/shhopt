%define	major 1
%define libname	%mklibname shhopt %{major}

Summary:	Library for parsing command line options
Name:		shhopt
Version:	1.1.7
Release:	%mkrel 6
License:	Artistic
Group:		System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://shh.thathost.com/pub-unix/
Source0:	http://shh.thathost.com/pub-unix/files/%{name}-%{version}.tar.bz2

%description
C-functions for parsing command line options, both traditional
one-character options, and GNU'ish --long-options.

%package -n	%{libname}
Summary:	Library for parsing command line options
Group:          System/Libraries

%description -n	%{libname}
C-functions for parsing command line options, both traditional
one-character options, and GNU'ish --long-options.

%package -n	%{libname}-devel
Summary:	Library and header files for the %{name} library
Group:		Development/C
Provides:	lib%{name}-devel = %{version}
Provides:	%{name}-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
C-functions for parsing command line options, both traditional
one-character options, and GNU'ish --long-options.

%prep

%setup -q -n %{name}-%{version}

%build

# make the shared library
make SHARED="1" OPTIM="%{optflags} -D_REENTRANT -fPIC"

# make the static library
make OPTIM="%{optflags} -D_REENTRANT -fPIC"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

# install the shared library
make \
    SHARED="1" \
    INSTBASEDIR="%{buildroot}%{_prefix}" \
    INSTLIBDIR="%{buildroot}%{_libdir}" \
    install

# install the static library
make \
    INSTBASEDIR="%{buildroot}%{_prefix}" \
    INSTLIBDIR="%{buildroot}%{_libdir}" \
    install

# fix a file conflict with netpbm-devel
install -d %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_includedir}/*.h %{buildroot}%{_includedir}/%{name}/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%doc CREDITS ChangeLog INSTALL README TODO
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so
%{_libdir}/*.a


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.1.7-6mdv2010.0
+ Revision: 433781
- rebuild

* Mon Jun 09 2008 Pixel <pixel@mandriva.com> 1.1.7-5mdv2009.0
+ Revision: 217195
- do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Feb 14 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.1.7-5mdv2008.1
+ Revision: 168224
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.7-5mdv2008.0
+ Revision: 25475
- Import shhopt



* Fri Apr 28 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.7-5mdk
- fix spec file mistake

* Fri Apr 28 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.7-4mdk
- fix a file conflict with netpbm-devel

* Thu May 12 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.7-3mdk
- rpmlint fixes
- lib64 fixes

* Sat Nov 13 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.1.7-2mdk
- rpmbuildupdated

* Sun Oct 05 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.1.7-1mdk
- initial cooker contrib
