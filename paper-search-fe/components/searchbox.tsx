"use client";

import { useState } from "react";
import { Card, CardTitle } from "./ui/card";
import { Textarea } from "./ui/textarea";
import { Button } from "./ui/button";
import { usePathname, useRouter } from "next/navigation";
import { Slider } from "./ui/slider";
import { queryAugment } from "@/lib/action";

export default function SearchBox() {
  const [inputValue, setInputValue] = useState("");
  const [resultNum, setResultNum] = useState(20);
  const pathname = usePathname();
  const { replace } = useRouter();
  const handleSearch = (query: string, results: number) => {
    const params = new URLSearchParams();
    if (query) {
      params.set("query", query);
      params.set("results", String(results));
    } else {
      params.delete("query");
    }

    replace(`${pathname}?${params.toString()}`);
  };

  const handleClear = () => {
    setInputValue("");
  };

  const handleResultNum = (value: number[]) => {
    setResultNum(value[0]);
  };

  return (
    <Card className="p-8 w-full space-y-4 mx-auto border-black">
      <div className="flex mx-4">
        <CardTitle className="text-left mt-1 text-2xl">Query</CardTitle>
      </div>

      <Textarea
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        placeholder="Enter your query"
        className="h-[200px] mt-4 md:text-lg"
      />
      <div className="flex space-x-4 justify-between">
        <Button
          variant="outline"
          onClick={handleClear}
          className="w-1/6 border-black h-12 text-lg"
        >
          Clear
        </Button>
        <div className="text-left">
          <p className="mb-2">Number of Results: {resultNum}</p>
          <Slider
            defaultValue={[20]}
            max={100}
            step={10}
            onValueChange={handleResultNum}
            title="Number of Results"
            className="w-[360px]"
          />
        </div>
        <Button
          className="w-1/6 h-12 text-lg bg-blue-600"
          onClick={async () => {
            const augment_query = await queryAugment(inputValue);
            setInputValue(augment_query);
          }}
        >
          Query Augmentation
        </Button>
        <Button
          onClick={() => handleSearch(inputValue, resultNum)}
          className="w-1/6 h-12 text-lg"
        >
          Search
        </Button>
      </div>
    </Card>
  );
}
