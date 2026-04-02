.PHONY: generate

generate:
	openapi-python-client update \
		--path swagger.json \
		--config openapi-python-client.yaml \
		--output-path . \
		--overwrite
