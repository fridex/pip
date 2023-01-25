"""PEP XXXX"""

import json
import hashlib

from typing import Dict

from pip._internal.utils.misc import hash_file

__all__ = [
    "Provenance",
]

PROVENANCE_METADATA_NAME = "provenance.json"


class Provenance:

    __slots__ = ["url", "sha256"]

    def __init__(self, url: str, sha256: str) -> None:
        self.url = url
        self.sha256 = sha256

    @classmethod
    def create(cls, url, file_path: str) -> "Provenance":
        """Create provenance instance and compute digest on files."""
        sha256 = hash_file(file_path)[0]
        return Provenance(url=url, sha256=sha256.hexdigest())

    def to_dict(self) -> Dict[str, str]:
        return {
            "url": self.url,
            "sha256": self.sha256,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), sort_keys=True, indent=True) + "\n"
