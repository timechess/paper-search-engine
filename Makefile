.PHONY: fmt lint dev-fe start-be build-fe init-service proto clean

FRONTEND = paper-search-fe
BACKEND = paper-search-be

fmt:
	(fd -e nix -X nixfmt {} \; -X alejandra -q {})
	(cd proto && buf format -w)
	(cd ${FRONTEND} && prettier . -w )
	(cd ${BACKEND} && ruff format .)


lint:
	(cd ${BACKEND} && ruff check .)
	(cd proto && buf lint)
	(cd ${FRONTEND} && pnpm lint)

dev-fe:
	(cd $(FRONTEND) && pnpm run dev)

start-be:
	(cd $(BACKEND) && poetry run python paper_search_be/main.py)

proto:
		(cd proto && buf generate)
		(cd ${FRONTEND} && pnpm i && rm -rf lib/gen && pnpm exec buf generate ../proto/paper_search/v1/paper_search.proto)
