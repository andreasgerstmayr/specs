# Generated by go2rpm 1
%bcond_without check

# https://github.com/cpuguy83/go-md2man
%global goipath         github.com/cpuguy83/go-md2man/v2
Version:                2.0.0

%gometa

%global common_description %{expand:
Converts markdown into roff (man pages).}

%global golicenses      LICENSE.md
%global godocs          README.md go-md2man.1.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Converts markdown into roff (man pages)

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/russross/blackfriday/v2)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/go-md2man %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE.md
%doc README.md go-md2man.1.md
%{_bindir}/*

%gopkgfiles

%changelog
* Thu Apr 23 19:59:02 CEST 2020 Andreas Gerstmayr <agerstmayr@redhat.com> - 2.0.0-1
- Initial package for github.com/cpuguy83/go-md2man/v2
