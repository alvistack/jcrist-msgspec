# Copyright 2026 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-msgspec
Epoch: 100
Version: 0.20.0
Release: 1%{?dist}
Summary: A fast serialization and validation library
License: BSD-3-Clause
URL: https://github.com/jcrist/msgspec/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-pip

%description
msgspec is a fast serialization and validation library, with builtin
support for JSON, MessagePack, YAML, and TOML.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} >= 1500
%package -n python%{python3_version_nodots}-msgspec
Summary: A fast serialization and validation library
Requires: python3
Provides: python3-msgspec = %{epoch}:%{version}-%{release}
Provides: python3dist(msgspec) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-msgspec = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(msgspec) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-msgspec = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(msgspec) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-msgspec
msgspec is a fast serialization and validation library, with builtin
support for JSON, MessagePack, YAML, and TOML.

%files -n python%{python3_version_nodots}-msgspec
%license LICENSE
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} >= 1500)
%package -n python3-msgspec
Summary: A fast serialization and validation library
Requires: python3
Provides: python3-msgspec = %{epoch}:%{version}-%{release}
Provides: python3dist(msgspec) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-msgspec = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(msgspec) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-msgspec = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(msgspec) = %{epoch}:%{version}-%{release}

%description -n python3-msgspec
msgspec is a fast serialization and validation library, with builtin
support for JSON, MessagePack, YAML, and TOML.

%files -n python3-msgspec
%license LICENSE
%{python3_sitearch}/*
%endif

%changelog
