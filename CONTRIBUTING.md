# Contributing to undertheseanlp@resources

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.

## Get Started!

1. Fork the `resources` repo on GitHub.

Clone your fork locally:

```
$ git clone git@github.com:your_name_here/resources.git
 ```

Install your local copy into a conda. Assuming you have conda installed, this is how you build for local development:

```
$ conda create -n resources python=3.6
$ cd resources 
$ python build.py
```

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put your new functionality into a function with a docstring, and add the feature to the list in README.rst.
3. The pull request should work for Python 3.6 and for PyPy. Check https://travis-ci.org/undertheseanlp/underthesea/pull_requests and make sure that the tests pass for all supported Python versions.


