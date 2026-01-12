%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg kxmleditor
%define tde_prefix /opt/trinity


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


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/development/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DDATA_INSTALL_DIR=%{tde_prefix}/share/apps
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

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
%{tde_prefix}/bin/kxmleditor
%{tde_prefix}/%{_lib}/libkxmleditorpart.la
%{tde_prefix}/%{_lib}/libkxmleditorpart.so
%{tde_prefix}/%{_lib}/libkxmleditorpart.so.1
%{tde_prefix}/%{_lib}/libkxmleditorpart.so.1.0.0
%{tde_prefix}/share/applications/tde/kxmleditor.desktop
%{tde_prefix}/share/apps/kxmleditor/
%{tde_prefix}/share/doc/tde/HTML/en/kxmleditor/
%{tde_prefix}/share/icons/hicolor/*/apps/kxmleditor.png
%{tde_prefix}/share/icons/locolor/*/apps/kxmleditor.png
%{tde_prefix}/share/services/kxmleditorpart.desktop
%{tde_prefix}/share/man/man1/kxmleditor.1*

