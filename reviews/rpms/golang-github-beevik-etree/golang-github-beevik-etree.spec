# Generated by go2rpm 1
%bcond_without check

# https://github.com/beevik/etree
%global goipath         github.com/beevik/etree
Version:                1.1.0
%global tag             v1.1.0

%gometa

%global common_description %{expand:
Parse and generate XML easily in go.}

%global golicenses      LICENSE
%global godocs          README.md RELEASE_NOTES.md CONTRIBUTORS

Name:           %{goname}
Release:        1%{?dist}
Summary:        Parse and generate XML easily in go

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Fri Feb 07 16:34:05 CET 2020 Andreas Gerstmayr <agerstmayr@redhat.com> - 1.1.0-1
- Initial package

