Name: fonts-ttf-noto-emoji
Version: 2.042
Release: 1
Source0: https://github.com/googlefonts/noto-emoji/archive/refs/tags/v%{version}.tar.gz
# Based on comments on https://github.com/googlefonts/noto-emoji/issues/36
Source1: noto-emoji.conf
# FIXME This isn't being built anymore -- is it still worth shipping?
# Probably there is some stuff hardcoding NotoEmoji without "Color"...
# For now, let's be on the safe side
Source2: https://github.com/googlefonts/noto-emoji/raw/v2.034/fonts/NotoEmoji-Regular.ttf
Summary: Color and Black-and-White Noto emoji fonts
URL: https://github.com/googlefonts/noto-emoji
License: Apache-2.0
Group: Fonts
BuildRequires: fonttools
BuildRequires: python%{py_ver}dist(fonttools) >= 4.7.0
BuildRequires: python%{py_ver}dist(notofonttools) >= 0.2.16
BuildRequires: pkgconfig(cairo)
BuildRequires: zopfli
BuildRequires: cmake(Zopfli)
BuildRequires: pngquant
BuildRequires: imagemagick
Obsoletes: noto-emoji-fonts <= 20171024-4
Provides: noto-emoji-fonts = 20171024-4
Obsoletes: noto-coloremoji-fonts <= 20171024-4
Provides: noto-coloremoji-fonts = 20171024-4
BuildArch: noarch

%description
Color and Black-and-White Noto emoji fonts

%prep
%autosetup -p1 -n noto-emoji-%{version}

%build
# Official build instructions would have us set up venv and
# install deps in there with pip -- but our packaged versions
# are better, so let's just pretend we're virtualized
# (The Makefile only checks "ifdef VIRTUAL_ENV")
%make_build VIRTUAL_ENV=fake

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF
install -c -m 644 NotoColorEmoji.ttf %{buildroot}%{_datadir}/fonts/TTF/

install -c -m 644 %{S:2} %{buildroot}%{_datadir}/fonts/TTF/

mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
install -c -m 644 %{S:1} %{buildroot}%{_sysconfdir}/fonts/conf.d/90-noto-emoji.conf

%files
%{_sysconfdir}/fonts/conf.d/*
%{_datadir}/fonts/TTF/*
