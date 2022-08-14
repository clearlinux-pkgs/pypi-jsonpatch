#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jsonpatch
Version  : 1.32
Release  : 70
URL      : https://files.pythonhosted.org/packages/21/67/83452af2a6db7c4596d1e2ecaa841b9a900980103013b867f2865e5e1cf0/jsonpatch-1.32.tar.gz
Source0  : https://files.pythonhosted.org/packages/21/67/83452af2a6db7c4596d1e2ecaa841b9a900980103013b867f2865e5e1cf0/jsonpatch-1.32.tar.gz
Summary  : Apply JSON-Patches (RFC 6902)
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-jsonpatch-bin = %{version}-%{release}
Requires: pypi-jsonpatch-license = %{version}-%{release}
Requires: pypi-jsonpatch-python = %{version}-%{release}
Requires: pypi-jsonpatch-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(jsonpointer)
BuildRequires : pypi-jsonpointer

%description
=================
        
        |PyPI version| |Supported Python versions| |Build Status| |Coverage
        Status|
        
        Applying JSON Patches in Python
        -------------------------------
        
        Library to apply JSON Patches according to `RFC

%package bin
Summary: bin components for the pypi-jsonpatch package.
Group: Binaries
Requires: pypi-jsonpatch-license = %{version}-%{release}

%description bin
bin components for the pypi-jsonpatch package.


%package license
Summary: license components for the pypi-jsonpatch package.
Group: Default

%description license
license components for the pypi-jsonpatch package.


%package python
Summary: python components for the pypi-jsonpatch package.
Group: Default
Requires: pypi-jsonpatch-python3 = %{version}-%{release}

%description python
python components for the pypi-jsonpatch package.


%package python3
Summary: python3 components for the pypi-jsonpatch package.
Group: Default
Requires: python3-core
Provides: pypi(jsonpatch)
Requires: pypi(jsonpointer)

%description python3
python3 components for the pypi-jsonpatch package.


%prep
%setup -q -n jsonpatch-1.32
cd %{_builddir}/jsonpatch-1.32
pushd ..
cp -a jsonpatch-1.32 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656397356
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python tests.py
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jsonpatch
cp %{_builddir}/jsonpatch-1.32/COPYING %{buildroot}/usr/share/package-licenses/pypi-jsonpatch/0305317c0f694ba11e8f059938fd0c880356e7bc
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
## Remove excluded files
rm -f %{buildroot}*/usr/bin/jsondiff
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jsonpatch

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jsonpatch/0305317c0f694ba11e8f059938fd0c880356e7bc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
