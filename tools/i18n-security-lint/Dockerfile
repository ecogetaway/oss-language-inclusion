FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml ./
COPY i18n_security_lint ./i18n_security_lint
RUN pip install .
ENTRYPOINT ["i18n-security-lint"]
