# The Ray Tracer Challenge - Python implementation

Things to watch out for:

* infinity in Python: `float('inf')` / `float('-inf')`
* epsilon for comparing floating point numbers (e.g. EPSILON=0.0001)

Via [Stackoverflow](https://stackoverflow.com/questions/8560131/pytest-assert-almost-equal)
```
assert 2.2 == pytest.approx(2.3)
# fails, default is ± 2.3e-06
assert 2.2 == pytest.approx(2.3, 0.1)
# passes

# also works the other way, in case you were worried:
assert pytest.approx(2.3, 0.1) == 2.2
# passes
```

## Notes

(x, y, z, w) - w = 0 for vector, 1 for points
