%global tl_name fixmath
%global tl_revision 78348

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9.1
Release:	%{tl_revision}.1
Summary:	Make maths comply with ISO 31-0:1992 to ISO 31-13:1992
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fixmath
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fixmath.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fixmath.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fixmath.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LaTeX's default style of typesetting mathematics does not comply with
the International Standards ISO 31-0:1992 to ISO 31-13:1992 which
require that uppercase Greek letters always be typeset upright, as
opposed to italic (even though they usually represent variables) and
allow for typesetting of variables in a boldface italic style (even
though the required fonts are available). This package ensures that
uppercase Greek be typeset in italic style, that upright $\Delta$ and
$\Omega$ symbols are available through the commands \upDelta and
\upOmega; and provides a new math alphabet \mathbold for boldface italic
letters, including Greek. This package used to be part of the was
bundle, but has now become a package in its own right.

