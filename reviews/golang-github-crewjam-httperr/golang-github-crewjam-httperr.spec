# Generated by go2rpm 1
%bcond_without check

# https://github.com/crewjam/httperr
%global goipath         github.com/crewjam/httperr
Version:                0.2.0
%global tag             v0.2.0

%gometa

%global common_description %{expand:
A golang error object that speaks HTTP.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        A golang error object that speaks HTTP

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/pkg/errors)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

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
* Tue Feb 18 23:00:42 CET 2020 Andreas Gerstmayr <agerstmayr@redhat.com> - 0.2.0-1
- Initial package
