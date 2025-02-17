"use server";

import { queryAugmentation } from "./grpc";

export async function queryAugment(query: string): Promise<string> {
  const augment_query = await queryAugmentation({
    $typeName: "paper_search.v1.QueryAugmentationRequest",
    query,
  });
  return augment_query.res;
}
