from functools import lru_cache
from typing import cast

import numpy as np
from FlagEmbedding import BGEM3FlagModel

from app.config import settings


@lru_cache
def get_model() -> BGEM3FlagModel:
    return BGEM3FlagModel(settings.embedding_model, use_fp16=False)


def embed_texts(texts: list[str]) -> np.ndarray:
    if not texts:
        return np.empty((0, settings.embedding_dimension), dtype=np.float32)

    output = get_model().encode(
        texts,
        batch_size=8,
        max_length=512,
    )
    return cast(np.ndarray, output["dense_vecs"])
