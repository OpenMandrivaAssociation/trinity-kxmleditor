%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg kxmleditor
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_confdir %{_sysconfdir}/trinity
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity

Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.1.4
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	XML Editor for TDE
Group:		Applications/Multimedia
URL:		http://www.trinitydesktop.org/

License:	GPLv2+

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/development/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake
BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_SKIP_RPATH=OFF
BuildOption:    -DCMAKE_SKIP_INSTALL_RPATH=OFF
BuildOption:    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON
BuildOption:    -DCMAKE_INSTALL_RPATH="%{tde_libdir}"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_datadir}
BuildOption:    -DDATA_INSTALL_DIR=%{tde_datadir}/apps
BuildOption:    -DLIB_INSTALL_DIR=%{tde_libdir}
BuildOption:    -DBUILD_ALL=ON

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	libtool

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

Obsoletes:      %name-devel < %{EVRD}


%description
KXML Editor is a simple program, that displays and edits the contents of an
XML file. It can be embedded in Quanta, and used with DCOP.

The left side contains a tree representing the XML document structure. The
right side contains a list of attributes for the selected XML element and its
contents.


%install -a
%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_bindir}/kxmleditor
%{tde_libdir}/libkxmleditorpart.la
%{tde_libdir}/libkxmleditorpart.so
%{tde_libdir}/libkxmleditorpart.so.1
%{tde_libdir}/libkxmleditorpart.so.1.0.0
%{tde_tdeappdir}/kxmleditor.desktop
%{tde_datadir}/apps/kxmleditor/
%{tde_tdedocdir}/HTML/en/kxmleditor/
%{tde_datadir}/icons/hicolor/*/apps/kxmleditor.png
%{tde_datadir}/icons/locolor/*/apps/kxmleditor.png
%{tde_datadir}/services/kxmleditorpart.desktop
%{tde_mandir}/man1/kxmleditor.1*

