Summary: Library providing the Gnome XSLT engine
Name: libxslt
Version: 1.1.26
Release: 2%{?dist}%{?extra_release}
License: MIT
Group: Development/Libraries
Source: ftp://xmlsoft.org/XSLT/libxslt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL: http://xmlsoft.org/XSLT/
Requires: libxml2 >= 2.6.27
BuildRequires: libxml2-devel >= 2.6.27
BuildRequires: python python-devel
BuildRequires: libxml2-python
BuildRequires: libgcrypt-devel
Prefix: %{_prefix}
Docdir: %{_docdir}
Patch0: multilib.patch

%description
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine

%package devel
Summary: Libraries, includes, etc. to embed the Gnome XSLT engine
Group: Development/Libraries
Requires: libxslt = %{version}-%{release}
Requires: libxml2-devel >= 2.6.27
Requires: libgcrypt-devel
Requires: pkgconfig

%description devel
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed.

%package python
Summary: Python bindings for the libxslt library
Group: Development/Libraries
Requires: libxslt = %{version}-%{release}
Requires: libxml2 >= 2.6.27
Requires: libxml2-python >= 2.6.27

%description python
The libxslt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libxslt library to apply XSLT transformations.

This library allows to parse sytlesheets, uses the libxml2-python
to load and save XML and HTML files. Direct access to XPath and
the XSLT transformation context are possible to extend the XSLT language
with XPath functions written in Python.

%prep
%setup -q
%patch0 -p1

%build
%configure
make
gzip -9 ChangeLog

%install
rm -fr %{buildroot}

%makeinstall

rm -fr $RPM_BUILD_ROOT%{_libdir}/*.la \
       $RPM_BUILD_ROOT%{_libdir}/python*/site-packages/libxsltmod*a

# multiarch crazyness on timestamp differences
touch -m --reference=$RPM_BUILD_ROOT/%{prefix}/include/libxslt/xslt.h $RPM_BUILD_ROOT/%{prefix}/bin/xslt-config

%clean
rm -fr %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)

%doc AUTHORS ChangeLog.gz NEWS README Copyright TODO FEATURES
%doc doc/*.html doc/html doc/tutorial doc/tutorial2 doc/*.gif
%doc doc/EXSLT
%doc %{_mandir}/man1/xsltproc.1*
%{_libdir}/lib*.so.*
%{_libdir}/libxslt-plugins
%{prefix}/bin/xsltproc

%files devel
%defattr(-, root, root)

%doc AUTHORS ChangeLog.gz NEWS README Copyright TODO FEATURES
%doc doc/libxslt-api.xml
%doc doc/libxslt-refs.xml
%doc doc/EXSLT/libexslt-api.xml
%doc doc/EXSLT/libexslt-refs.xml
%doc %{_mandir}/man3/libxslt.3*
%doc %{_mandir}/man3/libexslt.3*
%doc doc/*.html doc/html doc/*.gif doc/*.png
%doc doc/images
%doc doc/tutorial
%doc doc/tutorial2
%doc doc/EXSLT
%{_libdir}/lib*.so
%{_libdir}/*a
%{_libdir}/*.sh
%{prefix}/share/aclocal/libxslt.m4
%{prefix}/include/*
%{prefix}/bin/xslt-config
%{_libdir}/pkgconfig/libxslt.pc
%{_libdir}/pkgconfig/libexslt.pc

%files python
%defattr(-, root, root)

%doc AUTHORS ChangeLog.gz NEWS README Copyright FEATURES
%{_libdir}/python*/site-packages/libxslt.py*
%{_libdir}/python*/site-packages/libxsltmod*
%doc python/TODO
%doc python/libxsltclass.txt
%doc python/tests/*.py
%doc python/tests/*.xml
%doc python/tests/*.xsl

%changelog
* Tue Jul 13 2010 Daniel Veillard <veillard@redhat.com> 1.1.26-2
- Fix the release numbering
- Resolves: rhbz#604553

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.1.26-1.1
- Rebuilt for RHEL 6

* Thu Sep 24 2009 Daniel Veillard <veillard@redhat.com> 1.1.26-1
- couple of bug fixes
- export a symbol needed by lxml

* Mon Sep 21 2009 Daniel Veillard <veillard@redhat.com> 1.1.25-2
- fix a locking bug in 1.1.25

* Thu Sep 17 2009 Daniel Veillard <veillard@redhat.com> 1.1.25-1
- release of 1.1.25
- Add API versioning  for libxslt shared library
- xsl:sort lang support using the locale
- many bug fixes

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 1.1.24-3
- Rebuild for Python 2.6

* Wed Oct  8 2008 Daniel Veillard <veillard@redhat.com> 1.1.24-2.fc10
- CVE-2008-2935 fix

* Tue May 13 2008 Daniel Veillard <veillard@redhat.com> 1.1.24-1.fc10
- release of 1.1.24
- fixes a few bugs including the key initialization problem
- tentative fix for multiarch devel problems

* Mon Apr 28 2008 Daniel Veillard <veillard@redhat.com> 1.1.23-3.fc10
- and the previous patch was incomplte breaking the python bindings
  see 444317 and 444455

* Tue Apr 22 2008 Daniel Veillard <veillard@redhat.com> 1.1.23-2.fc10
- revert a key initialization patch from 1.1.23 which seems broken
  see rhbz#442097

* Tue Apr  8 2008 Daniel Veillard <veillard@redhat.com> 1.1.23-1.fc9
- upstream release 1.1.23
- bugfixes

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.22-2
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Daniel Veillard <veillard@redhat.com> 1.1.22-1
- upstream release 1.1.22 see http://xmlsoft.org/XSLT/news.html

* Tue Jun 12 2007 Daniel Veillard <veillard@redhat.com> 1.1.21-1
- upstream release 1.1.21 see http://xmlsoft.org/XSLT/news.html

* Thu Feb 15 2007 Adam Jackson <ajax@redhat.com>
- Add dist tag to Release to fix 6->7 upgrades.

* Wed Jan 17 2007 Daniel Veillard <veillard@redhat.com>
- upstream release 1.1.20 see http://xmlsoft.org/XSLT/news.html

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 1.1.19-2
- rebuild against python 2.5

* Wed Nov 29 2006 Daniel Veillard <veillard@redhat.com>
- upstream release 1.1.19 see http://xmlsoft.org/XSLT/news.html

* Thu Oct 26 2006 Daniel Veillard <veillard@redhat.com>
- upstream release 1.1.18 see http://xmlsoft.org/XSLT/news.html

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.1.17-1.1
- rebuild

* Tue Jun  6 2006 Daniel Veillard <veillard@redhat.com>
- upstream release 1.1.17 see http://xmlsoft.org/XSLT/news.html
