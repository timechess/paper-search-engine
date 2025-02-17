import { Client, createClient } from "@connectrpc/connect";
import {
  createGrpcTransport,
  GrpcTransportOptions,
} from "@connectrpc/connect-node";
import {
  PaperSearchService,
  QueryAugmentationRequest,
  QueryAugmentationResponse,
  SearchPaperRequest,
  SearchPaperResponse,
} from "./gen/paper_search/v1/paper_search_pb";

const baseUrl = "http://127.0.0.1:7720";

const grpcOptions: GrpcTransportOptions = {
  baseUrl,
};

const transport = createGrpcTransport(grpcOptions);

const paperSearchClient: Client<typeof PaperSearchService> = createClient(
  PaperSearchService,
  transport,
);

export const searchPaper: (
  request: SearchPaperRequest,
) => Promise<SearchPaperResponse> = async (request: SearchPaperRequest) => {
  return await paperSearchClient.searchPaper(request);
};

export const queryAugmentation: (
  request: QueryAugmentationRequest,
) => Promise<QueryAugmentationResponse> = async (
  request: QueryAugmentationRequest,
) => {
  return await paperSearchClient.queryAugmentation(request);
};
