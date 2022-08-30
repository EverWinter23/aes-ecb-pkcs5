.PHONY: tests
tests:
		py.test aes_ecb_pkcs5 --cov=aes_ecb_pkcs5 -vv

.PHONY: lint
lint:
		flake8 aes_ecb_pkcs5

.PHONY: format
format:
		isort aes_ecb_pkcs5
		black aes_ecb_pkcs5
