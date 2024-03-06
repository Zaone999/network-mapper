import struct
from random import randint


class ICMP:
    def __init__(self, type, code):
        self.type = type
        self.code = code
        self.identifier = randint(0, 65535)
        self.seq_num = 1
        self.initial_message = struct.pack(
            "!BBHHH", self.type, self.code, 0, self.identifier, self.seq_num
        )
        self.checksum = self.getChecksum()
        self.message = struct.pack(
            "!BBHHH", self.type, self.code, self.checksum, self.identifier, self.seq_num
        )

    def calculate_checksum(self, message):
        countTo = (len(message) // 2) * 2
        sum = 0
        count = 0

        # Handle bytes in pairs (16 bits)
        while count < countTo:
            thisVal = message[count + 1] * 256 + message[count]
            sum = sum + thisVal
            sum = sum & 0xFFFFFFFF  # Necessary?
            count = count + 2

            # Handle last byte if applicable (odd-number of bytes)
            # Endianness should not be an issue here, as both byte and short values are in network order
            if countTo < len(message):
                sum = sum + message[len(message) - 1]
                sum = sum & 0xFFFFFFFF  # Necessary?

            sum = (sum >> 16) + (sum & 0xFFFF)  # Add high 16 bits to low 16 bits
            sum = sum + (sum >> 16)  # Add carry from above (if any)
            answer = ~sum  # Invert and truncate to 16 bits
            answer = answer & 0xFFFF  # Keep only the last 16 bits

            # Swap bytes. Bugger me if I know why.
            answer = answer >> 8 | (answer << 8 & 0xFF00)

        return answer

    def getChecksum(self):
        return self.calculate_checksum(self.initial_message)

    def __str__(self) -> str:
        return str(self.message)

    def send():
        pass
