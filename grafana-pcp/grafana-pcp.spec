Name:           grafana-pcp
Version:        0.0.7
Release:        1%{?dist}
Summary:        Grafana PCP Plugin

%global         github https://github.com/performancecopilot/grafana-pcp
%global         install_dir %{_sharedstatedir}/grafana/plugins/grafana-pcp
%global         _debugsource_template %{nil} # avoid empty debugsourcefiles.list

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches}

License:        ASL 2.0
URL:            %{github}

Source0:        %{github}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        node_modules-%{version}.tar.xz

Requires:       pcp >= 4.3.4
Requires:       grafana >= 6.2.2
Suggests:       redis >= 5.0.4

Obsoletes:      grafana-pcp-datasource
Obsoletes:      grafana-pcp-redis

%description
This Grafana plugin for Performance Co-Pilot includes datasources for
pmseries, live metrics and the bpftrace PMDA, and several example dashboards.

%prep
%setup -q
%setup -q -a 1


%build
echo 'Grafana plugins are always pre-built in the "dist" directory'
[ -f dist/module.js.map ] || exit 1 # fail

%check
./node_modules/jest-cli/bin/jest.js --silent

%install
install -d -m 755 %{buildroot}/%{install_dir}
cp -a dist/* %{buildroot}/%{install_dir}

%files
%{install_dir}

%license LICENSE NOTICE
%doc README.md

%changelog
* Fri Aug 16 2019 Andreas Gerstmayr <agerstmayr@redhat.com> 0.0.7-1
- converted into a Grafana app plugin, renamed to grafana-pcp
- redis: support for instance domains, labels, autocompletion, automatic rate conversation
- live and bpftrace: initial commit of datasources

* Tue Jun 11 2019 Mark Goodwin <mgoodwin@redhat.com> 0.0.6-1
- renamed package to grafana-pcp-redis, updated README, etc

* Wed Jun 05 2019 Mark Goodwin <mgoodwin@redhat.com> 0.0.5-1
- renamed package to grafana-pcp-datasource, README, etc

* Fri May 17 2019 Mark Goodwin <mgoodwin@redhat.com> 0.0.4-1
- add suggested pmproxy URL in config html
- updated instructions and README.md now that grafana is in Fedora

* Fri Apr 12 2019 Mark Goodwin <mgoodwin@redhat.com> 0.0.3-1
- require grafana v6.1.3 or later
- install directory is now below /var/lib/grafana/plugins

* Wed Mar 20 2019 Mark Goodwin <mgoodwin@redhat.com> 0.0.2-1
- initial version
