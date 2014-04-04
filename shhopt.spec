%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Library for parsing command line options
Name:		shhopt
Version:	1.1.7
Release:	8
License:	Artistic
Group:		System/Libraries
Url:		http://shh.thathost.com/pub-unix/
Source0:	http://shh.thathost.com/pub-unix/files/%{name}-%{version}.tar.bz2

%description
C-functions for parsing command line options, both traditional
one-character options, and GNU'ish --long-options.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library for parsing command line options
Group:		System/Libraries

%description -n %{libname}
C-functions for parsing command line options, both traditional
one-character options, and GNU'ish --long-options.

%files -n %{libname}
%doc CREDITS ChangeLog README TODO
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Library and header files for the %{name} library
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}
Obsoletes:	%{_lib}shhopt1-devel < 1.1.7-8
Conflicts:	%{_lib}shhopt1-devel < 1.1.7-8

%description -n %{devname}
C-functions for parsing command line options, both traditional
one-character options, and GNU'ish --long-options.

%files -n %{devname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so
%{_libdir}/*.a

#----------------------------------------------------------------------------

%prep
%setup -q

%build
# make the shared library
make SHARED="1" OPTIM="%{optflags} -D_REENTRANT -fPIC"

# make the static library
make OPTIM="%{optflags} -D_REENTRANT -fPIC"

%install
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

