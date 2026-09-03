# Changelog

All notable changes to this project are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [3.4.1]

Documentation only. The README and this changelog were trimmed; the package
itself is unchanged from `3.4.0`.

## [3.4.0]

The library is now fully open source. Everything it does at runtime is in this
repository: pure Python, no compiled extensions. Nothing in the package
contacts an external service other than Payme itself.

### Removed

- **Compiled distribution.** Wheels are `py3-none-any` instead of
  per-platform binaries. The Cython build pipeline, the Docker build image and
  the `.so` artifacts are removed.
- The `environs` dependency, which nothing in the package uses any more.

### Changed

- Packaging moved to a single `pyproject.toml`. The version is read from
  `payme.__version__`, so it is declared in one place.
- Minimum Python is 3.8.

### Unchanged

- Every public import: `from payme import Payme`,
  `from payme.views import PaymeWebHookAPIView`, the `payme` Django app, its
  models, migrations and admin.

## [3.3.2] and earlier

Released as compiled wheels. See the git history for details.
