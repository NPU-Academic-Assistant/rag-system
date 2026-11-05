FROM python:3.12-slim 
WORKDIR /App/backend
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --timeout 1000 torch \
    --index-url https://download.pytorch.org/whl/cpu

RUN pip install --no-cache-dir --timeout 1000 --retries 10 \
    -r requirements.txt
COPY . .
RUN useradd --create-home appuser
USER appuser
EXPOSE 8000
CMD ["uvicorn", "RAG.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
