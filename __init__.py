import filecmp
import shutil
import os
import json
import sys
import __main__
import requests

from .deepseek import DeepSeekChat

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    DeepSeekChat.NAME: DeepSeekChat,
}

# display name
NODE_DISPLAY_NAME_MAPPINGS = {
    DeepSeekChat.NAME: "DeepSeek Chat",
}

__all__ = [NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS]
