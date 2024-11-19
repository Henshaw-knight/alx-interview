#!/usr/bin/env python3
"""validUTF8 function module"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
      data: List of integers, where each integer represents
         a byte (0-255)

    Returns:
      True if data is a valid UTF-8 encoding, else False
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks for the most significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        # Mask to consider only the least significant 8 bits
        byte &= 0xFF

        if num_bytes == 0:
            # Determine the number of bytes for the current character
            if (byte & mask1) == 0:  # 1-byte character
                continue
            elif (byte & 0xE0) == 0xC0:  # 2-byte character
                num_bytes = 1
            elif (byte & 0xF0) == 0xE0:  # 3-byte character
                num_bytes = 2
            elif (byte & 0xF8) == 0xF0:  # 4- byte character
                num_bytes = 3
            else:
                return False
        else:
            # Check continuation byte
            if (byte & 0xC0) != 0x80:
                return False
            num_bytes -= 1

    # If num_bytes is not 0, then not all characters were properly closed
    return num_bytes == 0
