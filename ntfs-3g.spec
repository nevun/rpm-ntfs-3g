%define buildrev 20070920

Name:		ntfs-3g
Summary: 	Linux NTFS userspace driver 
Version:	0
Release:	0.3.%{buildrev}%{?dist}
License:	GPL
Group:		System Environment/Base
Source0:	http://mlf.linux.rulez.org/mlf/ezaz/%{name}-%{buildrev}-BETA.tgz
Patch0:		ntfs-3g-20070920-BETA-noldconfig.patch
URL:		http://mlf.linux.rulez.org/mlf/ezaz/ntfs-3g-download.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	fuse-devel
Requires:	fuse
Epoch:		1

%description
The ntfs-3g driver is an open source, GPL licensed, third generation 
Linux NTFS driver. It provides full read-write access to NTFS, excluding 
access to encrypted files, writing compressed files, changing file 
ownership, access right.

Technically it’s based on and a major improvement to the third 
generation Linux NTFS driver, ntfsmount. The improvements include 
functionality, quality and performance enhancements.

ntfs-3g features are being merged to ntfsmount. In the meanwhile, 
ntfs-3g is currently the only free, as in either speech or beer, NTFS 
driver for Linux that supports unlimited file creation and deletion.

%package devel
Summary:	Development files and libraries for ntfs-3g
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Headers and libraries for developing applications that use ntfs-3g 
functionality.

%prep
%setup -q -n %{name}-%{buildrev}-BETA
%patch0 -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la

# make the symlink an actual copy to avoid confusion
rm -rf $RPM_BUILD_ROOT/sbin/mount.ntfs-3g
cp -a $RPM_BUILD_ROOT%{_bindir}/ntfs-3g $RPM_BUILD_ROOT/sbin/mount.ntfs-3g

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING CREDITS NEWS README
/sbin/mount.ntfs-3g
%{_bindir}/ntfs-3g
%{_libdir}/libntfs-3g.so.*
%{_mandir}/man8/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/ntfs-3g/
%{_libdir}/libntfs-3g.so

%changelog
* Mon Oct 16 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1:0-0.3.20070920
- add explicit Requires on fuse

* Mon Oct 16 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1:0-0.2.20070920
- fixed versioning (bumped epoch, since it now shows as older)
- change sbin symlink to actual copy to be safe

* Sun Oct 15 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.1.20070920-1
- Initial package for Fedora Extras
