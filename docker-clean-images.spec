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
Requires:       findutils
Requires:       systemd
%systemd_requires
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides a systemd service to clean dangling docker
images.  It also provides a timer to call that service regularly.

%prep
%setup -q

%install
install -d -m 755 %{buildroot}%{_unitdir}
cp -p %{name}.service %{name}.timer %{buildroot}%{_unitdir}

%pre
%service_add_pre %{name}.timer

%post
%service_add_post %{name}.timer

%preun
%service_del_preun %{name}.timer

%postun
%service_del_postun %{name}.timer

%files
%defattr(-,root,root)
%doc README.rst
%license LICENSE
%{_unitdir}/*

%changelog
