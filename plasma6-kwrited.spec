%define major %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20231103

Summary:	Application for monitoring messages sent with write or wall
Name:		plasma6-kwrited
Version:	5.27.80
Release:	%{?git:0.%{git}.}2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://kde.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/kwrited/-/archive/master/kwrited-master.tar.bz2#/kwrited-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%{major}/kwrited-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Pty)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)

%description
Application for monitoring messages sent with write or wall.

%files
%{_bindir}/kwrited
%{_sysconfdir}/xdg/autostart/kwrited-autostart.desktop
%{_datadir}/knotifications6/kwrited.notifyrc

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n kwrited-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
