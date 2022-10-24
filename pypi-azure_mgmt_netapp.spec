#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-azure_mgmt_netapp
Version  : 9.0.0
Release  : 15
URL      : https://files.pythonhosted.org/packages/10/1f/618a152b3875f0530eecf60cf47e5f8ebbb3659c7f6e9a8c209c585daf7f/azure-mgmt-netapp-9.0.0.zip
Source0  : https://files.pythonhosted.org/packages/10/1f/618a152b3875f0530eecf60cf47e5f8ebbb3659c7f6e9a8c209c585daf7f/azure-mgmt-netapp-9.0.0.zip
Summary  : Microsoft Azure NetApp Files Management Client Library for Python
Group    : Development/Tools
License  : MIT
Requires: pypi-azure_mgmt_netapp-license = %{version}-%{release}
Requires: pypi-azure_mgmt_netapp-python = %{version}-%{release}
Requires: pypi-azure_mgmt_netapp-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(azure_common)
BuildRequires : pypi(azure_mgmt_core)
BuildRequires : pypi(msrest)

%description
# Microsoft Azure SDK for Python
This is the Microsoft Azure NetApp Files Management Client Library.
This package has been tested with Python 3.7+.
For a more complete view of Azure libraries, see the [azure sdk python release](https://aka.ms/azsdk/python/all).

%package license
Summary: license components for the pypi-azure_mgmt_netapp package.
Group: Default

%description license
license components for the pypi-azure_mgmt_netapp package.


%package python
Summary: python components for the pypi-azure_mgmt_netapp package.
Group: Default
Requires: pypi-azure_mgmt_netapp-python3 = %{version}-%{release}

%description python
python components for the pypi-azure_mgmt_netapp package.


%package python3
Summary: python3 components for the pypi-azure_mgmt_netapp package.
Group: Default
Requires: python3-core
Provides: pypi(azure_mgmt_netapp)
Requires: pypi(azure_common)
Requires: pypi(azure_mgmt_core)
Requires: pypi(msrest)

%description python3
python3 components for the pypi-azure_mgmt_netapp package.


%prep
%setup -q -n azure-mgmt-netapp-9.0.0
cd %{_builddir}/azure-mgmt-netapp-9.0.0
pushd ..
cp -a azure-mgmt-netapp-9.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664288251
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-azure_mgmt_netapp
cp %{_builddir}/azure-mgmt-netapp-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-azure_mgmt_netapp/7aea571d641549de89730da8e7ff5a6940c5526b || :
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
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-azure_mgmt_netapp/7aea571d641549de89730da8e7ff5a6940c5526b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
