#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dimRed
Version  : 0.2.2
Release  : 28
URL      : https://cran.r-project.org/src/contrib/dimRed_0.2.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dimRed_0.2.2.tar.gz
Summary  : A Framework for Dimensionality Reduction
Group    : Development/Tools
License  : GPL-3.0
Requires: R-CVST
Requires: R-kernlab
BuildRequires : R-CVST
BuildRequires : R-DRR
BuildRequires : R-RANN
BuildRequires : R-diffusionMap
BuildRequires : R-fastICA
BuildRequires : R-highr
BuildRequires : R-igraph
BuildRequires : R-keras
BuildRequires : R-kernlab
BuildRequires : R-rlang
BuildRequires : R-tinytex
BuildRequires : buildreq-R
BuildRequires : texlive

%description
techniques from R packages and a common
    interface for calling the methods.

%prep
%setup -q -c -n dimRed

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556494786

%install
export SOURCE_DATE_EPOCH=1556494786
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dimRed
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dimRed
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dimRed
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc dimRed || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/dimRed/CITATION
/usr/lib64/R/library/dimRed/DESCRIPTION
/usr/lib64/R/library/dimRed/INDEX
/usr/lib64/R/library/dimRed/LICENSE
/usr/lib64/R/library/dimRed/Meta/Rd.rds
/usr/lib64/R/library/dimRed/Meta/features.rds
/usr/lib64/R/library/dimRed/Meta/hsearch.rds
/usr/lib64/R/library/dimRed/Meta/links.rds
/usr/lib64/R/library/dimRed/Meta/nsInfo.rds
/usr/lib64/R/library/dimRed/Meta/package.rds
/usr/lib64/R/library/dimRed/Meta/vignette.rds
/usr/lib64/R/library/dimRed/NAMESPACE
/usr/lib64/R/library/dimRed/NEWS.md
/usr/lib64/R/library/dimRed/R/dimRed
/usr/lib64/R/library/dimRed/R/dimRed.rdb
/usr/lib64/R/library/dimRed/R/dimRed.rdx
/usr/lib64/R/library/dimRed/doc/dimensionality-reduction.R
/usr/lib64/R/library/dimRed/doc/dimensionality-reduction.Rnw
/usr/lib64/R/library/dimRed/doc/dimensionality-reduction.pdf
/usr/lib64/R/library/dimRed/doc/index.html
/usr/lib64/R/library/dimRed/help/AnIndex
/usr/lib64/R/library/dimRed/help/aliases.rds
/usr/lib64/R/library/dimRed/help/dimRed.rdb
/usr/lib64/R/library/dimRed/help/dimRed.rdx
/usr/lib64/R/library/dimRed/help/paths.rds
/usr/lib64/R/library/dimRed/html/00Index.html
/usr/lib64/R/library/dimRed/html/R.css
/usr/lib64/R/library/dimRed/tests/testthat.R
/usr/lib64/R/library/dimRed/tests/testthat/test_ICA.R
/usr/lib64/R/library/dimRed/tests/testthat/test_NNMF.R
/usr/lib64/R/library/dimRed/tests/testthat/test_PCA.R
/usr/lib64/R/library/dimRed/tests/testthat/test_PCA_L1.R
/usr/lib64/R/library/dimRed/tests/testthat/test_all.R
/usr/lib64/R/library/dimRed/tests/testthat/test_autoencoder.R
/usr/lib64/R/library/dimRed/tests/testthat/test_dataSets.R
/usr/lib64/R/library/dimRed/tests/testthat/test_dimRedData.R
/usr/lib64/R/library/dimRed/tests/testthat/test_dimRedMethod-class.R
/usr/lib64/R/library/dimRed/tests/testthat/test_dimRedResult.R
/usr/lib64/R/library/dimRed/tests/testthat/test_drr.R
/usr/lib64/R/library/dimRed/tests/testthat/test_embed.R
/usr/lib64/R/library/dimRed/tests/testthat/test_isomap.R
/usr/lib64/R/library/dimRed/tests/testthat/test_kPCA.R
/usr/lib64/R/library/dimRed/tests/testthat/test_misc.R
/usr/lib64/R/library/dimRed/tests/testthat/test_quality.R
/usr/lib64/R/library/dimRed/tests/testthat/test_umap.R
