# Generated by go2rpm 1
%bcond_without check

# https://github.com/urfave/cli
%global goipath         gopkg.in/urfave/cli.v2
%global forgeurl        https://github.com/urfave/cli
Version:                2.2.0

%gometa

%global goaltipaths     github.com/urfave/cli/v2

%global common_description %{expand:
A simple, fast, and fun package for building command line apps in Go.}

%global golicenses      LICENSE
%global godocs          docs CODE_OF_CONDUCT.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        A simple, fast, and fun package for building command line apps in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/cpuguy83/go-md2man/v2/md2man)
BuildRequires:  golang(gopkg.in/yaml.v2)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
mkdir -p _build/src/github.com/urfave/cli
cp -P _build/src/gopkg.in/urfave/cli.v2 _build/src/github.com/urfave/cli/v2
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Apr 21 19:24:12 CEST 2020 Andreas Gerstmayr <agerstmayr@redhat.com> - 2.2.0-1
- Initial package
