Name:           docker-clean-images
Version:        @VERSION@
Release:        1
Summary:        systemd servive to clean dangling docker images
License:        MIT
Group:          System/Local
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Requires:       docker
Requires:       systemd
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides a systemd service to clean dangling docker
images.  It also provides a timer to call that service regularly.

%prep
%setup -q

%install
install -d -m 755 %{buildroot}%{_unitdir}
cp -p %{name}.service %{name}.timer %{buildroot}%{_unitdir}

%post
systemctl enable %{name}.timer

%preun
systemctl stop %{name}.timer
systemctl disable %{name}.timer

%files
%defattr(-,root,root)
%{_unitdir}/*

%changelog
