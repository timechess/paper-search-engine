import { PaperSearchResultTable } from "@/components/search-result";
import SearchBox from "@/components/searchbox";

export default async function StateSearchSearchPage(props: {
  searchParams?: Promise<{
    query?: string;
    results?: string;
  }>;
}) {
  const searchParams = await props.searchParams;

  const query = searchParams?.query;
  const results = Number.parseInt(searchParams?.results ?? "20");
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-gradient-to-r">
      <main className="flex flex-col items-center justify-center px-4 text-center mt-16 w-full">
        <h1 className="text-6xl font-extrabold text-gray-800 drop-shadow-lg">
          Paper Search
        </h1>
        <p className="mt-4 text-2xl text-gray-700 max-w-xl">
          Search academic papers in a semantic manner
        </p>
        <div className="container mx-32 py-10 mt-10 w-full">
          <SearchBox />
          {query ? (
            <div className="w-auto mx-auto text-start items-center mt-10">
              <PaperSearchResultTable query={query} results={results} />
            </div>
          ) : null}
        </div>
      </main>
    </div>
  );
}
