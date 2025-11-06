# Makefile for LIGO Tools Project

.PHONY: env html clean help

# Default target
help:
	@echo "Available targets:"
	@echo "  env    - Create/update conda environment"
	@echo "  html   - Build HTML documentation"
	@echo "  clean  - Clean generated files"
	@echo "  help   - Show this help message"

# Environment setup
env:
	@if conda env list | grep -q "ligo-tools"; then \
		echo "Updating existing ligo-tools environment..."; \
		conda env update -f environment.yml --prune; \
	else \
		echo "Creating new ligo-tools environment..."; \
		conda env create -f environment.yml; \
	fi

# Build HTML documentation
html:
	myst build --html

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	rm -rf figures/*
	rm -rf audio/*
	rm -rf _build/
	@echo "Clean complete!"