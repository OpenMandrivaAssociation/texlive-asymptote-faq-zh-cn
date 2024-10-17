Name:		texlive-asymptote-faq-zh-cn
Version:	15878
Release:	2
Summary:	Asymptote FAQ (Chinese translation)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/asymptote-faq-zh-cn
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asymptote-faq-zh-cn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asymptote-faq-zh-cn.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a Chinese translation of the Asymptote FAQ

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/support/asymptote-faq-zh-cn

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
