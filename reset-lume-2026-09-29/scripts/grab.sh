#!/bin/bash
S=/tmp/claude-0/-home-user-Dropshipping/194890f3-5dea-5898-afd6-d3b8aab39306/scratchpad
T=/root/.claude/projects/-home-user-Dropshipping/194890f3-5dea-5898-afd6-d3b8aab39306/tool-results
for f in $T/mcp-AutoDS-*.txt; do b=$(basename $f); [ -f $S/raw/$b ] || cp $f $S/raw/$b; done
for f in $S/raw/*.txt; do op=$(jq -r '.operation_id' $f); jq -c --arg op "$op" '.data.results[]? | del(.images) + {src:$op}' $f; done | jq -sc 'unique_by(._id)[]' > $S/all.jsonl
wc -l < $S/all.jsonl
