# PG_JOBMON RPM built for RHEL 6.5

**Description**: This project to build an pg_jobmon spec file for building the pg_jobmon rpm package as an extension for Postgresql.

    pg_jobmon is an extension to add the capability to log the progress of running functions and provide a limited monitoring capability to those logged functions


  - **Technology stack**: 

    When installed pg_jobmon will serve as an extension for Postgresql. 



=======

## Dependencies

    The build process for the pg_jobmon rpm requires postgresql9.4-devel and postgresql9.4 (x86_64) packages. 
    And the package is intended for an x86_64 system.

## Installation

Build RPM using Vagrant
1. The repo is cloned into a local sandbox
2. Run "vagrant up" to build the VM.
3. Run "vagrant ssh" to connect to VM.
4. Run "rpmbuild -ba SPECS/pg_jobmon.spec" to build the pg_jobmon rpm package.

Build RPM on server
1. Once repo is cloned, run "sh ./bootstrap.sh"
2. cd to ~/rpmbuild 
3. Run "rpmbuild -ba /SPECS/pg_jobmon.spec"

Installing the RPM 
Install the built RPM by running "sudo yum install RPMS/x86_64/pg_jobmon-1.3.1-1.el6.x86_64.rpm"

## Configuration

    Edit the SPEC file (SPEC/pg_jobmon.spec) to make necessary changes to the build configuration

=======

## Usage

    Please refer to https://github.com/omniti-labs/pg_jobmon for details on usage.
    and the following pdf https://wiki.postgresql.org/images/0/08/Pgconfnyc2014_whenpgcantyoucan.pdf


## Known issues

    There is a compilation error that is displayed during the RPM build process. 
    This is corrected by setting the right path for pg_config
    These is related to the build process and does not affect the usability of the package install.

## Getting help

If you have questions, concerns, bug reports, etc, please file an issue in this repository's Issue Tracker.


## Getting involved

For general instructions on _how_ to contribute, please refer to [CONTRIBUTING](CONTRIBUTING.md).


----

## Open source licensing info
1. [TERMS](TERMS.md)
2. [LICENSE](LICENSE)
3. [CFPB Source Code Policy](https://github.com/cfpb/source-code-policy/)


----

## Credits and references

See below links
https://wiki.postgresql.org/images/0/08/Pgconfnyc2014_whenpgcantyoucan.pdf
https://github.com/omniti-labs/pg_jobmon
