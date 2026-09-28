#!/bin/bash
# copy any new tool-result files into raw/ (idempotent)
S=/tmp/claude-0/-home-user-Dropshipping/edd3f668-73f0-5b21-9c24-f699ed49a66a/scratchpad
T=/root/.claude/projects/-home-user-Dropshipping/edd3f668-73f0-5b21-9c24-f699ed49a66a/tool-results
for f in $T/mcp-AutoDS-*.txt; do b=$(basename $f); [ -f $S/raw/$b ] || cp $f $S/raw/$b; done
# merge all results into all.jsonl keyed by _id (keep first seen, tag source op)
for f in $S/raw/*.txt; do op=$(jq -r '.operation_id' $f); jq -c --arg op "$op" '.data.results[]? | del(.images) + {src:$op}' $f; done | jq -sc 'unique_by(._id)[]' > $S/all.jsonl
wc -l < $S/all.jsonl
