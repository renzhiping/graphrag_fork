# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""A module containing load method definition."""

import logging
import re
from pathlib import Path
from typing import Any

import pandas as pd

from graphrag.index.config.input import PipelineInputConfig
from graphrag.index.utils.hashing import gen_sha512_hash
from graphrag.logging.base import ProgressReporter
from graphrag.storage.pipeline_storage import PipelineStorage

DEFAULT_FILE_PATTERN = re.compile(
    r".*[\\/](?P<source>[^\\/]+)[\\/](?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})_(?P<author>[^_]+)_\d+\.txt"
)
input_type = "json"
log = logging.getLogger(__name__)


async def load(
    config: PipelineInputConfig,
    progress: ProgressReporter | None,
    storage: PipelineStorage,
) -> pd.DataFrame:
    """Load text inputs from a directory."""

    return None
    
