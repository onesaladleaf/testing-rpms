%global commit 0a43c8be564feae0493b6e24b2e3e98459a4f9b6

Name:           pd-mapper
Version:        1.0
Release:        7
Summary:        Service listing daemon for Qualcomm IPC Router

License:        BSD-3-Clause
URL:            https://github.com/andersson/pd-mapper
Source:         %{url}/archive/%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd-rpm-macros

BuildRequires:  qrtr-devel
BuildRequires:  xz-devel
Requires:       qrtr

%description
This package provides the userspace component for the Qualcomm IPC Router
protocol, which maintains a service listing and allows peforming lookups.

%prep
%autosetup -n pd-mapper-%{commit}

%build
%make_build prefix="%{_prefix}"

%install
%make_install prefix="%{_prefix}"

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service

%changelog
%autochangelog
