
## Requires
`homophones_get_all` action that returns a `dict[str, list[str]]` mapping a homophone
to all of its homophones (including itself).

## Recommended configuration
```talon
(rotate | cycle) <user.homophones_canonical>:
    user.rotate_word(homophones_canonical)
```
