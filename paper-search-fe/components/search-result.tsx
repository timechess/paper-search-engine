import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "./ui/card";
import { Paper } from "@/lib/gen/paper_search/v1/paper_search_pb";
import { searchPaper } from "@/lib/grpc";

export const PaperCard: React.FC<{ paper: Paper }> = ({ paper }) => {
  return (
    <Card className="mb-4 bg-gray-200">
      <CardHeader>
        <CardTitle className="text-2xl">{paper.title}</CardTitle>
        <CardDescription>{paper.authors}</CardDescription>
      </CardHeader>
      <CardContent className="text-lg">{paper.abstract}</CardContent>
    </Card>
  );
};

export async function PaperSearchResultTable({
  query,
  results,
}: {
  query: string;
  results: number;
}) {
  const data = (
    await searchPaper({
      $typeName: "paper_search.v1.SearchPaperRequest",
      query,
      numResults: results,
    })
  ).papers;
  console.log(data)
  return (
    <div className="">
      {data.map((paper, id) => (
        <PaperCard key={id} paper={paper} />
      ))}
    </div>
  );
}
