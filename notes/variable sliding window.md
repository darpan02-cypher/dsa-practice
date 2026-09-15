The one idea you need

For variable sliding window:

left → [ window window window ] ← right

right keeps expanding.

When the window becomes invalid, move left until it becomes valid again.

for right in range(len(s)):
    # add s[right]

    while window_is_invalid:
        # remove s[left]
        left += 1

The difficult part is only:

What makes my window invalid, and what data structure tells me that?