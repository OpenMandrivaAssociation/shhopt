%define	major 1
%define libname	%mklibname shhopt %{major}

Summary:	Library for parsing command line options
Name:		shhopt
Version:	1.1.7
Release:	%mkrel 5
License:	Artistic
Group:		System/Libraries
URL:		http://shh.thathost.com/pub-unix/
Source0:	http://shh.thathost.com/pub-unix/files/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

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
