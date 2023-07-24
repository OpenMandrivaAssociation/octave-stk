%global octpkg stk

Summary:	The STK is a (not so) Small Toolbox for Kriging for Octave
Name:		octave-stk
Version:	2.8.1
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/stk/
Url:		https://github.com/stk-kriging/stk
Source0:	https://github.com/stk-kriging/stk/releases/download/%{version}/stk-%{version}-octpkg.tar.gz

BuildRequires:  octave-devel >= 4.0.1

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
The STK is a (not so) Small Toolbox for Kriging. Its primary focus is on the
interpolation/regression technique known as kriging, which is very closely
related to Splines and Radial Basis Functions, and can be interpreted as a
non-parametric Bayesian method using a Gaussian Process (GP) prior. The STK
also provides tools for the sequential and non-sequential design of
experiments. Even though it is, currently, mostly geared towards the Design
and Analysis of Computer Experiments (DACE), the STK can be useful for other
applications areas (such as Geostatistics, Machine Learning, Non-parametric
Regression, etc.).

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

