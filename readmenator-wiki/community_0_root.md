# root

*Community 0 | 1 files | cohesion 1.00*

## Definition

This community groups 1 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `update_freq`, `wheelEvent`. Core file: `app.py` (2 symbols).

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `app.py` | py | utility | 2 | no |

## Key Symbols

- `wheelEvent` (function, `app.py:14`) `def wheelEvent(event)`
- `update_freq` (function, `app.py:77`) `def update_freq(value)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- No cross-community bridges recorded. This community is self-contained.

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `app.py`)? What purpose do they serve?
- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `app.py`
