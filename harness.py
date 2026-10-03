"""Tiny offline test harness. No internet, no packages needed.

Run a problem file with:  python 01_valid_anagram.py
"""
import copy


def run_tests(func, cases, normalize=None, mutates=False):
    """cases: list of (args_tuple, expected).

    normalize: optional function applied to both result and expected before
               comparing (use when order does not matter).
    mutates:   True for in-place problems -- the first argument is checked
               after the call instead of the return value.
    """
    passed = 0
    failed = []
    for i, (args, expected) in enumerate(cases, 1):
        args_copy = copy.deepcopy(args)
        try:
            result = func(*args_copy)
            if mutates:
                result = args_copy[0]
            got, want = result, expected
            if normalize is not None:
                got, want = normalize(got), normalize(want)
            if got == want:
                passed += 1
            else:
                failed.append((i, args, expected, result))
        except Exception as exc:
            failed.append((i, args, expected, f"{type(exc).__name__}: {exc}"))

    print(f"{passed}/{len(cases)} passed")
    for i, args, expected, result in failed:
        print(f"\n  test {i} FAILED")
        print(f"    input:    {args}")
        print(f"    expected: {expected}")
        print(f"    got:      {result}")
    if not failed:
        print("All tests passed. Now check your time and space complexity.")
