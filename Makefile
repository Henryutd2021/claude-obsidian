# Top Paper Lab Makefile
# Test runner entry points for DragonScale machinery still in active use.
# (The setup-dragonscale target was removed after the 2026-05-11 plugin-scaffold
# archive. The installer now lives at wiki/_meta/dropped-plugin-scaffold/bin/.)

.PHONY: test test-address test-tiling test-boundary clean-test-state help

help:
	@echo "Top Paper Lab developer targets:"
	@echo "  make test              Run all DragonScale tests"
	@echo "  make test-address     scripts/allocate-address.sh tests (shell)"
	@echo "  make test-tiling      scripts/tiling-check.py tests (python, no ollama required)"
	@echo "  make test-boundary    scripts/boundary-score.py tests (python, no prereqs)"
	@echo "  make clean-test-state Remove runtime lockfiles and tiling cache"

test: test-address test-tiling test-boundary
	@echo ""
	@echo "All tests passed."

test-address:
	@echo "=== test_allocate_address.sh ==="
	@bash tests/test_allocate_address.sh

test-tiling:
	@echo "=== test_tiling_check.py ==="
	@python3 tests/test_tiling_check.py

test-boundary:
	@echo "=== test_boundary_score.py ==="
	@python3 tests/test_boundary_score.py

clean-test-state:
	@rm -f .vault-meta/.address.lock .vault-meta/.tiling.lock .vault-meta/tiling-cache.json .vault-meta/tiling-cache.*.tmp
	@echo "Runtime lockfiles and tiling cache removed."
