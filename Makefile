# Makefile utama untuk mengelola seluruh repo Numerical-Computation-Practicum

.PHONY: all clean run-regula run-romberg

# Build semua bagian
all:
	$(MAKE) -C romberg_integration
	# Python tidak perlu build

# Jalankan program Python Regula Falsi
run-regula:
	$(MAKE) -C regula_falsi run

# Jalankan program C Romberg
run-romberg:
	$(MAKE) -C romberg_integration run

# Bersihkan semua file hasil kompilasi/cache
clean:
	$(MAKE) -C regula_falsi clean
	$(MAKE) -C romberg_integration clean
