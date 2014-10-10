# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       systemsettings

# >> macros
# << macros

Summary:    KDE System Settings application
Version:    5.1.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  systemsettings.yaml
Source101:  systemsettings-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  kitemviews-devel
BuildRequires:  kcmutils-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  kservice-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kconfig-devel
BuildRequires:  khtml-devel
BuildRequires:  kdelibs4support-devel

%description
KDE System Settings application


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%package doc
Summary:    Documentation and user manuals for %{name}
Group:      Documentation
Requires:   %{name} = %{version}-%{release}

%description doc
Documentation and user manuals for %{name}


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%doc COPYING COPYING.DOC
%{_kf5_bindir}/systemsettings5
%{_kf5_libdir}/libsystemsettingsview.so.*
%{_kf5_plugindir}/*
%{_kf5_sharedir}/systemsettings
%{_kf5_servicesdir}/*
%{_kf5_servicetypesdir}/*
%{_kf5_sharedir}/applications/*.desktop
%{_kf5_sharedir}/kxmlgui5/*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_includedir}/systemsettingsview
%{_kf5_libdir}/libsystemsettingsview.so
# >> files devel
# << files devel

%files doc
%defattr(-,root,root,-)
%{_kf5_htmldir}/en/systemsettings
# >> files doc
# << files doc