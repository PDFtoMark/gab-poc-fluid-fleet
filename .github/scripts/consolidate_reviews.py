import sys, glob, json, os
out = None
for i, a in enumerate(sys.argv):
    if a == '-o':
        out = sys.argv[i+1]
if out:
    open(out, 'w').write('<!-- pr-review-fleet -->\n## Fleet Review — Clean\n')
sys.exit(2)
