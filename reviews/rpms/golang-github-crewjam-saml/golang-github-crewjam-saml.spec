# Generated by go2rpm 1
%bcond_without check

# https://github.com/crewjam/saml
%global goipath         github.com/crewjam/saml
Version:                0.4.0
%global tag             v0.4.0

%gometa

%global common_description %{expand:
SAML library for go.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        SAML library for go

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/beevik/etree)
BuildRequires:  golang(github.com/crewjam/httperr)
BuildRequires:  golang(github.com/dchest/uniuri)
BuildRequires:  golang(github.com/dgrijalva/jwt-go)
BuildRequires:  golang(github.com/kr/pretty)
BuildRequires:  golang(github.com/russellhaering/goxmldsig)
BuildRequires:  golang(github.com/russellhaering/goxmldsig/etreeutils)
BuildRequires:  golang(github.com/zenazn/goji)
BuildRequires:  golang(github.com/zenazn/goji/web)
BuildRequires:  golang(golang.org/x/crypto/bcrypt)
BuildRequires:  golang(golang.org/x/crypto/ripemd160)

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
* Tue Feb 18 11:19:56 CET 2020 Andreas Gerstmayr <agerstmayr@redhat.com> - 0.4.0-1
- Initial package

