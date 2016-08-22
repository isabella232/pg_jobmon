%global _version 1.3.1


Name:           pg_jobmon
Version:        %{_version}
Release:        1%{?dist}
Summary:        postgresql extension for logging and monitoring automated jobs

Group:          Development/Tools
License:        pg_jobmon is released under the PostgreSQL License, a liberal Open Source license, similar to the BSD or MIT licenses
URL:            https://github.com/omniti-labs/pg_jobmon
Source0:        https://github.com/omniti-labs/pg_jobmon/archive/master.tar.gz
Obsoletes:      pg_jobmon <= 1.3.0
Provides:       pg_jobmon => 1.3.1


%description
pg_jobmon is an extension to add the capability to log the progress of running functions and provide a limited monitoring capability to those logged functions.
The logging is done in a NON-TRANSACTIONAL method, so that if your function fails for any reason, all steps up to that point are kept in the log tables.
See the pg_jobmon.md file in docs for more details. Also see the following blog for some examples and tips: http://www.keithf4.com/tag/pg_jobmon/

###############################################################################################################################################################
# Build requirements

BuildRoot: %(mktemp -ud %{_tmppath}/build/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: postgresql-devel, postgresql


###############################################################################################################################################################
#PREP and SETUP
# The prep directive removes existing build directory and extracts source code so we have a fresh code base .....-n flag where present, defines the name of the directory

%prep
%setup -n pg_jobmon-master


###############################################################################################################################################################
%build

make

###############################################################################################################################################################
%install
mkdir -p %{buildroot}/etc/profile.d
echo "export PATH=$PATH:%{pg_dir}/bin/" >> %{buildroot}/etc/profile.d/pg_jobmon.sh
echo "export USE_PGXS=1" >> %{buildroot}/etc/profile.d/pg_jobmon.sh
source %{buildroot}/etc/profile.d/pg_jobmon.sh

%make_install


###############################################################################################################################################################
%files
/etc/profile.d/pg_jobmon.sh
/usr/pgsql-9.5
