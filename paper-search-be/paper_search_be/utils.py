from paper_search_be.paper_search.v1.paper_search_pb2 import Paper
from typing import List, Tuple
from sentence_transformers import SentenceTransformer
from numpy import ndarray
import numpy as np
from pathlib import Path
import os


def json2paper(json_paper) -> Paper:
    return Paper(
        title=json_paper["title"],
        abstract=json_paper["abstract"],
        authors=json_paper["authors"],
    )


def search(
    model: SentenceTransformer,
    query: str,
    corpus_embedding: ndarray[ndarray],
    num_results: int,
) -> ndarray[int]:
    """Search the corpus according to the query.

    Args:
        model: A sentence transformer model as embedding model.
        query: The query string.
        corpus_embedding: The embeddings of the documents in corpus. Note that the index matches that in corpus.
        num_results: The number of documents to return.

    Returns:
        The top num_results papers.
    """
    query_embedding = model.encode(
        [query], convert_to_numpy=True, normalize_embeddings=True
    ).reshape(-1, 1)
    scores = corpus_embedding @ query_embedding
    topk = np.argsort(scores, axis=0)[::-1][:num_results]
    return topk.reshape(-1)


def prompt(paper: Paper) -> str:
    """Transform the paper to certain format for the LM."""
    return f"<TITLE>{paper.title}<ABSTRACT>{paper.abstract}"


def check_cache(save_path: Path, num: int) -> Tuple[ndarray, bool]:
    """Check if the cache is valid."""
    if not os.path.exists(save_path):
        return (np.array([]), False)
    else:
        embeddings = np.load(save_path)
        return (embeddings, len(embeddings) == num)


def index(model: SentenceTransformer, corpus: List[Paper], save_path: Path):
    """
    Encode the corpus and manage cache.

    Args:
        model: A sentence transformer model as embedding model.
        corpus: The papers to encode.
        save_path: The cache path.

    Returns:
        The embeddings of the corpus.
    """
    corpus_prompts = list(map(lambda p: prompt(p), corpus))
    corpus_embeddings, valid = check_cache(save_path, len(corpus))
    if not valid:
        corpus_embeddings = model.encode(
            corpus_prompts,
            batch_size=1,
            show_progress_bar=True,
            normalize_embeddings=True,
            convert_to_numpy=True,
        )
        with open(save_path, "wb") as f:
            np.save(f, corpus_embeddings)
    return corpus_embeddings
