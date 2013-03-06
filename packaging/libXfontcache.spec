Name:           libXfontcache
Version:        1.0.5
Release:        0
Summary:        X TrueType font cache extension client library
License:        MIT
Group:          Development/Libraries
Url:            http://xorg.freedesktop.org/

Source:         %name-%version.tar.bz2
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontcacheproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.3

%description
FontCache is an extension that is used by X TrueType to cache
information about fonts.

%package devel
Summary:        Development files for the X TrueType font cache library
Group:          Development/Libraries
Requires:       %name = %version

%description devel
FontCache is an extension that is used by X TrueType to cache
information about fonts.

This package contains the development headers for the library found
in %name.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
%fdupes %buildroot

%post  -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%defattr(-,root,root)
%license COPYING
%_libdir/libXfontcache.so.1*

%files devel
%defattr(-,root,root)
%_libdir/libXfontcache.so
%_libdir/pkgconfig/xfontcache.pc
%_mandir/man3/*

%changelog
