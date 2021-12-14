#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-azure_mgmt_netapp
Version  : 5.1.0
Release  : 2
URL      : https://files.pythonhosted.org/packages/aa/01/566bdba5bd0f7eef7ff4e4a14de6a0096dd114e4df4bea6cbd4d3ccf568d/azure-mgmt-netapp-5.1.0.zip
Source0  : https://files.pythonhosted.org/packages/aa/01/566bdba5bd0f7eef7ff4e4a14de6a0096dd114e4df4bea6cbd4d3ccf568d/azure-mgmt-netapp-5.1.0.zip
Summary  : Microsoft Azure NetApp Files Management Client Library for Python
Group    : Development/Tools
License  : MIT
Requires: pypi-azure_mgmt_netapp-python = %{version}-%{release}
Requires: pypi-azure_mgmt_netapp-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(azure_common)
BuildRequires : pypi(azure_mgmt_core)
BuildRequires : pypi(msrest)

%description
This is the Microsoft Azure NetApp Files Management Client Library.
        This package has been tested with Python 2.7, 3.5, 3.6, 3.7 and 3.8.

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
%setup -q -n azure-mgmt-netapp-5.1.0
cd %{_builddir}/azure-mgmt-netapp-5.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639046992
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

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
