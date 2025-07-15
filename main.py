import sys
from fetch import mourad_fetch
from Sum import mourad_sum

if len(sys.argv) != 2:
    print("please enter this command to run: python mourad_main.py <owner/repo>")
else:
    x = sys.argv[1]
    try:
        y = mourad_fetch(x)
        for i, z in enumerate(y[:10], 1):
            print(f"[{i}]")
            print(mourad_sum(z))
            print("-" * 37)
    except Exception as e:
        print(f"error: {e}")
