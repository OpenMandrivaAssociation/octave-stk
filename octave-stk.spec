%define octpkg stk

# Exclude .oct files from provides
%define __provides_exclude_from ^%{octpkglibdir}/.*.oct$

Summary:	Octave Small Toolbox for Kriging
Name:		octave-%{octpkg}
Version:	2.4.0
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 3.2.4

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

This package is part of external Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
%doc %{octpkg}/NEWS
%doc %{octpkg}/COPYING

