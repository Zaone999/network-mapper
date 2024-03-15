import struct
from random import randint


class ICMP:
    def __init__(self, type=8, code=0, seq_num=1, checksum=None):
        self.type = type
        self.code = code
        self.identifier = randint(0, 65535)
        self.seq_num =  seq_num
        self.initial_message = struct.pack(
            "!BBHHH", self.type, self.code, 0, self.identifier, self.seq_num
        )
        if checksum is None:
            self.checksum = self._getChecksum()
        else:
            self.checksum = checksum
        self.message = struct.pack(
            "!BBHHH", self.type, self.code, self.checksum, self.identifier, self.seq_num
        )

    @staticmethod
    def parse_bytes(packet):
        icmp_type, icmp_code, icmp_checksum = struct.unpack("!BBH", packet[:4])
        return ICMP(icmp_type, icmp_code, icmp_checksum)

    def _calculate_checksum(self, message):
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

    def _getChecksum(self):
        return self._calculate_checksum(self.initial_message)

    def __str__(self) -> str:
        return str(
            f"ICMP type: {self.type}, ICMP code: {self.code}, ICMP checksum: {self.checksum}"
        )
