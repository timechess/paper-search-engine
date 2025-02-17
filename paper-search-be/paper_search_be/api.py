from paper_search_be.paper_search.v1.paper_search_pb2_grpc import (
    PaperSearchServiceServicer,
)
from paper_search_be.paper_search.v1.paper_search_pb2 import (
    Paper,
    SearchPaperRequest,
    SearchPaperResponse,
    QueryAugmentationRequest,
    QueryAugmentationResponse,
)
from paper_search_be.utils import index, search
from typing import List
from sentence_transformers import SentenceTransformer
from torch.cuda import is_available


class PaperSearchServicer(PaperSearchServiceServicer):
    def __init__(self, papers: List[Paper]):
        self.papers = papers
        self.model = SentenceTransformer(
            "answerdotai/ModernBERT-base", "cuda" if is_available() else "cpu"
        )
        self.corpus_embeddings = index(self.model, papers, "data/embeddings.npy")

    async def SearchPaper(self, request: SearchPaperRequest, context):
        # TODO
        paper_idxes = search(
            self.model, request.query, self.corpus_embeddings, request.num_results
        )
        papers = [self.papers[i] for i in paper_idxes]
        return SearchPaperResponse(papers=papers)

    async def QueryAugmentation(self, request: QueryAugmentationRequest, context):
        # TODO
        return QueryAugmentationResponse(res="Not Implement yet")
