# Python 3.13 Compatibility Updates

This document tracks the changes made to update the codebase for Python 3.13 compatibility.

## Dependencies to Update

1. FastAPI and related:
   - fastapi (latest)
   - pydantic v2 (latest)
   - pytest (latest)
   - httpx (replacing requests)

2. Data Science Stack:
   - pandas (latest)
   - numpy (latest)
   - scikit-learn (latest)
   - aequitas (latest)
   - altair (latest)

3. Web Framework:
   - Flask (latest, replacing 0.12.2)
   - Flask-Bootstrap (latest)

## Code Changes Required

1. FastAPI Updates:
   - Update type hints in all FastAPI routes
   - Update pydantic models for v2 compatibility
   - Update test client usage
   - Replace requests with httpx for async HTTP calls

2. Notebook Updates:
   - Update kernel to Python 3.13
   - Update pandas syntax
   - Update scikit-learn imports and patterns
   - Update aequitas imports and usage
   - Add type hints to function definitions

## Progress Tracking

- [x] Update dependency specifications
  - Created requirements.txt with latest versions
  - Updated all Python packages to latest versions
  - Added httpx for modern async HTTP calls

- [x] Update FastAPI code
  - Updated type hints to use Python 3.13 style (list[] instead of List)
  - Added proper response models and return type annotations
  - Updated Pydantic models to use v2 style configuration
  - Added field validation and examples
  - Removed redundant validations in favor of Pydantic built-in validation
  - Added proper documentation and examples

- [x] Update notebooks
  - Updated package installation commands to use latest versions
  - Added type hints to function definitions
  - Updated pandas and scikit-learn patterns
  - Added async/await patterns where applicable

- [x] Update tests
  - Added type hints to test functions
  - Added async/await pattern with pytest.mark.anyio
  - Updated assertions to be more specific
  - Updated HTTP client usage to use json parameter
  - Updated expected status codes for validation errors (422)

- [x] Additional Updates
  - Replaced requests with httpx in sample_request.py
  - Updated HTTP client examples to use async/await pattern
  - Enhanced FastAPI application metadata and documentation
  - Added proper type hints throughout the codebase

- [x] Verify all changes
  - All FastAPI applications updated with latest best practices
  - Tests updated to match new patterns
  - Dependencies specified with minimum compatible versions
  - Code modernized for Python 3.13 features
  - Documentation and examples added/updated
