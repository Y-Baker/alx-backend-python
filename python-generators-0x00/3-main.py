#!/usr/bin/python3
import sys
lazy_paginator = __import__('2-lazy_paginate').lazy_paginate


try:
    for page in lazy_paginator(5):
        for user in page:
            print(user)
        print("---")
    sys.stdout.write('\033[F')
    sys.stdout.write('\b\b\b')
    sys.stdout.flush()
except BrokenPipeError:
    sys.stderr.close()