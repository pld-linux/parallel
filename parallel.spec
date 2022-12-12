Summary:	Shell tool for executing jobs in parallel
Summary(pl.UTF-8):	Narzędzie powłoki do równoległego uruchamiania zadań
Name:		parallel
Version:	20221122
Release:	1
License:	GPL v3+
Group:		Applications/System
Source0:	https://ftp.gnu.org/gnu/parallel/%{name}-%{version}.tar.bz2
# Source0-md5:	3a2b8a4afe6f168d8d3ed58c126ef563
URL:		https://www.gnu.org/software/parallel/
BuildRequires:	perl-tools-pod
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.745
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

%description -l pl.UTF-8
GNU Parallel to narzędzie powłoki do równoległego uruchamiania zadań
przy użyciu jednej lub większej liczby maszyn. Zadanie to zwykle
pojedyncze polecenie lub mały skrypt, który ma być uruchomiony dla
każdego wiersza z wejścia. Zwykle wejściem jest lista plików, lista
hostów, lista użytkowników lub lista tabel.

Korzystający dotychczas z xargs uznają GNU Parallel za bardzo łatwe w
użyciu. Piszący pętle w języku powłoki zauważą, że GNU Parallel może
zastąpić większość pętli i przyspieszyć je poprzez uruchamianie zadań
równolegle. Użytkownicy programów ppss lub pexec zwykle uznają, że
GNU Parallel czyni polecenia bardziej czytelnymi.

GNU Parallel zapewnia dodatkowo, że wyjście poleceń jest takie samo,
jak przy sekwencyjnym uruchamianiu poleceń. Pozwala to wykorzystywać
wyjście z GNU Parallel jako wejście dla innych programów.

GNU Parallel jest zgodny co do wiersza poleceń z narzędziem parallel z
moreutils, ale oferuje dodatkowe możliwości.

%package -n env_parallel
Summary:	env_parallel shell function
Summary(pl.UTF-8):	Funkca powłoki env_parallel
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description -n env_parallel
env_parallel is a shell function that exports the current environment
to GNU Parallel.

%description -n env_parallel -l pl.UTF-8
env_parallel to funkcja powłoki eksportująca bieżące środowisko do
GNU Parallel.

%package -n bash-completion-parallel
Summary:	Bash completion for parallel commands
Summary(pl.UTF-8):	Bashowe uzupełnianie poleceń parallel
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 1:2.0

%description -n bash-completion-parallel
Bash completion for parallel commands.

%description -n bash-completion-parallel -l pl.UTF-8
Bashowe uzupełnianie poleceń parallel.

%package -n zsh-completion-parallel
Summary:	Zsh completion for parallel commands
Summary(pl.UTF-8):	Uzupełnianie poleceń parallel w Zsh
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	zsh

%description -n zsh-completion-parallel
Zsh completion for parallel commands.

%description -n zsh-completion-parallel -l pl.UTF-8
Uzupełnianie poleceń parallel w Zsh.

%prep
%setup -q

%{__sed} -i -e '1s,^#!.*perl,#!%{__perl},' src/{parallel,sem}
%{__sed} -i -e '1{\@^#!@d}' src/env_parallel.*
%{__sed} -i -e '1s,^#!/usr/bin/env ,#!/bin/,' src/env_* src/parset

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/parallel

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_mandir}/man1/{sql,parallel-sql}.1
touch $RPM_BUILD_ROOT%{_sysconfdir}/parallel/config
%{__rm} -rv $RPM_BUILD_ROOT%{_docdir}/parallel

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CITATION CREDITS NEWS README
%dir %{_sysconfdir}/parallel
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/parallel/config
%attr(755,root,root) %{_bindir}/niceload
%attr(755,root,root) %{_bindir}/parallel
%attr(755,root,root) %{_bindir}/parcat
%attr(755,root,root) %{_bindir}/parset
%attr(755,root,root) %{_bindir}/parsort
%attr(755,root,root) %{_bindir}/sem
%attr(755,root,root) %{_bindir}/sql
%{_mandir}/man1/niceload.1*
%{_mandir}/man1/parallel.1*
%{_mandir}/man1/parallel-sql.1*
%{_mandir}/man1/parcat.1*
%{_mandir}/man1/parset.1*
%{_mandir}/man1/parsort.1*
%{_mandir}/man1/sem.1*
%{_mandir}/man7/parallel_alternatives.7*
%{_mandir}/man7/parallel_book.7*
%{_mandir}/man7/parallel_design.7*
%{_mandir}/man7/parallel_examples.7*
%{_mandir}/man7/parallel_tutorial.7*

%files -n env_parallel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/env_parallel
%attr(755,root,root) %{_bindir}/env_parallel.ash
%attr(755,root,root) %{_bindir}/env_parallel.bash
%attr(755,root,root) %{_bindir}/env_parallel.csh
%attr(755,root,root) %{_bindir}/env_parallel.dash
%attr(755,root,root) %{_bindir}/env_parallel.fish
%attr(755,root,root) %{_bindir}/env_parallel.ksh
%attr(755,root,root) %{_bindir}/env_parallel.mksh
%attr(755,root,root) %{_bindir}/env_parallel.pdksh
%attr(755,root,root) %{_bindir}/env_parallel.sh
%attr(755,root,root) %{_bindir}/env_parallel.tcsh
%attr(755,root,root) %{_bindir}/env_parallel.zsh
%{_mandir}/man1/env_parallel.1*

%files -n bash-completion-parallel
%defattr(644,root,root,755)
%{bash_compdir}/parallel

%files -n zsh-completion-parallel
%defattr(644,root,root,755)
%{zsh_compdir}/_parallel
