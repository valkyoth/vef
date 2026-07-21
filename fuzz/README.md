# Fuzzing

Fuzz targets are introduced with the first hostile-input implementation in
each component. The fuzz workspace remains outside published crates and may
not weaken the production dependency policy.
