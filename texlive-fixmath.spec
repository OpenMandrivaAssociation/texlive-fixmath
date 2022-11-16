Name:		texlive-fixmath
Version:	64648
Release:	1
Summary:	Make maths comply with ISO 31-0:1992 to ISO 31-13:1992
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fixmath
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixmath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixmath.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixmath.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX's default style of typesetting mathematics does not
comply with the International Standards ISO 31-0:1992 to ISO
31-13:1992 which require that uppercase Greek letters always be
typset upright, as opposed to italic (even though they usually
represent variables) and allow for typsetting of variables in a
boldface italic style (even though the required fonts are
available). This package ensures that uppercase Greek be
typeset in italic style, that upright $\Delta$ and $\Omega$
symbols are available through the commands \upDelta and
\upOmega; and provides a new math alphabet \mathbold for
boldface italic letters, including Greek. This package used to
be part of the was bundle, but has now become a package in its
own right.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/fixmath
%{_texmfdistdir}/tex/latex/fixmath
%doc %{_texmfdistdir}/doc/latex/fixmath

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
