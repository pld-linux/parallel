%include	/usr/lib/rpm/macros.perl
Summary:	Shell tool for executing jobs in parallel
Name:		parallel
Version:	20150522
Release:	1
License:	GPL v3+
Group:		Applications/System
Source0:	http://ftp.gnu.org/gnu/parallel/%{name}-%{version}.tar.bz2
# Source0-md5:	baa13d9ed0caad76004e9fe9b9b78c72
URL:		http://www.gnu.org/software/parallel/
BuildRequires:	perl-tools-pod
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Parallel is a shell tool for executing jobs in parallel using one
or more machines. A job is typically a single command or a small
script that has to be run for each of the lines in the input. The
typical input is a list of files, a list of hosts, a list of users, or
a list of tables.

If you use xargs today you will find GNU Parallel very easy to use. If
you write loops in shell, you will find GNU Parallel may be able to
replace most of the loops and make them run faster by running jobs in
parallel. If you use ppss or pexec you will find GNU Parallel will
often make the command easier to read.

GNU Parallel also makes sure output from the commands is the same
output as you would get had you run the commands sequentially. This
makes it possible to use output from GNU Parallel as input for other
programs.

GNU Parallel is command-line-compatible with moreutils' parallel, but
offers additional features.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/parallel
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_mandir}/man1/{sql,parallel-sql}.1
:> $RPM_BUILD_ROOT%{_sysconfdir}/parallel/config
rm -rv $RPM_BUILD_ROOT%{_docdir}/parallel

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS
%doc src/parallel.html src/sem.html src/sql.html src/niceload.html
%doc src/*.texi
%dir %{_sysconfdir}/parallel
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/parallel/config
%attr(755,root,root) %{_bindir}/parallel
%attr(755,root,root) %{_bindir}/sem
%attr(755,root,root) %{_bindir}/sql
%attr(755,root,root) %{_bindir}/niceload
%{_mandir}/man1/niceload.1*
%{_mandir}/man1/parallel.1*
%{_mandir}/man1/sem.1*
%{_mandir}/man1/parallel-sql.1*
%{_mandir}/man7/parallel_design.7*
%{_mandir}/man7/parallel_tutorial.7*
